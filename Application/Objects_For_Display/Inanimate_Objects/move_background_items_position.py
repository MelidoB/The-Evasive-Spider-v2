def move_background_items_position(obstacles,x=0,y=0):
    for i in range(0, len(obstacles)):
        obstacles[i].set_coord(obstacles[i].x + x, obstacles[i].y + y)