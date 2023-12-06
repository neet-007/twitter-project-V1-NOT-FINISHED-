# Generated by Django 4.2.8 on 2023-12-06 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0006_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]