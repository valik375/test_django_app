# Generated by Django 4.0.6 on 2022-08-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='max_health',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='monster',
            name='max_health',
            field=models.IntegerField(default=60),
        ),
    ]
