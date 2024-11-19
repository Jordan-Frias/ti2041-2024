# Generated by Django 5.1.1 on 2024-10-21 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("productos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Caracteristica",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Marca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="producto",
            name="fecha_vencimiento",
        ),
        migrations.AddField(
            model_name="producto",
            name="precio",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="producto",
            name="categoria",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="productos.categoria",
            ),
        ),
        migrations.AlterField(
            model_name="producto",
            name="marca",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="productos.marca",
            ),
        ),
        migrations.CreateModel(
            name="ProductoCaracteristica",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("valor", models.CharField(max_length=100)),
                (
                    "caracteristica",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productos.caracteristica",
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="productos.producto",
                    ),
                ),
            ],
            options={
                "unique_together": {("producto", "caracteristica")},
            },
        ),
        migrations.AddField(
            model_name="producto",
            name="caracteristicas",
            field=models.ManyToManyField(
                through="productos.ProductoCaracteristica",
                to="productos.caracteristica",
            ),
        ),
    ]
