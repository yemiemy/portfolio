# Generated by Django 3.0.5 on 2020-06-10 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('category', models.CharField(default='Travels', max_length=120)),
                ('body', models.TextField()),
                ('blockquote', models.CharField(max_length=1500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/%Y/%m/')),
                ('tag', models.CharField(max_length=120)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('subject', models.CharField(max_length=750)),
                ('message', models.TextField()),
                ('date_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=120)),
                ('website', models.CharField(blank=True, max_length=120, null=True)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='folio.Blog')),
            ],
        ),
    ]
