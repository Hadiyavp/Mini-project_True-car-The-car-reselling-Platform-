# Generated by Django 3.2.25 on 2024-10-20 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TC', '0003_product_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='testdrive_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('PRODUCT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TC.product_table')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TC.user_table')),
            ],
        ),
    ]