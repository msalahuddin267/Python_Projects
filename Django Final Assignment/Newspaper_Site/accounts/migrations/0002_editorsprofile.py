# Generated by Django 5.0.2 on 2024-03-01 20:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EditorsProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=17)),
                ('n_id', models.CharField(max_length=17)),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'OTHERS')])),
                ('educations', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('ragistraions_date', models.DateTimeField(auto_now_add=True)),
                ('profile_update_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('tota_posts', models.IntegerField(default=0)),
                ('average_rating', models.FloatField(default=0.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]