# Generated by Django 5.1 on 2024-08-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_alter_tbl_chat_chat_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_chat',
            name='chat_content',
            field=models.BinaryField(max_length=10000),
        ),
    ]
