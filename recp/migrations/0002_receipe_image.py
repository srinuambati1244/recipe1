# Generated by Django 3.1.7 on 2021-03-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]
