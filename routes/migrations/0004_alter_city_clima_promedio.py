# Generated by Django 5.1.1 on 2024-11-15 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_remove_city_attractions_remove_city_average_climate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='clima_promedio',
            field=models.CharField(blank=True, help_text='Clima promedio', max_length=50, null=True),
        ),
    ]
