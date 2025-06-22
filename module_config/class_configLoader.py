# import.general
import os
import yaml
import logging

""" Class to import all .yaml files in given directory.
        Will generate yaml objects named with the filename
"""
class ConfigLoader:
    """_summary_
    """    
    def __init__(self, directory):
        self.log = logging.getLogger(__name__)
        self.directory = directory
        
        __dirExists = os.path.exists(directory)
        if not os.path.exists(self.directory):
            raise FileNotFoundError(f"Path not found: {self.directory}")
        self.conf_objects = self._load_yaml_files()
        
    """_summary_
    """    
    def _load_yaml_files(self):
        conf_objects = {}
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith(('.yaml', '.yml')):
                    full_path = os.path.join(root, file)
                    with open(full_path, 'r', encoding='utf-8') as f:
                        try:
                            data = yaml.safe_load(f)
                            conf_objects[file] = data
                        except yaml.YAMLError as e:
                            print(f"Error while reading {full_path}: {e}")
        return conf_objects
