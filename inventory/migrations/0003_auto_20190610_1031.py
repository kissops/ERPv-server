# Generated by Django 2.2.2 on 2019-06-10 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20190411_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='warehouse',
            options={'ordering': ['name']},
        ),
    ]
