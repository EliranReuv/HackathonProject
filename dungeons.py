import random
import consts


#יצירת מבוך ריק
def create_empty_dungeon():
    matrix_dungeons = []
    for i in range(consts.ROWS):
        mini_dungeon = []
        for j in range(consts.COLS):
            mini_dungeon.append("x")
        matrix_dungeons.append(mini_dungeon)
    return matrix_dungeons

#הדפסת המטריצה
def print_dungeon(matrix_dungeon):
    for row in range(len(matrix_dungeon)):
        print(matrix_dungeon[row])

#הוספת אויבים במקום אקראי - 3 אויבים
def add_enemies(matrix_dungeon):
    for i in range(0, 3):
        x = random.randrange(0, consts.ROWS)
        y = random.randrange(0, consts.COLS)
        if matrix_dungeon[x][y] == "x":
            matrix_dungeon[x][y] = "enemy"
    return matrix_dungeon

#הוספת הדיסק במקום אקראי
def add_disc(matrix_dungeon):
    for i in range(1):
        x = random.randrange(0, consts.ROWS)
        y = random.randrange(0, consts.COLS)
        if matrix_dungeon[x][y] == "x":
            matrix_dungeon[x][y] = "disc"
    return matrix_dungeon

#הוספת השחקן במיקום ה0,0 במטריצה
def add_player(matrix_dungeon):
    for i in range(0, 1):
        for j in range(0, 1):
            matrix_dungeon[i][j] = "player"
    return matrix_dungeon

#יצירת המבוך
def create_dungeon():
    dungeon = []
    dungeon = create_empty_dungeon()
    dungeon = add_disc(dungeon)
    dungeon = add_enemies(dungeon)
    dungeon = add_player(dungeon)
    return dungeon


dungeons = create_dungeon()
print_dungeon(dungeons)

