import json
import requests
import csv

data=requests.get('https://jsonplaceholder.typicode.com/users')
todos = json.loads(data.text)  

for todo in todos:
    print(f"Name: {todo['name']}, \nCity: {todo['address']['city']}, \nGPS coordinates in form of (LAT, LNG): \n{todo['address']['geo']['lat']}, \n{todo['address']['geo']['lng']}\n Company Name: {todo['company']['name']}\n ")           

with open('users.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'City', 'Latitude', 'Longitude', 'Company Name'])

    for todo in todos:
            Name = todo['name']
            City = todo['address']['city']
            lat = todo['address']['geo']['lat']
            lng = todo['address']['geo']['lng']
            geo =f"({lat}, {lng})"
            Company_Name = todo['company']['name']
            writer.writerow([Name, City, geo, Company_Name])
