# Generated by Django 4.2.9 on 2024-09-21 17:37

import base.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_questions_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='priority',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True, validators=[base.models.validate_higher_value]),
        ),
        migrations.AddField(
            model_name='results',
            name='priority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.answers'),
        ),
    ]
