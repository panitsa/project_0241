# Generated by Django 4.2.8 on 2024-01-08 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panitsa', '0002_villagepublic'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_news',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='activity_news',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
