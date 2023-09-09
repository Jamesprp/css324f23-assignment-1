def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    #x -> y
    t = 5-y
    if x > 0 and t > 0:
        if x>t:
            yield ((x-t,5,z),t)
        else:
            yield ((0,y+x,z),x)
    #x->z
    t = 3-z
    if x > 0 and t > 0:
        if x>t:
            yield ((x-t,y,3),t)
        else:
            yield ((0,y,z+x),x)
    #y->x
    t = 8-x
    if y > 0 and t > 0:
        if y>t:
            yield ((x-t,5,z),t)
        else:
            yield ((0,y+x,z),y)
    #y->z
    t = 3-z
    if y > 0 and t > 0:
        if y>t:
            yield ((x,y-t,3),t)
        else:
            yield ((x,0,z+y),y)

    #z->x
    t=8-x
    if z > 0 and t > 0:
        if z>t:
            yield ((8,y,z-t),t)
        else:
            yield ((x+z,y,0),z)
    
    #z -> y
    t=5-y
    if z > 0 and t > 0:
        if z>t:
            yield ((x,5,z-t),t)
        else:
            yield ((x,y+z,0),z)