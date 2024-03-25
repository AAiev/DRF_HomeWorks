# Generated by Django 5.0.3 on 2024-03-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_user_avatar_remove_user_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatar/', verbose_name='аватар'),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='страна'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=35, null=True, verbose_name='телефон'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='имя'),
        ),
    ]
