from configparser import ConfigParser
from pathlib import PurePath

config = ConfigParser()
config.read(PurePath(__file__).parent/'config.ini')