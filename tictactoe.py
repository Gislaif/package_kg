import random
print("welcome to TIC-TAC-Toe")
print("You need to choose a position")
print("_ _ _")
print("_ _ _")
print("_ _ _")
print("choose a number 0 to 9: ")
print("1 2 3")
print("4 5 6")
print("7 8 9")

def show_grid(grid):
 for indice in range(len(grid)):
   print (grid[indice], end=" ")
   if indice == 2 or indice == 5:
    print (" ")
grid = ["_"] * 9
choice = int(input("What is your choice: "))
grid[choice-1]="X"
show_grid(grid)
#check_grid(grid)

choice_computer = random.randint(1, 9)
while grid[choice_computer-1]!="_":
    choice_computer = random.randint(1, 9)
    grid[choice_computer-1]="0"
    show_grid(grid)
choice_computer=int(input("What is your choice"))
show_grid(grid)

print(choice_computer)
show_grid(grid)







