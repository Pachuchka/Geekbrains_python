from time import sleep
class TrafficLight:

   def __init__(self,c):
    self.__color = c

   def running(self):
       _color_dict ={0:"Red", 1:"Yellow", 2:"Green"}
       _timing = {'Green': 7, 'Yellow':2,'Red':7}

       while True:
           print(_color_dict.get(self.__color))
           sleep(float(_timing.get(_color_dict.get(self.__color))))
           self.__color=(self.__color+1)%3


Traffic = TrafficLight(0)
Traffic.running()
