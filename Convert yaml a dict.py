

import yaml
from yaml.loader import SafeLoader

  # such output is not valid YAML!
# Open the file and load the file
print("Entre la direccion del archivo:")
with open(input(), 'r') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)