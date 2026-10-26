import yaml


def load_config(path):
    f = open(path)
    data = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return data
