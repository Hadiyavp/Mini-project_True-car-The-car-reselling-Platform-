# Generated by Django 3.2.25 on 2024-11-09 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TC', '0012_category_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='bodytype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]