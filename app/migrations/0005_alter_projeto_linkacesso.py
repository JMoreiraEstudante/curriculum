# Generated by Django 3.2.4 on 2021-09-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210901_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='linkAcesso',
            field=models.URLField(blank=True, null=True),
        ),
    ]
