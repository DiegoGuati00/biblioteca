# Generated by Django 3.2 on 2022-05-26 21:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'PENDIENTE'), ('a', 'RECLAMAR'), ('r', 'RECLAMADO'), ('d', 'DEVUELTO')], max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rented',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateget', models.DateTimeField(auto_now_add=True)),
                ('dateIn', models.DateTimeField(auto_now=True)),
                ('state', models.BooleanField(default=False)),
                ('bookItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.bookitem')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.rent')),
            ],
        ),
    ]