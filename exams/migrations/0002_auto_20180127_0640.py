# Generated by Django 2.0.1 on 2018-01-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='response_field',
            field=models.TextField(blank=True, default='ABC', max_length=20, null=True),
        ),
    ]