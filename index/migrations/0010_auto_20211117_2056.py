# Generated by Django 3.2.7 on 2021-11-17 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20211014_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='images',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='vedios',
        ),
        migrations.AddField(
            model_name='complaint',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='data/images<django.db.models.fields.AutoField>'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='vedio',
            field=models.FileField(default='', null=True, upload_to='data/vedios<django.db.models.fields.AutoField>'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='idprooof',
            field=models.FileField(default='', null=True, upload_to='data/id/<django.db.models.fields.AutoField>'),
        ),
    ]
