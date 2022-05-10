from quakeFuncs import *
def sort_by_mag(filename):
   qlist = read_quakes_from_file(filename)
   quakes= []
   for i in range(len(qlist)):
      quakes.append(Earthquake(qlist[i][4], qlist[i][0], qlist[i][1], qlist[i][2], time_to_str(qlist[i][3])))

   quakes.sort(key=attrgetter('mag'), reverse = True)
   print(quakes)



display_quakes(sort_by_mag("test0.txt"))

