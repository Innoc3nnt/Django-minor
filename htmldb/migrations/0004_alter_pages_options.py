# Generated by Django 4.2 on 2023-05-28 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("htmldb", "0003_pages_name_alter_pages_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pages",
            options={"verbose_name": "Page", "verbose_name_plural": "Pages"},
        ),
    ]