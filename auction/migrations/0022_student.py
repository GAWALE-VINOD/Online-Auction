# Generated by Django 3.2.12 on 2022-02-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0021_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=100)),
                ('sclass', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
            ],
        ),
    ]
