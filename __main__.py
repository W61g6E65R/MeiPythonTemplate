# General imports
import logging
import dotenv
import os


# Local imports
import modules.globalConstants

# Config logging
logging.basicConfig(format=modules.globalConstants.LOGGING_CONFIG_FORMAT, level=logging.INFO)

# DEBUGGING
# When debugging locally ensure to load the enviromental variables from .env with dotenv.load_dotenv().
# In productive mode this should be done by docker and the line must be commented!

# dotenv.load_dotenv()

m_var1= os.environ['ENV_VAR_NAME']
m_var2 = os.environ['ENV_VAR2_NAME']