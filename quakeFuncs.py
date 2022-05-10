from urllib.request import *
import ssl
from json import *
from datetime import *
from operator import *

class Earthquake:
   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self, other):
      return self.place == other.place and \
         self.mag == other.mag and \
         self.longitude == other.longitude and \
         self.latitude == other.latitude and \
         self.time == other.time

   def __str__(self):
      return "(%.2f) %40s at %s (%8.3f, %6.3f)" % (self.mag, self.place, time_to_str(self.time), self.longitude, self.latitude) 

   def __repr__(self):
      return(str(self.mag) + " " + str(self.longitude)+ " " + str(self.latitude)+ " " + str(self.time)+ " " + str(self.place))
      
def read_quakes_from_file(filename):
   inFile = open(filename, "r" )
   res = []
   for line in inFile:
      l = line.split()      
      mag = float(l[0])
      longitude = float(l[1])
      latitude = float(l[2])
      time = int(l[3])
      place = ' '.join((l[4:]))

      res.append((Earthquake(place, mag, longitude, latitude, time)))
   return res

def display_quakes(quakes):#takes a 2dlist of quakes and prints it to the screen in the correct format 
   print("Earthquakes:")
   print("------------")
   for quake in quakes:
      print(quake)

def filter_by_mag(quakes, low, high):
   print()
   quakes = [quake for quake in quakes if low <= quake.mag and high >= quake.mag]
   return quakes
     
def filter_by_place(quakes, word):
   quakes = [quake for quake in quakes if word.lower() in quake.place.lower()]
   return quakes


def quake_from_feature(f):
   return Earthquake(f["properties"]["place"], f["properties"]["mag"], f["geometry"]["coordinates"][0], f["geometry"]["coordinates"][1], (f["properties"]["time"]//1000))

def get_json(url):
   gcontext = ssl.SSLContext() 
   with urlopen(url, context=gcontext) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    

def write_to_file(quakes, file):
   outFile = open(file, "w")
   for quake in quakes:
      outFile.write("%s %s %s %s %s\n" % (quake.mag, quake.longitude, quake.latitude, quake.time, quake.place))