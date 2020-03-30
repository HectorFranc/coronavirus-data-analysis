from transform.dating import drop_zero_cases, dataset_dating_transform


def convert_dataset_dates_first_cases_date(dataset, droped_columns=['Province/State', 'Country/Region', 'Lat', 'Long']):
    df = dataset.copy()

    df_no_dates = df[droped_columns]
    df_dates = df.drop(droped_columns, axis=1)

    df_dates = drop_zero_cases(df_dates)
    initial_date = df_dates.columns[0]
    df_dates = dataset_dating_transform(df_dates, initial_date=initial_date)

    return (df_no_dates.join(df_dates), initial_date)
