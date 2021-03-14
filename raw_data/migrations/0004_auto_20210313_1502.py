# Populates distinct_platfroms table with data from raw data table.

from django.db import migrations


def load_distinct_platforms(apps, schema_editor):
    videogames = apps.get_model('raw_data', 'Videogames')
    distinct_platforms_model = apps.get_model('raw_data', 'DistinctPlatforms')
    distinct_platfroms = videogames.objects.values('platform').distinct()
    distinct_platforms_model.objects.bulk_create(distinct_platforms_model(**values) for values in distinct_platfroms)

class Migration(migrations.Migration):

    dependencies = [
        ('raw_data', '0001_initial'),
        ('raw_data', '0002_auto_20210313_1348'),
        ('raw_data', '0003_distinctplatforms'),
    ]

    operations = [migrations.RunPython(load_distinct_platforms),
    ]
