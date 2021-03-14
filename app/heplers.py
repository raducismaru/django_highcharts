import pandas as pd


from django.db import models


class DataReader():
    """
    Class for opening a file with pandas.
    Has method load_table for loading the dataframe into a table
    """
    def __init__(self, file_path, read_method='read_csv', conf=None):
        """
        :param file_path: file path
        :param read_method: read method (should be one of the many methods pandas has for reading files
                - example: read_csv(default), read_json, read_excel etc)
        :param conf: optional - if provided it represents a mapping of column-datatype pairs :
                     used for casting specific columns to the required type in the database.
        """
        self.reader = getattr(pd, read_method)(file_path)
        self.reader = self.reader[self.reader['year'].notna()]
        if conf:
            for column in conf:
                self.reader[column] = self.reader[column].astype(conf.get(column))

    def load_table(self, model):
        """
        :param model: table model
        checks if the model provided inherits from models.Model and if so
        loads the table in bulk mode using the pandas dataframe attr self.reader
        passing each row of the dataframe as kwargs.
        """
        if not issubclass(model, models.Model):
            raise Exception('Model object not provided')
        model.objects.bulk_create(model(**values) for values in self.reader.to_dict('records'))

