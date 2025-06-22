# import.global
import pytest
import os
from dotenv import load_dotenv, dotenv_values

# import.project
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

# import.local
from module_database.class_databaseConnector import DatabaseConnector
from module_config.class_configLoader import ConfigLoader

# <CONST>
CONST_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONST_CONFIG_FOLDER_GLOBAL = os.path.join(CONST_ROOT_DIR, "..\\config\\global.d")
# <CONST>

# <CONFIG>
globalConfig = ConfigLoader(CONST_CONFIG_FOLDER_GLOBAL)
load_dotenv(globalConfig.conf_objects["global.yaml"]["credentials"]) # Load Credentials
# </CONFIG>

# FAILURE

def test_postgres_Connection_failure():
   
    with pytest.raises(ConnectionError) as e_info:
        dbObject = DatabaseConnector("postgresql", os.getenv("DB_GRAFANA_READER_USER"), os.getenv("DB_GRAFANA_READER_PASSWORD"), '999.999.999.999', '5432', 'dms')


# SUCCESS

def test_postgres_Connection_success():
    dbObject = DatabaseConnector("postgresql", os.getenv("DB_GRAFANA_READER_USER"), os.getenv("DB_GRAFANA_READER_PASSWORD"), '10.17.33.15', '5432', 'dms')
    rows = dbObject.execute_raw("SELECT * FROM administration.enaio_server_information")
    assert len(rows)> 0