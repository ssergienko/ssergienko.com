# Generated by Django 3.0.8 on 2020-07-22 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('finishedAt', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/education')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='EducationDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('document', models.FileField(blank=True, null=True, upload_to='files/')),
                ('education', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='educations.Education')),
            ],
        ),
    ]
