# Generated by Django 4.2.6 on 2023-10-22 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comunicado_entidad_delete_post_comunicado_entidad_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comunicado',
            options={'verbose_name_plural': 'Crear comunicado'},
        ),
        migrations.AlterModelOptions(
            name='entidad',
            options={'verbose_name_plural': 'Agregar entidad'},
        ),
        migrations.AlterField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(max_length=500, upload_to='images/'),
        ),
    ]