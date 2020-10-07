# Generated by Django 3.1 on 2020-09-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_story_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='image',
        ),
        migrations.AddField(
            model_name='story',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]