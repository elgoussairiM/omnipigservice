# Generated by Django 4.0.1 on 2022-03-24 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='filetest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(default='meriem.jpg', upload_to='donn')),
                ('label', models.CharField(default='True', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pedigree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedigreeId', models.IntegerField()),
                ('generation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pigeon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pigeonId', models.IntegerField()),
                ('pigeonName', models.CharField(max_length=100)),
                ('numeroSerie', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('mere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pigeonMere', to='omni.pigeon')),
                ('pedigree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedigree', to='omni.pedigree')),
                ('pere', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pigeonPere', to='omni.pigeon')),
            ],
        ),
        migrations.CreateModel(
            name='PedigreeNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noeudId', models.IntegerField()),
                ('nodeKey', models.CharField(max_length=100)),
                ('noeudParent', models.CharField(max_length=100)),
                ('pedigree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedigreeNodes', to='omni.pedigree')),
                ('pigeon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pigeon', to='omni.pigeon')),
            ],
        ),
    ]
