# Generated by Django 3.2.9 on 2021-11-22 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=122)),
                ('state', models.CharField(max_length=122)),
                ('avgspeed', models.CharField(max_length=122)),
                ('temp', models.CharField(max_length=122)),
                ('fuel', models.CharField(max_length=122)),
                ('engine', models.CharField(max_length=122)),
                ('location', models.CharField(max_length=122)),
            ],
        ),
    ]
