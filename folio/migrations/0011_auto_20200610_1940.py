# Generated by Django 3.0.5 on 2020-06-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0010_auto_20200610_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
