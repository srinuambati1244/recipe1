# Generated by Django 3.1.7 on 2021-03-28 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recp', '0002_receipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='image',
            field=models.ImageField(upload_to='image/'),
        ),
    ]
