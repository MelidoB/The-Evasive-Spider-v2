from Application.Objects_For_Display.Inanimate_Objects.Inanimate_Objects import Inanimate_Object

def Inanimate_Objects_facilitator(walls,w_counter,x,y,w_amount_to_create=10,x_i=0,y_i=0):
    for i in range(w_amount_to_create):
        walls.append(Inanimate_Object())
        walls[w_counter].set_img("wall.png")
        walls[w_counter].set_coord(x,y)
        walls[w_counter].block_movement = True
        w_counter+=1
        x += x_i
        y += y_i

    x-= x_i
    y-= y_i
    return w_counter,x,y
