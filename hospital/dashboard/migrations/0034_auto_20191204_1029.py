# Generated by Django 2.2.7 on 2019-12-04 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_surgeryhistory_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surgeryhistory',
            old_name='pso',
            new_name='spo',
        ),
    ]