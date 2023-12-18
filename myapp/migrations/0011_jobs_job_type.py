# Generated by Django 4.2.7 on 2023-12-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_jobs_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_type',
            field=models.CharField(choices=[('part-time', 'part-time'), ('full-time', 'full-time')], default='full-time', max_length=200),
        ),
    ]
