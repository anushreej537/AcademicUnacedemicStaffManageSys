# Generated by Django 4.1.2 on 2023-11-09 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=250)),
                ('is_classteacher', models.BooleanField(default=True)),
                ('is_academic', models.BooleanField(default=True)),
                ('is_nonacademic', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usertype', models.CharField(max_length=250)),
                ('names', models.CharField(max_length=250)),
                ('contact', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(max_length=250)),
                ('education', models.CharField(blank=True, max_length=250, null=True)),
                ('joiningdate', models.DateField(blank=True, null=True)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('password', models.CharField(max_length=250)),
                ('profileimg', models.ImageField(blank=True, null=True, upload_to='pic')),
                ('designation_master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stu_app.designation')),
            ],
        ),
    ]
