# Generated by Django 5.1 on 2024-08-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=30)),
            ],
        ),
    ]