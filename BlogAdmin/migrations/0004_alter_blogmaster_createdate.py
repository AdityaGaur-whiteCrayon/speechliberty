# Generated by Django 3.2.5 on 2021-08-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAdmin', '0003_auto_20210818_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmaster',
            name='createdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]