def change_img(images_movements,index_movements, direction):
    img = images_movements[direction][index_movements[direction]]
    if index_movements[direction] < len(images_movements[direction])-1:
        index_movements[direction] += 1
    else:
        index_movements[direction] = 0


    for i in index_movements.keys():
        if i != direction:
            index_movements[i] = 0
    return img