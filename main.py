from data.creation import save_datasets, load_datasets
from data.models import CoronavirusDataset
from visualizations.graphs import plot
from transform.dating import convert_date_to_us_date, convert_days_number_to_us_date, convert_us_date_to_date, convert_us_date_to_days_number, dataset_dating_transform

URLS = {
    'confirmed': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
    'deaths': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
    'recovered': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv',
}

if __name__ == "__main__":
    # save_datasets(urls=URLS)
    data = load_datasets(datasets=URLS)

    df = CoronavirusDataset(data['confirmed'], 'confirmed')
    plot(df, ['Mexico', 'Italy', 'Colombia', 'Brazil', 'Peru', 'US', 'China', 'Spain', 'Guatemala', 'Iran'])
    df = CoronavirusDataset(data['deaths'], 'deaths')
    plot(df, ['Mexico', 'Italy', 'Colombia', 'Brazil', 'Peru', 'US', 'China', 'Spain', 'Guatemala', 'Iran'])
    df = CoronavirusDataset(data['recovered'], 'recovered')
    plot(df, ['Mexico', 'Italy', 'Colombia', 'Brazil', 'Peru', 'US', 'China', 'Spain', 'Guatemala', 'Iran'])
