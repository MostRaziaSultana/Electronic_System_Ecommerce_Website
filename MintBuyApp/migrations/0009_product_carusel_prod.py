# Generated by Django 4.2.4 on 2023-10-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MintBuyApp', '0008_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='carusel_prod',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]