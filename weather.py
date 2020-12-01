 

from tkinter import font
import tkinter as tk 
import requests


HEIGHT = 700
WIDTH = 800
def test_function(entry):
	print("hana" , entry )
root = tk.Tk()
#2953033522972ed52739214dde311fb3
#api.openweathermap.org/data/2.5/weather?q

def get_weather(city):	 
	weather_key = '2953033522972ed52739214dde311fb3'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID' : weather_key , 'q' :  city, 'units' : 'Metric'  }
	response = requests.get(url,params = params)
	weather = response.json()
	label['text'] = format_response(weather)	
def format_response(weather):
	try:
	 name = weather['name']  
	 desc= weather['weather'][0]['description']
	 temp= weather['main']['temp']
	 final_str = str(name) + '\n' + str(desc) +'\n'+ str(temp)
	except:
		final_str = 'there was a problem '

	return final_str


 




canvas = tk.Canvas(root , height = HEIGHT , width = WIDTH  )
canvas.pack()

background_image = tk.PhotoImage(file='/home/oussa/Desktop/1.png')
background_label = tk.Label(root , image=background_image)
background_label.place(relwidth = 1 , relheight=1)

frame = tk.Frame(root , bg = '#009e9e' , bd = 5 )
frame.place(relx = 0.5  , rely = 0.1,   relwidth=0.75 , relheight=0.1 , anchor = 'n' )

entry = tk.Entry(frame , font = ('courier',12) )
entry.place(  relwidth = 0.65 , relheight = 1)


button = tk.Button(frame, text="Get Weather"    ,font = ('courier',12) , command = lambda : get_weather(entry.get())  )
button.place(relx = 0.7   , relwidth = 0.3 , relheight = 1   )
 
lower_frame = tk.Frame(root , bg = '#80c1ff' , bd = 10 )
lower_frame.place(relx = 0.5 , rely = 0.25  , relwidth = 0.75 , relheight  = 0.6  ,anchor = 'n' ) 

label = tk.Label(lower_frame  ,font = ('courier',18) , anchor = 'nw' , justify = 'left' )
label.place(  relwidth = 1  , relheight = 1) 
 

root.mainloop()  