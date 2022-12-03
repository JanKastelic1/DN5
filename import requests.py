import requests

def get_html(url):

    # dodajte kodo po zgornjih navodilih
# preizkusite na primerih
page = get_html("https://example.com/")
print(page)
>>> <!doctype html>
>>> <html>
>>> <head>
>>>     <title>Example Domain</title>
...
page = get_html("http://example.com/neobstaja")
print(page)
>>> False