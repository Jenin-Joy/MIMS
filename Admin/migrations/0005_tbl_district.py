# Generated by Django 5.1 on 2024-08-21 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_tbl_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_state')),
            ],
        ),
    ]