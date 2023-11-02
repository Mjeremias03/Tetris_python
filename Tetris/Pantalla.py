from enum import Enum
import keyboard

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4

def tetris():
    screen = [
        ['⬛', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬛', '⬛', '⬛', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'], 
        ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️'],
        ['⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️', '⬜️']
    ]

    print_screen(screen)
    rotatee = 0
    while(True):

        event = keyboard.read_event()
        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            if event.name == "down":
                (screen,rotatee) = move_pieces(screen,Movement.DOWN,rotatee)
            elif event.name == "right":
                (screen,rotatee) = move_pieces(screen,Movement.RIGHT,rotatee)
            elif event.name == "left":
                (screen,rotatee) = move_pieces(screen,Movement.LEFT,rotatee)
            elif event.name == "space":
                (screen,rotatee) = move_pieces(screen,Movement.ROTATE,rotatee)            
def move_pieces(screen: list, movement:Movement,rotatee:int) -> (list,int):
    new_screen = [["⬜️"] * 10 for _ in range(10)]
    rotate_index = 0
    rotate = [[(0,0),(0,0),(0,0),(0,0)],
              [(0,1),(-1,0),(0,-1),(1,-2)],
              [(0,2),(1,1),(-1,1),(-2,-0)],
              [(0,0),(0,0),(0,0),(0,0)]]
    new_rotation = rotatee
    if movement is Movement.ROTATE:
       new_rotation = 0 if rotatee == 3 else rotatee + 1

    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item == "⬛":
                new_row_index = 0
                new_column_index = 0
                if movement == Movement.DOWN:
                    new_column_index = column_index
                    new_row_index = row_index + 1
                elif movement == Movement.RIGHT:
                    new_row_index = row_index
                    new_column_index = column_index + 1
                elif movement == Movement.LEFT: 
                    new_row_index = row_index
                    new_column_index = column_index - 1
                elif movement == Movement.ROTATE:
                    new_row_index= row_index + rotate[new_rotation][rotate_index][0]
                    new_column_index = column_index + rotate[new_rotation][rotate_index][1]
                    rotate_index += 1
                if new_row_index > 9 or new_column_index > 9  or new_column_index < 0:
                    print("No se puede realizar")
                    return (screen, rotatee)
                else:
                     new_screen[new_row_index][new_column_index] = "⬛"
           
    print_screen(new_screen)
    return (new_screen, new_rotation)

def print_screen(screen):
    print("\n Pantalla: \n")
    for row in screen:
        print("".join(row))

tetris()

