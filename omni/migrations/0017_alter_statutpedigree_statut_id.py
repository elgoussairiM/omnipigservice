# Generated by Django 4.0.1 on 2022-04-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omni', '0016_alter_pedigree_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statutpedigree',
            name='statut_id',
            field=models.CharField(default='1', max_length=100),
        ),
    ]
