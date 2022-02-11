import requests
import config

class booksAPI():
    def search(self, query, type):
        params = {"q":query, 'key':config.api_key}
        url = "https://www.googleapis.com/books/v1/volumes"
        response = requests.get(url, params=params)
        data = response.json()
        return(data["items"][0]["volumeInfo"][type])

    def searchISBN(self, query):
        params = {"q":query, 'key':config.api_key}
        url = "https://www.googleapis.com/books/v1/volumes"
        response = requests.get(url, params=params)
        data = response.json()
        print(data["items"][0]["volumeInfo"]["industryIdentifiers"][0]["identifier"])

# bk = booksAPI()
# bk.searchISBN("It Stephen King")
