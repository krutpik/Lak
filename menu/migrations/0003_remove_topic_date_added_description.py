# Generated by Django 4.1 on 2022-08-26 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_topic_date_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='date_added',
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.topic')),
            ],
            options={
                'verbose_name_plural': 'Descriptions',
            },
        ),
    ]
