# Generated by Django 3.2.12 on 2022-02-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0016_alter_prod_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prod',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]