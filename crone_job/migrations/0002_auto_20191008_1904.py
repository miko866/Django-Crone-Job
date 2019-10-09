# Generated by Django 2.2.6 on 2019-10-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crone_job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cronjob',
            old_name='userweb',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='cronjob',
            name='user',
        ),
        migrations.AddField(
            model_name='cronjob',
            name='password',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]