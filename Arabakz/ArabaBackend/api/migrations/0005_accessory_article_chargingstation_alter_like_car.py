from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_like_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ChargingStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('charging_time', models.DurationField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='like',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='api.car'),
        ),
    ]
