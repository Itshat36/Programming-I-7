def main():
  weight = int(input("weight in killograms: "))
  lenth = int(input("lenth in centimeters: "))
  width = int(input("width in centimeters: "))
  height = int(input("height in centimeters: "))
  yes = 0
  if weight >= 27:
    yes = 2
  elif lenth * width * height >= 100000:
    yes = 2
  if yes == 2:
    print("too heavy")
  if yes ==0:
    print("correct size")
  
  pass


if __name__ == "__main__":
  main()