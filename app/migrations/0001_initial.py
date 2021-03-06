# Generated by Django 3.1.4 on 2021-01-05 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=254)),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=60)),
                ('phone', models.IntegerField()),
                ('speciality', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=60)),
                ('phone', models.IntegerField()),
                ('photo', models.ImageField(upload_to='app/uploads')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicalCenter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('medicalCenterName', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('addresse', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=60)),
                ('photo', models.ImageField(upload_to='app/uploads')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=254)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=60)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TravelAgency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('travelAgencyName', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=60)),
                ('addresse', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=60)),
                ('photo', models.ImageField(upload_to='app/uploads')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='app.hotel')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Symptoms', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous', to='app.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rendezvous', to='app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Diagnosis', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='app.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultations', to='app.patient')),
                ('rendezVous', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultation', to='app.rendezvous')),
            ],
        ),
    ]
