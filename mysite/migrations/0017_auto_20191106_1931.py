# Generated by Django 2.2.6 on 2019-11-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_auto_20191106_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_from_my_db',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]