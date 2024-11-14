# Generated by Django 5.1.3 on 2024-11-12 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='about')),
            ],
            options={
                'verbose_name': 'About Images',
                'verbose_name_plural': 'About Images',
            },
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description1', models.CharField(blank=True, max_length=255, null=True)),
                ('description2', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_us')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='appointment')),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointment',
            },
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='classes')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='classes_teacher')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(max_length=255)),
                ('age', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('capacity', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Classes',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='ClassesMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Classes Main',
                'verbose_name_plural': 'Classes Main',
            },
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('icon_class', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Facilities',
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.CreateModel(
            name='FacilityMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Facility Main',
                'verbose_name_plural': 'Facility Main',
            },
        ),
        migrations.CreateModel(
            name='FooterMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Footer Main',
                'verbose_name_plural': 'Footer Main',
            },
        ),
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('icon_class', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Get In Touch',
                'verbose_name_plural': 'Get In Touch',
            },
        ),
        migrations.CreateModel(
            name='MainSaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Main Saction',
                'verbose_name_plural': 'Main Saction',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletter',
            },
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='gallery')),
            ],
            options={
                'verbose_name': 'Photo Gallery',
                'verbose_name_plural': 'Photo Gallery',
            },
        ),
        migrations.CreateModel(
            name='QuickLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_url', models.CharField(max_length=255)),
                ('link_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Quick Links',
                'verbose_name_plural': 'Quick Links',
            },
        ),
        migrations.CreateModel(
            name='Socials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, max_length=255)),
                ('html_class', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Socials',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description1', models.CharField(blank=True, max_length=255, null=True)),
                ('description2', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='teacher')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='team')),
                ('social_title1', models.CharField(blank=True, max_length=50, null=True)),
                ('social_title2', models.CharField(blank=True, max_length=50, null=True)),
                ('social_title3', models.CharField(blank=True, max_length=50, null=True)),
                ('social_url1', models.URLField(blank=True, max_length=255)),
                ('social_url2', models.URLField(blank=True, max_length=255)),
                ('social_url3', models.URLField(blank=True, max_length=255)),
                ('social_html_class1', models.CharField(blank=True, max_length=200, null=True)),
                ('social_html_class2', models.CharField(blank=True, max_length=200, null=True)),
                ('social_html_class3', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
            },
        ),
        migrations.CreateModel(
            name='TeamMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Team Main',
                'verbose_name_plural': 'Team Main',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Testimonials',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='TestimonialsBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials_blocks')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('profession', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Testimonials blocks',
                'verbose_name_plural': 'Testimonials blocks',
            },
        ),
    ]