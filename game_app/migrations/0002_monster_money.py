# Generated by Django 4.0.6 on 2022-08-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='money',
            field=models.IntegerField(default=10),
        ),
    ]