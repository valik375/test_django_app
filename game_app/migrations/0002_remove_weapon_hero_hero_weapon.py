# Generated by Django 4.0.6 on 2022-08-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weapon',
            name='hero',
        ),
        migrations.AddField(
            model_name='hero',
            name='weapon',
            field=models.ManyToManyField(to='game_app.weapon'),
        ),
    ]