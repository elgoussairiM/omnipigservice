# Generated by Django 4.0.1 on 2022-03-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omni', '0009_remove_pedigreenode_pigeon_pigeon_pedigreenode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedigreenode',
            name='noeudId',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
