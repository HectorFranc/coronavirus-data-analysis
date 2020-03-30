import pandas as pd
from datetime import date, timedelta
from functools import partial, lru_cache


def dataset_dating_transform(dataset, initial_date):
    """
    Converts datasets dates columns into number (number of days since initial_date)

    Parameters
    --------
    dataset : pd.DataFrame
        Dataset that will be transformed
    initial_date : str
        Initial date for start count.
    """
    df = dataset.copy()
    df.columns = map(partial(convert_us_date_to_days_number, initial_date=initial_date), df.columns)
    return df


def drop_zero_cases(series):
    """
    Drops columns when its value is zero

    Parameters
    --------
    series : pd.Series
        Serie that will be transformed
    """
    df = series.copy()
    for column in df.columns:
        if 0 in df[column].values:
            df.drop(column, axis=1, inplace=True)
    return df


@lru_cache(maxsize=128)
def convert_us_date_to_date(us_date):
    """
    Convert date in format 'mm/dd/YYYY' to datetime.date object

    Parameters
    --------
    us_date: str
        Date that will be converted into datetime.date object
    """
    date_values = us_date.split('/')
    return date(year=int(date_values[2]), month=int(date_values[0]), day=int(date_values[1]))


@lru_cache(maxsize=128)
def convert_date_to_us_date(date_obj):
    """
    Converts datetime.date object into date string in format 'mm/dd/YYYY'

    Parameters
    --------
    date_obj: datetime.date
        date that will will be converted
    """
    return f'{date_obj.month}/{date_obj.day}/{date_obj.year}'


@lru_cache(maxsize=512)
def convert_us_date_to_days_number(date_str, initial_date):
    """
    Converts a given date in format 'mm/dd/YYYY' to the number of days since initial_date

    Parameters
    ----------
    date_str : str
        Date that will be transformed.

    initial_date : str
        Initial date for start count.
    """
    return (convert_us_date_to_date(date_str) - convert_us_date_to_date(initial_date)).days


@lru_cache(maxsize=128)
def convert_days_number_to_us_date(days_number, initial_date):
    """
    Converts the number of days since initial_date in format 'mm/dd/YYYY'

    Parameters
    ----------
    date_number : int
        The number of days since initial_date.

    initial_date : str
        Initial date for start count.
    """
    return convert_date_to_us_date(convert_us_date_to_date(initial_date) + timedelta(days=days_number))
