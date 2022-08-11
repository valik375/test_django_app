# Generated by Django 4.0.6 on 2022-08-10 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0002_hero_max_health_monster_max_health'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('damage', models.IntegerField(default=20)),
                ('hero', models.ManyToManyField(to='game_app.hero')),
            ],
        ),
    ]
