# Generated by Django 5.0.6 on 2024-06-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_producto_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.PositiveIntegerField(),
        ),
    ]