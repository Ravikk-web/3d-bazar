# Generated by Django 4.2.7 on 2023-11-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_icon', models.CharField(max_length=50)),
                ('product_title', models.CharField(max_length=50)),
                ('product_des', models.TextField()),
            ],
        ),
    ]
