# Generated by Django 4.0.3 on 2022-03-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0018_job_applied_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]