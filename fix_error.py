import sys
from ruamel.yaml import YAML

returnValue = [{'utter_What is Bansoori?': [{'text': 'Bansoori is an Indian classical instrument.'}]}, {'utter_What does Akhil play?': [{'text': 'Akhil plays Bansoori and Guitar.'}]}, {'utter_What is Puliyogare?': [{'text': 'Puliyogare is a South Indian dish made of rice and tamarind.'}]}]
toPrintYaml = dict()
for element in returnValue:
    for key, value in element.items():
      toPrintYaml[key] = value

eval = dict({'responses':{'utter_What is Bansoori?': [{'text': 'Bansoori is an Indian classical instrument.'}], 'utter_What does Akhil play?': [{'text': 'Akhil plays Bansoori and Guitar.'}]}})
eval = dict({'responses':toPrintYaml})

d = dict(a=dict(b=[{3:"text"}, {4:"nuevo"}]),c=[{3:"text"}, {4:"nuevo"}])
data = {1: {1: [{1: 1, 2: 2}, {1: 1, 2: 2}], 2: 2}, 2: 42}
# 1:
#   1:
#   - 1: 1
#     2: 2
#   - 1: 1
#     2: 2
#   2: 2
# 2: 42
# ---
# 1:
#   1:
#     - 1: 1
#       2: 2
#     - 1: 1
#       2: 2
#   2: 2
# 2: 42
# ---
# 1:
#   1:
#     - 1: 1
#       2: 2
#     - 1: 1
#       2: 2
#   2: 2
# 2: 42
#d = dict(a=dict(b=[{3:"text"}, {4:"nuevo"}]),c=[{3:"text"}, {4:"nuevo"}])
yaml = YAML()
yaml.explicit_start = True
yaml.dump(d, sys.stdout)
print('0123456789')
yaml = YAML()
yaml.indent(mapping=4, sequence=6, offset=3)
yaml.dump(eval, sys.stdout)
print('0123456789')