# Generated by Django 2.2.7 on 2019-12-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0043_labrequest_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='labrequest',
            name='myfield',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
