# Generated by Django 5.0.2 on 2024-03-01 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_editorsprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('headline', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('rating', models.IntegerField()),
                ('image', models.ImageField(upload_to='photos/post_img')),
                ('slug', models.SlugField(unique=True)),
                ('writer', models.CharField(default='unknown', max_length=100)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.editorsprofile')),
            ],
        ),
    ]
