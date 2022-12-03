import requests
import json

def get_api_data(url):
    site = requests.get(url)
    koda = site.status_code
    js = json.dumps(site.text)
    diction = json.loads(js)
    if koda != 200:
        return False
    else:
        return diction

    # dodajte kodo po zgornjih navodilih
# preizkusite na primerih
data = get_api_data("https://jsonplaceholder.typicode.com/todos/1")
print(data)
#>>> {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
data = get_api_data("https://jsonplaceholder.typicode.com/nedala/nedala")
print(data)
#>>> False