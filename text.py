# list = ' * '

# for i in range(5):
#     for j in range(5):
#         print((list),end = "")
#     print()

playerX = 3
playerY =3

def printMap(side):
    for i in range(side):
        for j in range(side):
            if i == playerY and j == playerX:
                print(" P ", end="")
            else:
                print((' * '),end = "")
        print()
def run():
    global playerX, playerY
    direct = input("Your move: ")
    print(direct)
    if direct.lower() == "w":
        playerY = playerY - 1
        if playerY < 0:
            playerY += 1
    if direct.lower() == "s":
        playerY = playerY + 1
        if playerY > 6:
            playerY -= 1
    if direct.lower() == "d":
        playerX += 1
        if playerX > 6:
            playerX -= 1
    if direct.lower() == "a":
        playerX -= 1
        if playerX < 0:
            playerX += 1
printMap(7)
while True:
    print(chr(27) + "[2]")
    printMap(7)
    run()
