# Generated by Django 3.2.18 on 2023-05-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_alter_orden_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='DIRECCION',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
    ]
