# Generated by Django 3.2.2 on 2021-05-14 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90, verbose_name='Name')),
                ('slug', models.SlugField(max_length=90, verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ismi')),
                ('email', models.EmailField(max_length=200, verbose_name='Emaili')),
                ('subject', models.TextField(max_length=150, verbose_name='subject')),
                ('message', models.CharField(max_length=50, verbose_name='Xabari')),
            ],
            options={
                'verbose_name': 'Aloqa',
                'verbose_name_plural': 'Aloqalar',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='*')),
                ('developer', models.CharField(max_length=100, verbose_name='Developers')),
                ('year', models.DateField(verbose_name='Year')),
                ('budget', models.PositiveIntegerField(default=0, verbose_name='Budget')),
                ('platform', models.CharField(max_length=100, verbose_name='Platform')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='game.category')),
            ],
            options={
                'verbose_name_plural': 'Games',
            },
        ),
    ]