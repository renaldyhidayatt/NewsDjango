# Generated by Django 3.1.6 on 2021-02-13 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacklistIp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blacklist',
            name='date',
            field=models.CharField(default='-', max_length=12),
        ),
    ]
