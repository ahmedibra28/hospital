# Generated by Django 2.2.7 on 2019-12-07 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0037_auto_20191206_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labrequest',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='labrequest',
            name='group',
        ),
        migrations.AddField(
            model_name='labrequest',
            name='ticket',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Ticket'),
            preserve_default=False,
        ),
    ]
