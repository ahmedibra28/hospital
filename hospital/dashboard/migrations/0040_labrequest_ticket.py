# Generated by Django 2.2.7 on 2019-12-09 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_remove_labrequest_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='labrequest',
            name='ticket',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]