# Generated by Django 2.2.7 on 2019-12-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0049_auto_20191209_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labrequest',
            name='created_by',
            field=models.IntegerField(),
        ),
    ]