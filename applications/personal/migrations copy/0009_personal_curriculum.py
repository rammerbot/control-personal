# Generated by Django 4.1.4 on 2023-01-29 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0008_remove_personal_curriculum'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='curriculum',
            field=models.FileField(blank=True, upload_to='curriculums/', verbose_name='Curriculum'),
        ),
    ]
