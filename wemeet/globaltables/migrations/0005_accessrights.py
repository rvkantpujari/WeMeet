# Generated by Django 3.0.8 on 2020-08-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globaltables', '0004_defaultrole'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accessRightCode', models.CharField(max_length=30)),
                ('accessRightDescription', models.CharField(max_length=100)),
            ],
        ),
    ]