# Initial migration to create raw_data table

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videogames',
            fields=[
                ('rank', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('platform', models.CharField(max_length=1000)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=1000)),
                ('publisher', models.CharField(max_length=1000)),
                ('na_sales', models.FloatField()),
                ('eu_sales', models.FloatField()),
                ('jp_sales', models.FloatField()),
                ('other_sales', models.FloatField()),
                ('global_sales', models.FloatField()),
            ],
        ),
    ]
