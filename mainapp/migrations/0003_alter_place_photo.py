# Generated by Django 3.2.6 on 2022-08-01 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_place_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='photo',
            field=models.ImageField(blank=True, default='place/photo/defalt_image.png', upload_to='place/photo/%Y/%m/%d'),
        ),
    ]