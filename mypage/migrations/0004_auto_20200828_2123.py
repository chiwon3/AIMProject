# Generated by Django 3.0.8 on 2020-08-28 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mypage', '0003_customurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUrl2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUrl3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='CustomUrl',
            new_name='CustomUrl1',
        ),
        migrations.RemoveField(
            model_name='tab12',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tab13',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tab21',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tab22',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tab23',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tab31',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tab32',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tab33',
            name='user',
        ),
        migrations.DeleteModel(
            name='tab11',
        ),
        migrations.DeleteModel(
            name='tab12',
        ),
        migrations.DeleteModel(
            name='tab13',
        ),
        migrations.DeleteModel(
            name='tab21',
        ),
        migrations.DeleteModel(
            name='tab22',
        ),
        migrations.DeleteModel(
            name='tab23',
        ),
        migrations.DeleteModel(
            name='tab31',
        ),
        migrations.DeleteModel(
            name='tab32',
        ),
        migrations.DeleteModel(
            name='tab33',
        ),
    ]
