# Generated by Django 4.1.6 on 2023-09-18 15:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('shoe', '0005_order_imageurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('CartId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('productId', models.CharField(max_length=36)),
                ('productName', models.CharField(max_length=100)),
                ('totalAmount', models.IntegerField()),
                ('imageUrl', models.URLField(default=None)),
                ('foreignKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoe.customer')),
            ],
        ),
    ]
