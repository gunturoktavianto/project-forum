# Generated by Django 4.2.6 on 2023-10-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmain', '0002_auto_20231026_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Link',
            field=models.URLField(blank=True, null=True),
        ),
    ]