import requests

def fox():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)  # Заменяем request на requests
    if response.status_code == 200:
        data = response.json()  # Метод json() для получения данных из ответа
        return data.get('image')
   

if __name__ == "__main__":
    fox()
