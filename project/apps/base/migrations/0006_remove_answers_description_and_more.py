# Generated by Django 4.2.9 on 2024-09-21 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_delete_forms_questions_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='description',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='description',
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.TextField(blank=True, null=True),
        ),
    ]
