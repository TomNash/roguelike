import libtcodpy as libtcod

#handle key input
def handle_keys(key):
    #fullscreen toggle
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        return {'fullscreen':True}
       #game exit
    elif key.vk ==libtcod.KEY_ESCAPE:
        return {'exit':True}
    #motion
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        return {'move':(0,-1)}
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        return {'move':(0,1)}
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        return {'move':(-1,0)}
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        return {'move':(1,0)}

    return{}


