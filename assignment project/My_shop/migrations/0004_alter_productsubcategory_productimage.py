# Generated by Django 4.1.4 on 2022-12-25 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_shop', '0003_alter_productsubcategory_productid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsubcategory',
            name='productimage',
            field=models.FileField(default='media/samsung_mobile.jpg', upload_to='media/images'),
        ),
    ]
