import pandas as pd


class CoronavirusDataset:
    def __init__(self, data, name=None):
        '''
        Coronavirus Dataset model

        Params:

        data(pd.DataFrame): Dataset dataframe

        name(str, optional): Coronavirus Dataset model instance name
        '''
        self.name = name
        self.data = data

    def querie(self, province_or_state=None, country_or_region=None, days=None):
        # Get indexes for province/state and country/region conditions
        if province_or_state:
            province_or_state_indexes = self.data[self.data['Province/State'] == province_or_state].index
        if country_or_region:
            country_or_region_indexes = self.data[self.data['Country/Region'] == country_or_region].index

        # Get rows with all conditions
        if province_or_state and country_or_region:
            filtered_indexes = province_or_state_indexes.intersection(country_or_region_indexes)
        elif province_or_state or country_or_region:
            if province_or_state:
                filtered_indexes = province_or_state_indexes
            else:
                filtered_indexes = country_or_region_indexes
        else:
            filtered_indexes = self.data.index

        filtered_data = self.data.iloc[filtered_indexes]

        # Get days columns
        if days:
            try:
                filtered_data = filtered_data[days]
            except KeyError as e:
                print(f'Error. Not found all {days} columns')
                return None

        # Return None if not found data
        if len(filtered_data) == 0:
            filtered_data = None

        return filtered_data
