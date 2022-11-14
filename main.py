"""This project uses Tkinter library to recreate the popular game Crossy-Road"""

import tkinter as tk
import time
import game_settings as gs

import game as g


def main():
    game = g.Game()

    def key_pressed(event):
        key = event.keysym
        print(f"Pressed key: {key}")
        if key == "Up":
            game.player.move_up()
        elif key == "Down":
            game.player.move_down()
        elif key == "Left":
            game.player.move_left()
        elif key == "Right":
            game.player.move_right()
        else:
            pass
            # do nth

    game.bind("<Key>", key_pressed)

    game.after(ms=gs.CLOCK_TICK, func=game.visual_update())
    game.mainloop()

    '''
    def after(self, ms, func=None, *args):
        """Call function once after given time.

        MS specifies the time in milliseconds. FUNC gives the
        function which shall be called. Additional parameters
        are given as parameters to the function call.  Return
        identifier to cancel scheduling with after_cancel."""
    '''
    # png = PhotoImage(file=r'example.png')  # Just an example
    # canvas.create_image(0, 0, image=png, anchor="nw")

    # Create instances of Level Obj
    # Create one instance of Player Obj
    # Create one instance of Game Obj


if __name__ == '__main__':
    main()

# TODO 1 Make a Game Class to control the entire game-play.
#   Game will be responsible for -
#   Score condition, Gameover condition, Level behavior changes
#   Game obj instance will contain Level Obj and Player Obj

# TODO 2 Make a Level Class to control unique level behaviours
#   Level obj instance will contain CarSpawnBase obj

# TODO 3 Make a CarSpawnBase Class to control spawn positions and randomness of cars spawned
#   CarSpawnBase instance will contain Car obj

# TODO 4 Make a Car Class to control each car instance. speed, appearance, etc.

# TODO 5 Make a Player Class to control all player inputs


