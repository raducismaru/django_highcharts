# Migration that populates raw_data table from
# video_games_sales.csv(available in main path of application)
import os
from django.db import migrations

from app.heplers import DataReader
from app.settings import BASE_DIR


def load_table(apps, schema_editor):
    file_path = os.path.join(BASE_DIR, 'video_game_sales.csv')
    conf = {'rank': int,
            'year': int}
    Videogames = apps.get_model('raw_data', 'Videogames')
    reader = DataReader(file_path, conf=conf)
    reader.load_table(Videogames)


class Migration(migrations.Migration):

    dependencies = [
        ('raw_data', '0001_initial'),
    ]

    operations = [migrations.RunPython(load_table),
    ]
