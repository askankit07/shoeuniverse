# Generated by Django 4.1.6 on 2023-04-06 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoeuniverse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateNewAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='CreateAccount',
        ),
    ]
