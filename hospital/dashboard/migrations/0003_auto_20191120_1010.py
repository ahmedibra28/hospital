# Generated by Django 2.2.7 on 2019-11-20 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_auto_20191119_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('birth_date', models.DateField(max_length=10)),
                ('address', models.CharField(choices=[('Banaadir', 'Banaadir'), ('Jubbada Dhexe', 'Jubbada Dhexe'), ('Jubbada Hoose', 'Jubbada Hoose'), ('Mudug', 'Mudug'), ('Hiiran', 'Hiiran'), ('Awdal', 'Awdal'), ('Bakool', 'Bakool'), ('Bari', 'Bari'), ('Baay', 'Baay'), ('Galgaduud', 'Galgaduud'), ('Gedo', 'Gedo'), ('Nugaal', 'Nugaal'), ('Sanaag', 'Sanaag'), ('Shabeellaha Hoose', 'Shabeellaha Hoose'), ('Shabeellaha Dhexe', 'Shabeellaha Dhee'), ('Sool', 'Sool'), ('Togdheer', 'Togdheer'), ('Woqooyi Galbeed', 'Woqooyi Galbeed')], default='Banaadir', max_length=20)),
                ('mobile', models.CharField(max_length=15)),
                ('emp_type', models.CharField(choices=[('Nurse', 'Nurse'), ('Doctor', 'Doctor'), ('Other', 'Other')], default='Nurse', max_length=6)),
                ('title', models.CharField(max_length=100)),
                ('value', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.IntegerField()),
                ('updated_by', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]