import libtcodpy as libtcod
import input_handler as ih
from entity import Entity
from render_functions import clear_all, render_all
from map_objects.game_map import GameMap
def main():
    #defining console attributes
    SCREEN_WIDTH=80
    SCREEN_HEIGHT=50
    MAP_WIDTH=60
    MAP_HEIGHT=45
    LIMIT_FPS=20

    colors={
            'dark_wall':libtcod.Color(0,0,100),
            'dark_ground':libtcod.Color(50,50,100)
            }
    
    #create subconsoles
    con=libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
    game_map=GameMap(MAP_WIDTH, MAP_HEIGHT)
    #initialize for turn-based segments
    TURN_BASED=True

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'PyRogue', False)
    key=libtcod.Key()
    mouse=libtcod.Mouse()



    #create actors
    player=Entity(int(MAP_WIDTH/2),int(MAP_HEIGHT/2),'@',libtcod.white)
    npc=Entity(int(MAP_WIDTH-10),int(MAP_HEIGHT-10),'&',libtcod.purple)

    entities=[player,npc]

    #game loop
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)
        render_all(con,entities,game_map,SCREEN_WIDTH,SCREEN_HEIGHT,colors)
        libtcod.console_flush()
        clear_all(con,entities)


        action=ih.handle_keys(key)
        move=action.get('move')
        exit=action.get('exit')
        fullscreen=action.get('fullscreen')
        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x+dx, player.y+dy):
                player.move(dx,dy)
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        if exit:
            return True

if __name__ == '__main__':
    main()
