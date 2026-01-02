import yaml


class YamlActions:

    def __init__(self, yaml_path):
        self.yaml_path = yaml_path

    def get_yaml_value_by_key(self, config_key):
        with open(self.yaml_path) as yf:
            data = yaml.load(yf, Loader=yaml.FullLoader)
            for key, value in data.items():
                if key == config_key:
                    return value