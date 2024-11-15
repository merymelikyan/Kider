# Generated by Django 5.1.3 on 2024-11-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_galleryimages_delete_classimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('icon_class', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Contact  Blocks',
                'verbose_name_plural': 'Contact  Blocks',
            },
        ),
        migrations.CreateModel(
            name='ContactUsMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description1', models.CharField(blank=True, max_length=255, null=True)),
                ('description2', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.URLField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Contact  Us Main',
                'verbose_name_plural': 'Contact  Us Main',
            },
        ),
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Error',
                'verbose_name_plural': 'Error',
            },
        ),
    ]
