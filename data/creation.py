import requests
import os
from datetime import date
import pandas as pd


def save_datasets(path=os.getcwd(), urls={}):
    '''
        Saves csv datasets at path.

        Params:

        path(str): path where will be saved datasets

        urls(obj): Object with datasets names (key) and datasets url (value)
    '''
    print('- Saving datasets')
    for name, url in urls.items():
        try:
            request = requests.get(url)

            if request.status_code != 200:
                raise Exception('Status code != 200')
        except Exception as e:
            print('Error while saving datasets:')
            print(e)
        else:
            if not os.path.exists(dir := os.path.join(path, 'datasets')):
                os.makedirs(dir)
            with open(os.path.join(path, 'datasets', f'data-{name}-{date.today()}.csv'), mode='w+') as f:
                f.write(request.text)


def load_datasets(path=os.getcwd(), datasets={}):
    '''
        Loads csv datasets at path.

        Params:

        path(str): path where will be read datasets

        datasets(obj): Object with datasets names (keys)
    '''
    print('- Loading datasets')
    data = {}

    for name in datasets.keys():
        df = pd.read_csv(os.path.join(path, 'datasets', f'data-{name}-{date.today()}.csv'))
        data[name] = df

    return data
