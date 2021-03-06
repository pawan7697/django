# Generated by Django 3.2.3 on 2021-06-12 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
        ('supercategory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supercategory',
            name='supercategory_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='supercategory',
            name='subcategory_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subcategory.subcategory'),
        ),
    ]
