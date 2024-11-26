import configparser
from pathlib import Path

def get_train_carriages_info_by_number(number):
    project_root = Path(__file__).parent.resolve()
    config_file_path = project_root / f'config/Train{number}.ini'
    config = configparser.ConfigParser()
    config.read(config_file_path)

    return {
        'CountCarriages': dict(config['CountCarriages']),
        'CountSeatCarriages': dict(config['CountSeatCarriages']),
        'PriceCarriages': dict(config['PriceCarriages'])
        }


def get_route_info_by_number(number):
    project_root = Path(__file__).parent.resolve()
    config_file_path = project_root / 'config/Route.ini'
    config = configparser.ConfigParser()
    config.read(config_file_path)

    stations = config['Route'][str(number)].split('-')
    trains = {}
    for train_num, route_num in config['Train'].items():
        if route_num == str(number):
            trains[train_num] = config['Shedule'][train_num].split(';')
    return {
        'stations': stations,
        'trains': trains
        }


def get_routes():
    project_root = Path(__file__).parent.resolve()
    config_file_path = project_root / 'config/Route.ini'
    config = configparser.ConfigParser()
    config.read(config_file_path)

    return config['Route'].keys()