# Generated by Django 4.1.1 on 2022-09-13 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
