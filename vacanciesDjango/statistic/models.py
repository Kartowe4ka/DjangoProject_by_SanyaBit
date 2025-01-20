from django.db import models


class Statistic(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    table = models.JSONField(default='{}', verbose_name="Данные для таблицы")
    chart = models.ImageField(upload_to='skills_images', blank=True, null=True, verbose_name="График")
    stat_class = models.CharField(max_length=50, null=True, verbose_name="К какой странице принадлежит анализ")
    is_active = models.BooleanField(default="False", verbose_name="Указывать на страницах")


    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистики"

    def __str__(self):
        return self.name

