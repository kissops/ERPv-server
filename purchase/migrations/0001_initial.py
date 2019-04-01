# Generated by Django 2.1.7 on 2019-04-01 13:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [("inventory", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="PurchasedProduct",
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
                ("cost", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_purchased_product",
                        to="inventory.Product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
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
                ("due_by", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseOrderLine",
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
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("complete", models.BooleanField(default=False)),
                ("complete_date", models.DateTimeField(blank=True, null=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_purchase_orders",
                        to="purchase.PurchasedProduct",
                    ),
                ),
                (
                    "purchase_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="purchase_order_lines",
                        to="purchase.PurchaseOrder",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
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
                ("address", models.TextField()),
                ("postcode", models.CharField(max_length=7)),
                ("phone", models.CharField(blank=True, max_length=64, null=True)),
                ("email", models.CharField(blank=True, max_length=128, null=True)),
                ("website", models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="supplier_purchase_orders",
                to="purchase.Supplier",
            ),
        ),
        migrations.AddField(
            model_name="purchasedproduct",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="supplier_products",
                to="purchase.Supplier",
            ),
        ),
    ]
