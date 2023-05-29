from django.db import models

class Pages(models.Model):
    id = models.IntegerField(verbose_name = 'ID', primary_key=True)
    name = models.CharField(verbose_name = 'Name', max_length=50)
    content = models.TextField(verbose_name='HTML code')

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'