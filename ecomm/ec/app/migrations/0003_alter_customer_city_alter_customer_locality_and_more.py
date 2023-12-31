# Generated by Django 4.1.3 on 2023-02-05 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='locality',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Lomé', 'TOGO'), ('Accra', 'GHANA')], max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CR', 'Curd'), ('ML', 'Milk'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('IC', 'Ice-Creams')], max_length=2),
        ),
    ]
