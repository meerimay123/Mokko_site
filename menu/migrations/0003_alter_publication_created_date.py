# Generated by Django 5.0.6 on 2024-07-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='created_date',
            field=models.DateField(),
        ),
    ]
