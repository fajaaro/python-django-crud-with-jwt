# Generated by Django 4.0.5 on 2022-06-23 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('slug', models.CharField(max_length=155, unique=True)),
                ('price', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(db_column='author_id', on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]