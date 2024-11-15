# Generated by Django 5.1.3 on 2024-11-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_classimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='gallery')),
            ],
            options={
                'verbose_name': 'Gallery Images',
                'verbose_name_plural': 'Gallery Images',
            },
        ),
        migrations.DeleteModel(
            name='ClassImages',
        ),
    ]
