# Generated by Django 5.0.3 on 2024-03-21 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]