from django.db import models


class Skills(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    table = models.JSONField(default="{}", verbose_name="Данные для таблицы")
    chart = models.ImageField(upload_to='skills_images', blank=True, null=True, verbose_name="График")

    class Meta:
        verbose_name = "Навыки"
        verbose_name_plural = "Навыки"
