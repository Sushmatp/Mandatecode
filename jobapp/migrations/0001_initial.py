# Generated by Django 3.1 on 2020-08-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_ID', models.CharField(max_length=10)),
                ('Company_Name', models.CharField(max_length=30, null=True)),
                ('Job_Catagory', models.CharField(max_length=50, null=True)),
                ('Job_Sub_Catagory', models.CharField(max_length=50, null=True)),
                ('HR_Name', models.CharField(max_length=30, null=True)),
                ('Job_Description', models.CharField(max_length=3000, null=True)),
                ('Skills_required', models.CharField(max_length=100, null=True)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
                ('No_of_openings', models.IntegerField()),
                ('Job_Location', models.CharField(max_length=30, null=True)),
                ('Job_Title', models.CharField(max_length=50, null=True)),
                ('CTC', models.IntegerField()),
                ('Min_Exp', models.IntegerField()),
                ('Max_Exp', models.IntegerField()),
                ('Company_ID', models.CharField(max_length=10)),
                ('Lkup_data01', models.IntegerField()),
                ('Job_Cate', models.IntegerField()),
                ('Job_Sub_Cate', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Job_Details',
                'verbose_name_plural': 'Job_Detailss',
            },
        ),
    ]
