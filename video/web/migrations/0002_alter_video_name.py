# Generated by Django 3.2.6 on 2021-08-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(default=None, max_length=256, verbose_name='视频名称'),
        ),
    ]
