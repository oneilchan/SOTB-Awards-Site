# Generated by Django 4.0.4 on 2022-06-27 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(max_length=100)),
                ('votes', models.IntegerField(default=0)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.award')),
            ],
        ),
    ]
