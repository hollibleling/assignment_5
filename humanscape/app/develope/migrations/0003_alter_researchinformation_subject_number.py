# Generated by Django 3.2.9 on 2021-11-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('develope', '0002_alter_researchinformation_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchinformation',
            name='subject_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]