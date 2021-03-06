# Generated by Django 3.0.3 on 2020-05-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=100)),
                ('slug_path', models.SlugField(unique='True')),
                ('blog_description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='post_image')),
            ],
        ),
    ]
