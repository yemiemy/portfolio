# Generated by Django 3.0.5 on 2020-06-10 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('recommendation', models.CharField(max_length=120)),
            ],
        ),
    ]
