# Generated by Django 2.2 on 2019-04-11 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="InventoryLedger",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={"verbose_name_plural": "Inventory ledger"},
        ),
        migrations.CreateModel(
            name="ManufacturingLedger",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={"verbose_name_plural": "Manufacturing ledger"},
        ),
        migrations.CreateModel(
            name="PurchaseLedger",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={"verbose_name_plural": "Purchase ledger"},
        ),
        migrations.CreateModel(
            name="SalesLedger",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("value", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={"verbose_name_plural": "Sales ledger"},
        ),
    ]