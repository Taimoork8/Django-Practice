# Generated by Django 5.0.2 on 2024-03-02 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_warehouse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warehouse',
            old_name='shopId',
            new_name='shop',
        ),
    ]
