# Generated by Django 3.1.6 on 2021-02-13 11:59

from django.db import migrations, models
import se.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to=se.models.get_file_path)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('file_name', models.TextField()),
                ('one', models.CharField(max_length=100)),
                ('two', models.CharField(max_length=100)),
                ('three', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
