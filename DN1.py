import requests

def get_html(url):
    site = requests.get({url})
    return site.text

    # dodajte kodo po zgornjih navodilih
# preizkusite na primerih
page = get_html("https://example.com/")
print(page)

#page = get_html("http://example.com/neobstaja")
#print(page)
#>>> False