# Generated by Django 3.2.8 on 2021-10-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0012_auto_20211021_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
