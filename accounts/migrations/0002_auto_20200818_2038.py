# Generated by Django 2.0.2 on 2020-08-18 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='나이'),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='위치'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='닉네임'),
        ),
    ]
