# Generated by Django 3.2.8 on 2021-10-19 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0006_auto_20211019_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]