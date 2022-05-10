from quakeFuncs import *
low = 0.5
high = 3
quakes = [[0.98, -122.7574997, 38.7970009, 1488186233, '2km N of The Geysers, California'], [3, -124.3346634, 40.3071671, 1488184278, '28km SW of Rio Dell, California'], [2.58, -124.934166, 40.348999, 1488251092, '62km WSW of Ferndale, California'], [4.5, -157.822, 55.2888, 1488211648, '122km SSE of Chignik Lake, Alaska']]


def filter_by_mag(quakes, low, high):
   res = []
   for i in range(len(quakes)):
      if low <= quakes[i][0] <= high:
         res.append(quakes[i])
   return res

display_quakes(filter_by_mag(quakes, low, high))

