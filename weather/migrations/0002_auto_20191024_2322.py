# Generated by Django 2.2.6 on 2019-10-24 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.IntegerField(db_index=True, primary_key=True, serialize=False),
        ),
    ]
