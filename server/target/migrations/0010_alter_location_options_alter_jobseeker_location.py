# Generated by Django 4.0.3 on 2022-03-11 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0009_jobseeker_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={},
        ),
        migrations.AlterField(
            model_name='jobseeker',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_seeker_location', to='target.location'),
        ),
    ]
