# Generated by Django 5.0.6 on 2024-06-23 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_profile_apellido_materno_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='date_of_birth',
            new_name='fecha_nacimiento',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='apellido_paterno',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='numero_celular',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='primer_nombre',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='segundo_nombre',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
