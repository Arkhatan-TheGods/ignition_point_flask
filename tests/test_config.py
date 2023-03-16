from os import system, getcwd
from pytest import fixture, mark, raises
# from typing import Iterable
from main.config import get_config


@fixture
def setup():

    file_yaml = "settings_test.yaml"
    root = getcwd()

    system(f"cd {root} && echo file_db: {root}/store.db > {file_yaml}")

    yield file_yaml

    system(f"cd {root} && rm -r {file_yaml}")


@mark.parametrize("path_settings", ["dev_test.yaml"])
def test_check_file_settings_exists_fail(path_settings: str):

    with raises(Exception) as ex_info:
        get_config(path_settings)

    assert ex_info.value.args[0] == f"Arquivo {path_settings} não localizado"


@mark.parametrize("expected_parameter", ["parameter_teste"])
def test_check_parameter_exists_fail(setup: str, expected_parameter: str):

    config = get_config(setup)

    assert config.get(expected_parameter) is None


def test_check_file_settings(setup: str):

    # Act
    config = get_config(setup)

    # Assert
    assert config.get('file_db')


@mark.parametrize("expected_parameter", ["file_db"])
def test_check_parameter_exists(setup: str, expected_parameter: str):

    config = get_config(setup)

    assert config.get(expected_parameter)
