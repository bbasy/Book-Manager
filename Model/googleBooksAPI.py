import requests
from Model import config

class booksAPI():
    def search(self, query, type):
        params = {"q":query, 'key':config.api_key}
        url = "https://www.googleapis.com/books/v1/volumes"
        response = requests.get(url, params=params)
        data = response.json()
        return(data["items"][0]["volumeInfo"][type])

# bk = booksAPI()
# bk.search("9780679721109", "description")
