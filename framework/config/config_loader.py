import yaml


class ConfigLoader:

    def __init__(self, path):

        self.path = path

    def load(self):

        with open(self.path) as file:

            return yaml.safe_load(file)