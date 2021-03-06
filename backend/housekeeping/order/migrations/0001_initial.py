# Generated by Django 3.0.7 on 2020-07-04 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hkman', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
                ('hours', models.FloatField()),
                ('pay_status', models.BooleanField(default=False)),
                ('score', models.FloatField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('serviceman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hkman.HKMan')),
            ],
        ),
    ]
