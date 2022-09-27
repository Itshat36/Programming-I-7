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
 def mm(self, num):
   """move multible"""
   for number in range(0, num):
     self.m()
 def putm(self, num):
   """put multible"""
   for i in range(num - 1):
     self.put()
     self.m()
     self.put()
 def pickm(self, num):
   for_ in range(num - 1):
     self.pick()
     self.m()
     self.pick()
 def sob(self) -> bool:
   """standing on beeper"""
   return beepers_present()
 def jump(self):
   """jump for 510"""
   while self.fic()
     self.m()
   self.tl()
   while self.rib():
     self.m()
   self.tr()
   self.m()
   self.tr()
   while self.fic():
     self.m()
   self.tl()
 def find(self):
   """find for 515"""
   while not facing_north():
     self.tl()
   self.m()
   if not self.sob():
     self.tl()
     self.m()
     self.tl()
     self.m()
   for _ in range(2):
     if not self.sob():
       self.m()
       self.tl()
       self.m()
   pass
  def main():
   """Karel code goes here!"""
   kt = ktools()
   pass
if __name__ == "__main__":
  run_karel_program()