# Generated by Django 5.0.6 on 2024-06-26 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_remove_boletacompra_detalles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]