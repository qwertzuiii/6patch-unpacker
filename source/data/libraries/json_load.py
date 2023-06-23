import json

def get_json_data(file):
    """#### Returns json data in form of a dictionary (FILE)"""

    with open(file, 'r') as jsf:
        content = jsf.read()
    
    return json.loads(content)