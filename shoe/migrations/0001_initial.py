# Generated by Django 4.1.6 on 2023-09-04 14:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('productId', models.CharField(max_length=36)),
                ('productName', models.CharField(max_length=100)),
                ('productQty', models.IntegerField()),
                ('totalAmount', models.IntegerField()),
            ],
        ),
    ]