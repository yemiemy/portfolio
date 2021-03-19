# Generated by Django 3.0.5 on 2020-06-10 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0009_auto_20200610_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='credit',
            field=models.CharField(default='Photo by ', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/'),
        ),
    ]