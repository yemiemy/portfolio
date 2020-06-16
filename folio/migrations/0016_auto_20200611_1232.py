# Generated by Django 3.0.5 on 2020-06-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0015_auto_20200610_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/blog/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portfolio/works/'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='portfolio/recommendations/%Y/%m/'),
        ),
    ]
