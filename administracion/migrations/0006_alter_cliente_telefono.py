# Generated by Django 3.2.18 on 2023-05-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0005_cliente_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='TELEFONO',
            field=models.CharField(default=52, max_length=15),
            preserve_default=False,
        ),
    ]
