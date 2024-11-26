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
