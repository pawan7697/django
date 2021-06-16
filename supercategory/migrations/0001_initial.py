# Generated by Django 3.2.3 on 2021-06-08 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_alter_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supercategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(blank=True, max_length=50)),
                ('status', models.IntegerField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
