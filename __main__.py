# import.general
import os
import yaml
import logging
import logging.config
from dotenv import load_dotenv
import argparse

# import.project

# import.local
from module_config.class_configLoader import ConfigLoader

# import.local.config

from config.project.logging import get_config as confLoader_logging



# <CONST>
CONST_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONST_CONFIG_FOLDER_GLOBAL = os.path.join(CONST_ROOT_DIR, ".\\config\\project")
# </CONST>

# <CONFIG>
globalConfig = ConfigLoader(CONST_CONFIG_FOLDER_GLOBAL)

# </CONFIG>

# <LOGGING>
logging.config.dictConfig((confLoader_logging(".\\config\\project\\logging.yaml")))
log = logging.getLogger(__name__)
# </LOGGING>

# <ARGPARSE>
parser = argparse.ArgumentParser()
parser_subparser = parser.add_subparsers(dest="command", required=True)

parser_m_database = parser_subparser.add_parser("database", help="Database Connector")
parser_m_database.add_argument("--testConnection", type=str, help="Connect to different database")

parser_m_httpRequests = parser_subparser.add_parser("httpRequests", help="Test http connection")
parser_m_httpRequests.add_argument("--show", help="show parameters")


args = parser.parse_args()
# </ARGPARSE>


# <PROG>
# <module_api>
from fastapi import FastAPI
from module_api import include_all_routers # import from __init__.py
import module_api.routes
import uvicorn

app_api = FastAPI()
module_api.include_all_routers(app_api, package_name="module_api", package_path=str(module_api.routes.__path__))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app_api, host="0.0.0.0", port=8000)
# </module_api>

# <module_database>
#from module_database.class_databaseConnector import DatabaseConnector

#database = DatabaseConnector()

# </module_database>

# </PROG>