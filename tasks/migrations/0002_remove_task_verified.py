# Generated by Django 2.0.2 on 2018-02-11 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='verified',
        ),
    ]