from data.creation import save_datasets, load_datasets
from data.models import CoronavirusDataset
from transform.pipelines import convert_dataset_dates_first_cases_date
import matplotlib.pyplot as plt

URLS = {
    'confirmed': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
    'deaths': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
    'recovered': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv',
}

if __name__ == "__main__":
    # save_datasets(urls=URLS)
    data = load_datasets(datasets=URLS)

    df = CoronavirusDataset(data['confirmed'], 'confirmed')

    droped_columns = ['Province/State', 'Country/Region', 'Lat', 'Long']
    for country in ['Mexico', 'Italy', 'Colombia', 'Brazil', 'Peru']:
        country_df = df.querie(country_or_region=country)
        country_df = country_df.drop(droped_columns, axis=1).sum().to_frame().transpose()
        country_df, country_init_date = convert_dataset_dates_first_cases_date(country_df, droped_columns=[])

        plt.plot(country_df.columns, country_df.to_numpy().reshape(-1), label=country)
    plt.legend()
    plt.show()
