# Generated by Django 3.2 on 2022-03-05 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0027_rename_images_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prod',
            old_name='image',
            new_name='images',
        ),
    ]