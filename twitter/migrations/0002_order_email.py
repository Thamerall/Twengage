# Generated by Django 2.1.1 on 2018-09-07 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Contact Email'),
        ),
    ]
