

import yaml
from yaml.loader import SafeLoader

 
print("Entre la direccion del archivo .yaml:")
with open(input(), 'r') as f:
    data = yaml.load(f, Loader=SafeLoader)
    print(data)