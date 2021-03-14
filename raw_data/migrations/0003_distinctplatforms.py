# Creates distinct_platforms table used to store distinct platforms
# from the raw data. Used for bringing options to dropdown.
# This way, no heavy "select distinct" will be done on the raw data table.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_data', '0002_auto_20210313_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistinctPlatforms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=1000)),
            ],
        ),
    ]
