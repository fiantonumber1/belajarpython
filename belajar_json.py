import json
import os

cwd = os.getcwd()
json_file_path = "{}/sample3.json".format(cwd)

with open(json_file_path, encoding='utf-8', errors='ignore') as json_data:
     contents = json.load(json_data, strict=False)


a_file = open("sample.json", "r")
a_json = json.load(a_file)
pretty_json = json.dumps(a_json, indent=4)
a_file.close()

print(pretty_json)
print(contents)