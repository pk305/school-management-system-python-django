# Generated by Django 3.2.16 on 2023-12-31 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
