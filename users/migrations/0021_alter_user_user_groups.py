# Generated by Django 4.2.11 on 2024-03-28 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_user_user_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_groups',
            field=models.CharField(choices=[('Member', 'Member'), ('Moderator', 'Moderator')], max_length=10, verbose_name='группа пользователя'),
        ),
    ]
