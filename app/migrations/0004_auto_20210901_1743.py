# Generated by Django 3.2.4 on 2021-09-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_projeto_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='link',
            new_name='linkAcesso',
        ),
        migrations.AddField(
            model_name='projeto',
            name='linkGit',
            field=models.URLField(null=True),
        ),
    ]
