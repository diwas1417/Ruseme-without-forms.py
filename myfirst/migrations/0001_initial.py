# Generated by Django 4.0.4 on 2022-05-25 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(max_length=100, null=True)),
                ('update_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_void', models.BooleanField(default=False, null=True)),
                ('void_remarks', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profileimg')),
                ('school', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('skill', models.TextField(max_length=100)),
                ('about_you', models.TextField(max_length=100)),
                ('experience', models.TextField(max_length=100)),
                ('hobbies', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
