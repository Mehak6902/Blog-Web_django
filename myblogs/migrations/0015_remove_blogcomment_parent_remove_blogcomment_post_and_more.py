# Generated by Django 5.0.1 on 2024-02-04 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblogs', '0014_post_blogcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]
