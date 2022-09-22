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
 def put():
   """Put beeper"""
   put_beeper()
 def put2(self):
    """put 2 beepers in a line"""
    self.put()
    self.m()
    self.put()
 def put5():
   """fibe beepers in a line"""
   self.put2 
   self.move
   self.put2
   self.move
   self.put
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


 def fic(self):
   """front is clear"""
   front_is_clear()
 def fib(self):
  """front is blocked"""
  return not self.fic()
 def ric(self):
  """right is clear"""
  self.tl()
  if self.fic():
    self.tl()
    return true #imidetly exit funtion
 def rib(self):
   """right is block"""
   return not self.ric()
 def mazemove(self):
   """maze move"""
   if self.fib():
     self.tl()
   else:
     self.m()
     if self.ric():
       self.tr()
       self.m()
     if self.ric():
       self.tr
       self.m()
     pass
  
def main():
    """Karel code goes here!"""
    kt = ktools()
    kt.m()
    put_beeper()
    kt.tl()
    kt.m()
    put_beeper()
    kt.m()
    put_beeper()
    kt.m()
    put_beeper()
    kt.m()
    put_beeper()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.tr()
    kt.m()
    kt.m()
    kt.m()
    put_beeper()
    kt.m()
    put_beeper()
    kt.m()
    kt.tl()
    kt.m()
    put_beeper()
    
    
    pass
if __name__ == "__main__":
  run_karel_program()