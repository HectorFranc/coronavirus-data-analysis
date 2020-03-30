from transform.pipelines import convert_dataset_dates_first_cases_date
import matplotlib.pyplot as plt


def plot(df, countries):
    droped_columns = ['Province/State', 'Country/Region', 'Lat', 'Long']
    for country in countries:
        country_df = df.querie(country_or_region=country)
        country_df = country_df.drop(droped_columns, axis=1).sum().to_frame().transpose()
        country_df, country_init_date = convert_dataset_dates_first_cases_date(country_df, droped_columns=[])

        plt.plot(country_df.columns, country_df.to_numpy().reshape(-1), label=country)
    plt.legend()
    plt.show()
