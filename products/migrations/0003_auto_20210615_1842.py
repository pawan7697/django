# Generated by Django 3.2.3 on 2021-06-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210614_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_img_nameB',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='products',
            name='product_img_nameS',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]