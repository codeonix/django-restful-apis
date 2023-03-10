# Generated by Django 4.1.6 on 2023-02-09 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('share_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('investment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waitListApp.category')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waitListApp.stock')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='waitListApp.stock'),
        ),
    ]
