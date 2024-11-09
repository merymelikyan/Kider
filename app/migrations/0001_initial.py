# Generated by Django 5.1.3 on 2024-11-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(blank=True, max_length=55, null=True)),
                ('text2', models.CharField(blank=True, max_length=255, null=True)),
                ('text3', models.CharField(blank=True, max_length=255, null=True)),
                ('link_url', models.URLField(blank=True, null=True)),
                ('link_url2', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name1', models.CharField(blank=True, max_length=255, null=True)),
                ('link_name2', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Footer Text',
                'verbose_name_plural': 'Footer Text',
            },
        ),
        migrations.CreateModel(
            name='HeaderText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='header_text')),
            ],
            options={
                'verbose_name': 'Header Text',
                'verbose_name_plural': 'Header Text',
            },
        ),
    ]
