import pandas as pd
import argparse
import datetime
from tqdm import trange

def get_args():
    parser = argparse.ArgumentParser(description='Data Preprocessing')
    parser.add_argument('--weather_data', type=str, default='data/weather_features.csv')
    parser.add_argument('--energy_data', type=str, default='data/energy_dataset.csv')
    parser.add_argument(
        '--target_column', 
        type=str, 
        help='Target column name in energy data', 
        default='generation fossil brown coal/lignite'
    )
    parser.add_argument('--output', type=str, default='data/merged.csv', help='Output file path')
    return parser.parse_args()

def weather_preprocess(weather_data):
    weather_data = weather_data.drop(['weather_icon', 'weather_main','weather_description'], axis=1)
    return weather_data

def energy_preprocess(energy_data):
    # replace nan by mean for every column
    for column in energy_data.columns[1:]:
        energy_data[column] = energy_data[column].fillna(energy_data[column].mean())
        
    return energy_data

def merge_data(weather_data, energy_data, args):
    data = pd.DataFrame(columns=['time'] + weather_data.columns[2:].to_list() + ['target'])

    for i in trange(len(energy_data)):
        time = energy_data.iloc[i]['time']
        weather_row = weather_data[weather_data['dt_iso'] == time]
        
        weather_row = weather_row.drop(['dt_iso', 'city_name'], axis=1).mean()

        time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S%z') - \
            datetime.datetime.strptime('2015-01-01 00:00:00+01:00', '%Y-%m-%d %H:%M:%S%z')

        data.loc[i] = [time.total_seconds()] + weather_row.to_list() + [energy_data.iloc[i][args.target_column]]
        
    return data

def main():
    args = get_args()
    
    weather_data = pd.read_csv(args.weather_data)
    energy_data = pd.read_csv(args.energy_data)

    weather_data = weather_preprocess(weather_data)
    energy_data = energy_preprocess(energy_data)

    data = merge_data(weather_data, energy_data, args)

    data.to_csv(args.output, index=False)

if __name__ == '__main__':
    main()