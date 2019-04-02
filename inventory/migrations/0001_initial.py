# Generated by Django 2.2 on 2019-04-02 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillOfMaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Bill of Materials',
                'ordering': ['product'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('quantity', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('allocated_for_jobs', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('desired_stock_level', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BOMItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bom_items', to='inventory.BillOfMaterials')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_bom_items', to='inventory.Product')),
            ],
        ),
        migrations.AddField(
            model_name='billofmaterials',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('product', models.ManyToManyField(related_name='product_locations', to='inventory.Product')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_locations', to='inventory.Warehouse')),
            ],
            options={
                'unique_together': {('warehouse', 'name')},
            },
        ),
    ]
