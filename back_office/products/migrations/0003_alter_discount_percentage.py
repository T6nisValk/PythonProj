# Generated by Django 4.2.7 on 2023-12-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_brand_brands_category_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
