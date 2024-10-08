# Generated by Django 4.2.9 on 2024-09-22 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_reports'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reports',
            options={'ordering': ['id', '-updated'], 'verbose_name': 'Reports', 'verbose_name_plural': 'Reports'},
        ),
        migrations.AlterField(
            model_name='reports',
            name='csv',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reports',
            name='graphic',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to=''),
        ),
    ]
