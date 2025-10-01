from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
import re


class LoginRequiredMiddleware:
    """Require authentication for all views except a safe allowlist.

    Exempt paths: admin, accounts (allauth), static, media, and health/simple probes if needed.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        static_url = getattr(settings, "STATIC_URL", "/static/") or "/static/"
        media_url = getattr(settings, "MEDIA_URL", "/media/") or "/media/"
        self.exempt_url_patterns = [
            r"^/admin/",
            r"^/accounts/",
            rf"^{re.escape(static_url)}",
            rf"^{re.escape(media_url)}",
        ]
        self.exempt_regexes = [re.compile(p) for p in self.exempt_url_patterns]

    def __call__(self, request):
        path = request.path

        is_exempt = any(r.match(path) for r in self.exempt_regexes)
        if is_exempt or request.user.is_authenticated:
            return self.get_response(request)

        login_url = reverse("account_login") if hasattr(settings, "LOGIN_URL") else "/accounts/login/"
        return redirect(f"{login_url}?next={request.get_full_path()}")


