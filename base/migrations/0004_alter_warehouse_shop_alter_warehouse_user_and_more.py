# Generated by Django 5.0.2 on 2024-03-04 06:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_shopid_warehouse_shop'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.shop'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='warehouse_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
