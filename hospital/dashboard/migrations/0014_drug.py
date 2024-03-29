# Generated by Django 2.2.7 on 2019-11-24 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20191122_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.CharField(max_length=100, unique=True)),
                ('feature', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
