# Generated by Django 4.0.5 on 2022-07-04 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_features_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufactured_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
