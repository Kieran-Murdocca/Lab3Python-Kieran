# Author: Kieran Murdocca kkm5754@psu.edu
# Collaborator: Augustus Perseghin agp5191@psu.edu
# Collaborator: Zehao Liu zql5426@psu.edu
# Collaborator: Nidhi Swamy nms6241@psu.edu
# Section: 004
# Breakout: 15
# Part 2: lab3-python

def sum_n(n): 
  if n>0:
    return n + sum_n(n-1)
  else: 
    return 0

def print_n(s , n): 
  if n>0: 
    print(f"{s}")
    print_n(s, n-1)
  else: 
    return

def run(): 
  n=int(input("Enter an int: "))
  print(f"sum is {sum_n(n)}")
  s=input("Enter a string: ")
  (print_n(s, n))

if __name__ == "__main__": 
  run()