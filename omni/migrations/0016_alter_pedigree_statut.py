# Generated by Django 4.0.1 on 2022-04-05 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('omni', '0015_statutpedigree_delete_filetest_pedigree_statut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedigree',
            name='statut',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedigree', to='omni.statutpedigree'),
        ),
    ]