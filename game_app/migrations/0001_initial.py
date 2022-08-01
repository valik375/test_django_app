# Generated by Django 4.0.6 on 2022-07-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateGame',
            fields=[
                ('user_name', models.CharField(max_length=200)),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(verbose_name=True)),
            ],
        ),
    ]
