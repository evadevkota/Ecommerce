# Generated by Django 4.2.4 on 2023-09-01 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0017_product_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="product", name="User",),
    ]