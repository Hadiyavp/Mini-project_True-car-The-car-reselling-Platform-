# Generated by Django 3.2.25 on 2024-11-09 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TC', '0013_bodytype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_booking',
            name='status',
            field=models.CharField(max_length=2000),
        ),
    ]
