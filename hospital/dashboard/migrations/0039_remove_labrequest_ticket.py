# Generated by Django 2.2.7 on 2019-12-09 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_auto_20191207_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labrequest',
            name='ticket',
        ),
    ]
