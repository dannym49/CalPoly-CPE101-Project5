from quakeFuncs import *

def main():
   quakes = read_quakes_from_file("quakes.txt")
   display_quakes(quakes)
   
   userinput = input("\nOptions:\n %7s \n %9s \n %13s \n %7s \n\nChoice: " % ('(s)ort', '(f)ilter', '(n)ew quakes', '(q)uit'))
   while userinput != 'q' and userinput != 'Q':
      if userinput == 's' or userinput == 'S':
         sort = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
         if sort == 'm' or sort == 'M':
            quakes.sort(key=attrgetter('mag'), reverse = True)
            print()
            print("Earthquakes:")
            print("------------")
            for quake in quakes:
               print(quake)
            write_to_file(quakes, "quakes.txt")  

         elif sort == 't' or sort == 'T':
            quakes.sort(key=attrgetter('time'), reverse = True)
            print()
            print("Earthquakes:")
            print("------------")
            for quake in quakes:
               print(quake)
            write_to_file(quakes, "quakes.txt")
         elif sort == 'l' or sort == 'L':
            quakes.sort(key=attrgetter('longitude'))
            print()
            print("Earthquakes:")
            print("------------")
            for quake in quakes:
               print(quake)
            write_to_file(quakes, "quakes.txt")   
         elif sort == 'a' or sort == 'A':
            quakes.sort(key=attrgetter('latitude'))
            print()
            print("Earthquakes:")
            print("------------")
            for quake in quakes:
               print(quake)
            write_to_file(quakes, "quakes.txt")
         userinput = input("\nOptions:\n %7s \n %9s \n %13s \n %7s \n\nChoice: " % ('(s)ort', '(f)ilter', '(n)ew quakes', '(q)uit'))
      elif userinput == 'f' or userinput == 'F':
         filterquake = input('Filter by (m)agnitude or (p)lace? ')
         if filterquake == 'm' or filterquake == 'M':
            low = float(input("Lower bound: "))
            upper = float(input("Upper bound: "))
            print("\nEarthquakes:")
            print("------------")
            quake = (filter_by_mag(quakes, low, upper))
            for q in quake:
               print(q)
            write_to_file(quakes, "quakes.txt")
            
         elif filterquake == 'p' or filterquake == 'P':
            place = input("Search for what string? ")
            print()
            print("Earthquakes:")
            print("------------")
            quake = filter_by_place(quakes, place)

            for q in quake:
               print(q)
            write_to_file(quake, "quakes.txt")
         userinput = input("\nOptions:\n %7s \n %9s \n %13s \n %7s \n\nChoice: " % ('(s)ort', '(f)ilter', '(n)ew quakes', '(q)uit'))

      elif userinput == 'n' or userinput == 'N':
         userinput = input("\nOptions:\n %7s \n %9s \n %13s \n %7s \n\nChoice: " % ('(s)ort', '(f)ilter', '(n)ew quakes', '(q)uit'))


if __name__ == "__main__":
   main()

