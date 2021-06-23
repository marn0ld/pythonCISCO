import http.client
import json
from tkinter import *
import tk as tk

root = Tk()
root.title("Arno's covid-tracker")

#defining refresh button
def refresh():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
    res = conn.getresponse()
    data = res.read()
    conv_str = data.decode("utf-8")  #making a list of dicts into dicts
    json = json.loads(conv_str)  #loading the result into json format
    for i in range(10):
        text.insert('1.0', '-' * 25)
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[14])
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[12])
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[10])
        text.insert('1.0', '\n')
        text.insert('1.0', list(json[i].items())[2])
        text.insert('1.0', '\n')

refresh_button = Button(root, text="REFRESH", command= refresh)
refresh_button.pack(pady=20)
text = Text(width=500, height=500)
text.pack()
conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

conn.request("GET", "/api/npm-covid-data/europe", headers=headers)

res = conn.getresponse()
data = res.read()
conv_str = data.decode("utf-8") #making a list of dictionaries into an dictionary
json = json.loads(conv_str) #loading the result into json format

# in range you can change the dimension of countries
for i in range(10):
    text.insert('1.0', '\n')
    text.insert('1.0', '-' * 25)
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[14])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[12])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[10])
    text.insert('1.0', '\n')
    text.insert('1.0', list(json[i].items())[2])

root.mainloop()

