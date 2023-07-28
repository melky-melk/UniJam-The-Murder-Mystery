init python:
    import pygame

    class Note():
        def __init__(self, note, key_code, x, y):
            self.NOTE_WIDTH = 60
            self.NOTE_HEIGHT = 150

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
                return False

    class Key(Note):
        def __init__(self, note, key_code, x, y):
            super().__init__(note, key_code, x, y)
            self.pressed = False

        def tick():
            # check if it is being pressed down, check if it is hitting the note correctly
            # increment points and combo
            return

        def set_pressed(self, pressed):
            # if the event type was its keycode, meaning if the keycode has been hit you want to change the colour of the key that has been hit
            # if ev.type == self.key_code:
            #     self.pressed = true
            
            # TODO should it be that this will constantly change what is being pressed down where should the self pressed reset?
            self.pressed = pressed

        def render(self, width, height, st, at):
            if self.pressed:
                # TODO is there a better way to recolour, rather than creating a new solid to replace it
                self.image = Solid("#aea9b0", xsize=self.NOTE_WIDTH, ysize=self.NOTE_HEIGHT)
            else:
                self.image = Solid("#ffffff", xsize=self.NOTE_WIDTH, ysize=self.NOTE_HEIGHT)

            r = renpy.render(self.image, width, height, st, at)
            return r

    class JamDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)

            # The sizes of some of the images.
            keyboard = ["1", "2", "3", "8", "9", "0"]
            keyboard_key_code = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_8, pygame.K_9, pygame.K_0]
            self.keys = []
            self.HEIGHT = 800
            self.WIDTH = 1600
            self.SPEED = 10

            self.NOTE_WIDTH = 60
            self.NOTE_HEIGHT = 150

            # makes 6 keys for the game object to contain
            for i in range(6):
                x = self.WIDTH/10 + (self.NOTE_WIDTH + self.NOTE_WIDTH/4) * i

                if i > 2:
                    x += 300

                self.keys.append(Key(keyboard[i], keyboard_key_code[i], x, self.HEIGHT))

        def render(self, width, height, st, at):
            r = renpy.Render(width, height)

            for key in self.keys:
                render_object = key.render(width, height, st, at)
                r.blit(render_object, (key.x, key.y))

            # Ask that we be re-rendered ASAP, so we can show the next frame. refreshes the screen
            renpy.redraw(self, 0)
            return r

        # Handles events i.e. whenever a button is pressed, keys being up, down, mouse being clicked and so on.
        def event(self, ev, x, y, st):
            # figure out if the event is a key up or key down
            pressed = None
            if pygame.KEYDOWN == ev.type:
                pressed = True
            elif pygame.KEYUP == ev.type:
                pressed = False
            
            if pressed != None:
                for key in self.keys:
                    if key.key_code == ev.key:
                        key.set_pressed(pressed)
screen jam():
    default jam_game = JamDisplayable()

    add jam_game

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
    
    call screen jam
