# Generated by Django 2.2.5 on 2020-03-23 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiBasic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
    ]
