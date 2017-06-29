import libtcodpy as libtcod
#defining console attributes
SCREEN_WIDTH=80
SCREEN_HEIGHT=100
LIMIT_FPS=20
#initializing player start point
playerx= SCREEN_WIDTH/2
playery= SCREEN_HEIGHT/2

#initialize for turn-based segments
TURN_BASED=True
#handle key input
def handle_input():
    global playerx,playery
    
    #console control
    key=libtcod.console_wait_for_keypress(TURN_BASED)
    #fullscreen toggle
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    #game exit
    elif key.vk ==libtcod.KEY_ESCAPE:
        return True

    #motion
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playery-=1;
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playery+=1
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerx-=1
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerx+=1


libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'PyRogue', False)

#game loop
while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(0,libtcod.white)
    libtcod.console_put_char(0,playerx,playery,'@', libtcod.BKGND_NONE)
    libtcod.console_flush();
    libtcod.console_put_char(0,playerx,playery,' ',libtcod.BKGND_NONE)
    exit=handle_input()
    if exit:
        break
