import yaml


def load_yaml(path):
    with open(path, "r") as p:
        file = yaml.safe_load(p)
    return file


if __name__ == "__main__":
    print(load_yaml("param.yaml")["url"])


# import yaml
#
# def load_yaml(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             data = yaml.safe_load(file)
#             return data
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")
#         return None
#     except yaml.YAMLError as e:
#         print(f"Error while parsing YAML file '{file_path}': {e}")
#         return None