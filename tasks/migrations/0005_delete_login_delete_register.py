# Generated by Django 5.1.4 on 2025-01-05 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_login_register_delete_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]