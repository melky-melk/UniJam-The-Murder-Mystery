init python:
    import pygame

    class Note():
        def __init__(self, note, key_code, x, y):
            # renpy.Displayable.__init__(self)

            self.NOTE_WIDTH = 30
            self.NOTE_HEIGHT = 30

            self.note = note
            self.key_code = key_code
            self.x = x
            self.y = y

            self.image = Solid("#ffffff", xsize=self.NOTE_WIDTH, ysize=self.NOTE_HEIGHT)

        def tick():
            # check if the note was missed, delete it if its after
            note_bottom = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            # make this later so that the speed is visible everywhere
            # self.y -= speed
            self.y -= 10

            # youve missed the note
            if self.y > note_bottom:
                return false

    class Key(Note):
        def __init__(self, note, key_code, x, y):
            super().__init__(note, key_code, x, y)
            self.pressed = false

        def tick():
            # check if it is being pressed down, check if it is hitting the note correctly
            # increment points and combo
            return

        def event(self, ev, x, y, st):
            # if the event type was its keycode, meaning if the keycode has been hit you want to change the colour of the key that has been hit
            # if ev.type == self.key_code:
            #     self.pressed = true
            
            # TODO should it be that this will constantly change what is being pressed down where should the self pressed reset?
            self.pressed = ev.type == self.key_code

        def draw():
            if self.pressed == true:
                # TODO is there a better way to recolour, rather than creating a new solid to replace it
                self.image = Solid("#aea9b0", xsize=self.NOTE_WIDTH, ysize=self.NOTE_HEIGHT)
            else:
                self.image = Solid("#ffffff", xsize=self.NOTE_WIDTH, ysize=self.NOTE_HEIGHT)

    class JamDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            keyboard = ["S", "D", "F", "J", "K", "L"]
            keyboard_key_code = [pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k, pygame.K_l]
            self.keys = []
            self.TOP = 129
            self.BOTTOM = 650
            self.SPEED = 10

            # makes 8 keys for the game object to contain
            for i in range(6):
                keys.add(Key(keyboard[i], keyboard_key_code[i], 40 * i, COURT_BOTTOM))

        def render(self):
            r = renpy.Render(width, height)

            # Ask that we be re-rendered ASAP, so we can show the next frame. refreshes the screen
            renpy.redraw(self, 0)

            return r

        # Handles events.
        # ON BUTTON PRESS CHANGE COLOUR
        def event(self, ev, x, y, st):

            import pygame

            # Mousebutton down == start the game by setting stuck to
            # false.
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False

                # Ensure the pong screen updates.
                renpy.restart_interaction()

            # Set the position of the player's paddle.
            y = max(y, self.COURT_TOP)
            y = min(y, self.COURT_BOTTOM)
            self.playery = y

            # If we have a winner, return him or her. Otherwise, ignore
            # the current event.
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

# screen jam():
#     default jam_game = JamDisplayable()

#     add "bg pong field"

#     add pong

#     text _("Player"):
#         xpos 240
#         xanchor 0.5
#         ypos 25
#         size 40

#     text _("Eileen"):
#         xpos (1280 - 240)
#         xanchor 0.5
#         ypos 25
#         size 40

#     if pong.stuck:
#         text _("Click to Begin"):
#             xalign 0.5
#             ypos 50
#             size 40

label first_jam:
    scene bg cafeteria
    "God I'm so damn nervous, theres so many people here"
    "Fuck, my stomach hurts"

    show eunie happy:
        yoffset 0
        easein 0.30 yoffset -75
        easeout 0.25 yoffset 0
    "Eunie" "Hey! You made it"
    "Jamie" "Haha... yeah I did. I- really don't know how this will go man"

    show eunie neutral
    "Eunie" "Hey don't worry, you'll do great" 

