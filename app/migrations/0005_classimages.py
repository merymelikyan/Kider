# Generated by Django 5.1.3 on 2024-11-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_teamblocks_delete_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='class')),
            ],
            options={
                'verbose_name': 'Class Images',
                'verbose_name_plural': 'Class Images',
            },
        ),
    ]
