# Generated by Django 4.0.4 on 2022-05-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirst', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='hobbies',
            field=models.TextField(max_length=100),
        ),
    ]
