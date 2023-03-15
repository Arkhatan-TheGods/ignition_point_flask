from yaml import load
from yaml.loader import SafeLoader
from os import path

def get_config(path_settings: str | None = None) -> dict:

    def check_file(file: str) -> str:
        if path.exists(file):
            return file
        else:
            raise Exception(f"Arquivo {file} não localizado")

    path_settings = check_file(path.abspath('settings.yaml')) \
        if path_settings is None else check_file(path_settings)

    with open(path_settings, 'r') as file:
        return load(file, Loader=SafeLoader)
