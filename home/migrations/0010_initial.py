# Generated by Django 5.0 on 2024-05-04 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0009_delete_category_remove_userprofile_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nomi')),
                ('type', models.CharField(choices=[('dona', 'Dona'), ('metr', 'Metr')], max_length=255, verbose_name='Birlik')),
                ('amount', models.IntegerField(verbose_name='Soni')),
                ('summa', models.IntegerField(verbose_name='Narxi Sum')),
                ('dollor', models.FloatField(verbose_name='Narxi $')),
                ('category', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='home.category', verbose_name='Kategoriya')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('sotuvchi', 'Sotuvchi'), ('admin', 'Admin'), ('boshliq', 'Boshliq')], max_length=255)),
                ('rating', models.FloatField()),
                ('phone_nomber', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'userprofile',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_price', models.FloatField()),
                ('time', models.DateField(auto_now=True)),
                ('p_amount', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userprofile')),
            ],
            options={
                'db_table': 'income',
            },
        ),
    ]
