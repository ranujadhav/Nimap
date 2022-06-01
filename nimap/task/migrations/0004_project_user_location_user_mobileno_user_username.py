# Generated by Django 4.0.4 on 2022-05-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_remove_client_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=100)),
                ('projectdiscription', models.CharField(max_length=100)),
                ('projecttechnology', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='mobileno',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
