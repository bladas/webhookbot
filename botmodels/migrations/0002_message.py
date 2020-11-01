# Generated by Django 3.1.2 on 2020-10-27 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('botmodels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botmodels.customer', verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Повідомлення',
                'verbose_name_plural': 'Повідомлення',
            },
        ),
    ]
