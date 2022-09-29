from stanfordkarel import *
from time import sleep

class ktools:
 def m(self):
    """shorthand for move"""
    move()
 def tl(self):
   """"Turn Left"""
   turn_left()
 def tr(self):
   """"Turn Right"""
   self.tl()
   self.tl()
   self.tl()
 def ta(self): 
   """turn around"""
   self.tl()
   self.tl()
 def pick(self):
   """pick beeper"""
   pick_beeper()
 def put(self):
    """Put Beeper"""
    put_beeper()
 def put2(self):
    """put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()
 def put5():
   """fibe beepers in a line"""
   self.put2()
   self.move()
   self.put2()
   self.move()
   self.put()
 def h(self):
   """print H"""
   self.tl()
   self.put5()
   self.tr()
   self.put5()
   self.m()
   self.m()
   self.tl()
   self.put5()
   self.m()
   self.m()
   self.tl()
   self.m()
   self.put2()
   self.m()
   self.m()
   self.tl()
   self.m()
   self.m()
   self.m()
   self.m()


 def fourb(self):
   self.put()
   self.tl()
   self.m()
   self.m()
   self.m()
   self.tr()
   self.m()
   self.tr()
   self.m()
   self.m()
   self.m()
 def rugw(self):
   self.m()
   self.m()
   self.m()
   self.m()
   self.m()
   self.m()
   self.tl()
   self.put()
 def rug(self):
   self.m()
   self.m()
   self.m()
   self.m()
   self.m()
   self.m()
   self.m()
   self.tl()
   self.put()
 def ky(self):
   self.pick()
   self.m()
   self.pick()
   self.m()
   self.pick()
   self.m()
   self.tl()


   
def main():
   """Karel code goes here!"""
   kt = ktools()
   kt.m()
   kt.m()
   kt.tl()
   kt.m()
   kt.m()
   kt.tr()
   kt.ky()
   kt.ky()
   kt.ky()
   kt.ky()
   pass
if __name__ == "__main__":
  run_karel_program()