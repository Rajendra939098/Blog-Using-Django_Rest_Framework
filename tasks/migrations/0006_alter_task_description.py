# Generated by Django 5.1.4 on 2025-01-07 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_delete_login_delete_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=150),
        ),
    ]
