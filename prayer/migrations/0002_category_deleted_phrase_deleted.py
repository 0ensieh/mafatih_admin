# Generated by Django 4.2.4 on 2023-09-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prayer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phrase',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
