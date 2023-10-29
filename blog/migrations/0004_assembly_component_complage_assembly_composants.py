# Generated by Django 4.2.6 on 2023-10-29 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_formulaire_texte'),
    ]

    operations = [
        migrations.CreateModel(
            name='assembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('fabricant', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='complage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField()),
                ('assemblage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.assembly')),
                ('composant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.component')),
            ],
            options={
                'unique_together': {('composant', 'assemblage')},
            },
        ),
        migrations.AddField(
            model_name='assembly',
            name='composants',
            field=models.ManyToManyField(through='blog.complage', to='blog.component'),
        ),
    ]
