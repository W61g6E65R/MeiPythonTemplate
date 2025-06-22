# import.global
import pytest

# import.local
from module_config.class_configLoader import ConfigLoader

# FAILURE
def test_read_config_folder_failure():
    with pytest.raises(FileNotFoundError):
        ConfigLoader("C:\\fake.folder")

# SUCCESS
def test_read_config_folder_success():
    loader = ConfigLoader(".\\config\\global.d")
    assert len(loader.conf_objects) > 0

def test_read_config_parameter_success():
    loader = ConfigLoader(".\\config\\global.d")
    para = loader.conf_objects["global.yaml"]["version"]
    assert para > 0