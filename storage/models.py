from django.db import models


class Bearing(models.Model):
    
    class Element(models.TextChoices):
        BALL = 'B', 'Шариковый'
        ROLLER = 'R', 'Роликовый'
        SLIDING = 'S', 'Скольжения'
    
    manufacturer = models.CharField("Производитель", max_length=40, help_text='производитель')
    number = models.CharField("Номер подшипника", max_length=40, help_text='номер подшипника')
    slug = models.SlugField("URL", max_length=50, null=False, unique=True, editable=True, help_text='URL')
    image = models.ImageField("Изображение", upload_to="storage/bearings/", help_text='изображение', null=True, blank=True)
    element_type = models.CharField("Тип подшипника", max_length=1, choices=Element.choices, help_text='тип подшипника')
    outer_diameter = models.PositiveIntegerField("Наружный диаметр", help_text='наружный диаметр', null=True, blank=True)
    inner_diameter = models.PositiveIntegerField("Внутренный диаметр", help_text='внутренный диаметр', null=True, blank=True)
    
    class Meta:
        verbose_name = "Подшипник"
        verbose_name_plural = "Подшипники"
        ordering = ['manufacturer', 'number']
        indexes = [
            models.Index(fields=['manufacturer', 'number']),
        ]
        
    def __str__(self):
        return f'{self.manufacturer} {self.number}'
    
    
class MechSeal(models.Model):
    label = models.CharField("Марка ТУ", max_length=40, null=True, blank=True, help_text='марка ТУ')
    manufacturer = models.CharField("Производитель", max_length=40, help_text='производитель')
    assembly_code = models.CharField("Код сборки", max_length=40, help_text='код сборки')
    slug = models.SlugField("URL", max_length=50, null=False, unique=True, editable=True, help_text='URL')
    image = models.ImageField("Изображение", upload_to="storage/mech_seals/", help_text='изображение', null=True, blank=True)
    material_id = models.CharField("ID материала", max_length=40, help_text='id материала', null=True, blank=True)
    repair_kit_id = models.CharField("ID ремонтного комплекта", max_length=40, help_text='id ремонтного комплекта', null=True, blank=True)
    
    class Meta:
        verbose_name = "Торцевое уплотнение"
        verbose_name_plural = "Торцевые уплотнения"
        ordering = ['manufacturer', 'label', 'assembly_code']
        indexes = [
            models.Index(fields=['manufacturer', 'label', 'assembly_code']),
        ]
        
    def __str__(self):
        return f'{self.manufacturer} {self.label}'