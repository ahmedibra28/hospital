# Generated by Django 2.2 on 2019-11-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='updated_by',
            field=models.IntegerField(),
        ),
    ]