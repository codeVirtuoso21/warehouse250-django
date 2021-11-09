# Generated by Django 3.1.5 on 2021-05-10 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_product'),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
  
                ('district', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('cell', models.CharField(max_length=100)),
                ('delivery_address', models.CharField(max_length=170)),

                ('delivery_cost', models.IntegerField(default=0)),

                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('vendors', models.ManyToManyField(related_name='orders', to='vendor.Vendor')),

                ('shipped_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ordered', 'Ordered'), ('shipped', 'Shipped'), ('arrived', 'Arrived')], default='ordered', max_length=20)),                
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_paid', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='vendor.vendor')),
            ],
        ),
    ]
