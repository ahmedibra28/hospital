# Generated by Django 2.2.7 on 2019-11-24 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0019_operaion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Operaion',
            new_name='Operation',
        ),
        migrations.RenameField(
            model_name='operation',
            old_name='operaion',
            new_name='operation',
        ),
    ]
