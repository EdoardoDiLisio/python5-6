import flask

api_url = "https://jsonplaceholder.typicode.com/todos/5"
response = requests.get(api_url)
print(response.json())