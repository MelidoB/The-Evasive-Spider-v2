from Application.Objects_For_Display.Player.check_for_obstacles import *
from Application.Objects_For_Display.Inanimate_Objects.move_background_items_position import move_background_items_position

def key_pressed_conditions(key_pressed,character,obstacles, left='a',right='d',top='w',down='s'):

    if key_pressed[ord(left)]:
        if no_obstacle_on_leftside(character, obstacles):
            character.move_left()
            move_background_items_position(obstacles, x = 10)

    if key_pressed[ord(right)]:
        if no_obstacle_on_rightside(character, obstacles):
            character.move_right()
            move_background_items_position(obstacles, x=-10)
    if key_pressed[ord(top)]:
        if no_obstacle_on_topside(character, obstacles):
            character.move_top()
            move_background_items_position(obstacles, y=10)
    if key_pressed[ord(down)]:
        if no_obstacle_on_downside(character, obstacles):
            character.move_down()
            move_background_items_position(obstacles, y=-10)