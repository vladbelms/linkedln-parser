
import os
import tomllib

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
SOURCE_PATH = os.path.join(PROJECT_PATH, 'linkedln_parser')
CONFIG_PATH = os.path.join(PROJECT_PATH, "config.toml")
TESTS_PATH = os.path.join(PROJECT_PATH, 'tests')

LOGS_PATH = os.path.join(PROJECT_PATH, "logs")
with open(CONFIG_PATH, 'r') as config:
    content = config.read()
    CONFIG = tomllib.loads(content)
