from django.db import models
from django.utils.text import slugify
from django.urls import reverse

import random
import string

from storage.models import Bearing, MechSeal
from django.conf import settings


def rand_slug():
    """
    Generates a random slug consisting of lowercase letters and digits.
    """
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))


class Category(models.Model):
    title = models.CharField("Название", max_length=50, blank=False, null=False, db_index=True, help_text='категория оборудования')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', help_text='родительская категория')
    description = models.TextField("Описание", blank=True, null=True, help_text='описание')
    slug = models.CharField("URL", max_length=50, null=False, unique=True, editable=True, help_text='URL')
    image = models.ImageField("Изображение", upload_to="categories/", blank=True, null=True, help_text='изображение категории')
        
    class Meta:
        unique_together = (["slug", "parent"])
        ordering = ["title"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return " > ".join(full_path[::-1])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-pickBetter" + self.title)
        super(Category, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("equipment:category-detail", args=str(self.pk))
    
        
        
class Equipment(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", help_text='категория оборудования')
    position = models.CharField("Позиция", max_length=25, blank=False, null=False, unique=True, help_text='позиция оборудования')
    manufacturer = models.CharField("Производитель", max_length=50, blank=True, null=True, help_text='производитель оборудования')
    label = models.CharField("Название", max_length=50, blank=False, null=False, db_index=True, help_text='название оборудования')
    inventory_number = models.CharField("Инвентарный номер", max_length=20, blank=True, null=True, unique=True, help_text='инвентарный номер')
    slug = models.SlugField("Адресная строка", max_length=50, null=False, unique=True, editable=True, help_text='URL')
    description = models.TextField("Описание", blank=True, null=True, help_text='описание')
    image = models.ImageField("Изображение", upload_to="equipment/", help_text='изображение')
    mech_seal = models.ForeignKey(MechSeal, on_delete=models.DO_NOTHING, related_name='mech_seal', blank=True, null=True, help_text='торцевое уплотнение')
    bearings = models.ManyToManyField(Bearing, blank=True, help_text='подшипники')

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"
        ordering = ['position', 'label']
        indexes = [
            models.Index(fields=['inventory_number']),
            models.Index(fields=['position']),
        ]

    def __str__(self):
        return f'{self.position} - {self.manufacturer} {self.label}'
    
    def get_absolute_url(self):
        return reverse("equipment:equipment-detail", args=str(self.slug))