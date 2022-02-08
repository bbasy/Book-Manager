import requests
import config

class booksAPI():
    def search(self, query):
        params = {"q":query, 'key':config.api_key}
        url = "https://www.googleapis.com/books/v1/volumes"
        response = requests.get(url, params=params)
        data = response.json()
        print(data["items"][0]["volumeInfo"]["title"])

bk = booksAPI()
bk.search("9780679721109")
