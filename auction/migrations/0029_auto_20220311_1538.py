# Generated by Django 3.2 on 2022-03-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0028_rename_image_prod_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prod',
            old_name='images',
            new_name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='temp',
            field=models.IntegerField(null=True),
        ),
    ]
