# Generated by Django 2.2 on 2020-09-19 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Company_name', models.CharField(blank=True, max_length=200)),
                ('Contact', models.CharField(blank=True, default='N/A', max_length=20)),
                ('Profile_Image', models.ImageField(blank=True, default='https://icon-library.net/images/young-person-icon/young-person-icon-7.jpg', upload_to='Vendors_Profile_Pic/')),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=2)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200)),
                ('Profile_Image', models.ImageField(blank=True, default='https://icon-library.net/images/young-person-icon/young-person-icon-7.jpg', upload_to='Customer_Profile_Pic/')),
                ('Contact', models.CharField(blank=True, default='N/A', max_length=20)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=2)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
