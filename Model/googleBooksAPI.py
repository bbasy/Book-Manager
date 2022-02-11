import requests
from Model import config

class booksAPI():
    def search(self, query, type):
        self.params = {"q":query, 'key':config.api_key}
        self.url = "https://www.googleapis.com/books/v1/volumes"
        self.response = requests.get(self.url, params=self.params)
        self.data = response.json()
        return(self.data["items"][0]["volumeInfo"][type])

    def searchISBN(self, query):
        self.params = {"q":query, 'key':config.api_key}
        self.url = "https://www.googleapis.com/books/v1/volumes"
        self.response = requests.get(self.url, params=self.params)
        self.data = self.response.json()
        return(self.data["items"][0]["volumeInfo"]["industryIdentifiers"][0]["identifier"])

# bk = booksAPI()
# bk.searchISBN("Madness & Civilization")
