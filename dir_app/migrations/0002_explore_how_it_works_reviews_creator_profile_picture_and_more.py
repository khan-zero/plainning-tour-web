# Generated by Django 5.0.7 on 2024-07-12 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dir_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Explore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField()),
                ('price', models.CharField(max_length=255)),
                ('typee', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('img', models.ImageField(upload_to='Explore')),
            ],
        ),
        migrations.CreateModel(
            name='How_it_works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.IntegerField()),
                ('listing_categories', models.IntegerField()),
                ('visitors', models.IntegerField()),
                ('happy_clients', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='creator',
            name='profile_picture',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('img', models.ImageField(upload_to='Blog')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dir_app.creator')),
            ],
        ),
        migrations.CreateModel(
            name='Client_reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dir_app.creator')),
            ],
        ),
    ]
