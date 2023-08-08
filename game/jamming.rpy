init python:
    import pygame
    import os 

    def note_number_to_name(note_number):
        # List of note names in scientific pitch notation
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        # Calculate the octave number and the note name
        octave = note_number // 12 - 1
        note_name = notes[note_number % 12] + str(octave)
        
        return note_name

    class Note():
        def __init__(self, key, note, start_time, duration):
            self.key = key 
            self.note = note

            # spawns in at the top of the screen
            self.width = key.width
            # the height i.e. how long the note should be held down
            self.start_time = float(start_time)
            self.height = int(key.height * duration)
            
            self.x = key.x
            self.y = 0 - self.height

            self.non_pressed_image = Solid("#9b74e8", xsize=self.width, ysize=self.height)
            self.pressed_image = Solid("#714a9e", xsize=self.width, ysize=self.height)
            self.pressed = False
            
        def set_pressed(self, pressed):
            self.pressed = pressed

        def render(self, width, height, st, at):
            image = self.non_pressed_image

            if self.pressed:
                image = self.pressed_image 
            
            return renpy.render(image, width, height, st, at)

        def __str__(self):
            return self.note + " " + str(self.key.pitch) + " " + str(self.start_time)

    class Key():
        def __init__(self, pitch, key_code, x, y, width, height):
            self.pitch = pitch
            self.note = note_number_to_name(int(pitch))
            self.key_code = key_code

            self.x = x
            self.y = y
            self.width = width
            self.height = height
            
            self.non_pressed_image = Solid("#ffffff", xsize=self.width, ysize=self.height) 
            self.pressed_image = Solid("#aea9b0", xsize=self.width, ysize=self.height)
            self.pressed = False

        def set_pressed(self, pressed):
            self.pressed = pressed

        def render(self, width, height, st, at):
            image = self.non_pressed_image
            
            if self.pressed:
                image = self.pressed_image
                
            return renpy.render(image, width, height, st, at)

    class JamDisplayable(renpy.Displayable):

        def parsing_notes(self, song):
            # generates a path from the user's computer
            path = os.path.join(sys.path[0], "game\\jam_data\\" + song + ".txt")
            f = open(path, "r") 

            # Start Time    Pitch	Duration	Dynamic
            # the actual note number it is
            unique_notes = []
            
            lines = []
            for line in f:
                line = line.split("\t", 4)
                lines.append(line)
                unique_notes.append(int(line[1]))

            unique_notes = list(set(unique_notes))
            unique_notes.sort()

            for note in line:
                print(note)

            lines = sorted(lines, key=lambda x: x[1]) # sort by pitch

            # how many seconds it waits before the note_values spawn
            buffer_time = 3

            self.notes = []
            # currently the note_values are arranged by their pitch, so these first note_values should correspond the lowest key avaliable 
            for i, line in enumerate(lines):
                note_value = int(line[1])

                # loop through the unique notes and make the key index equal to the unique note
                for j, unique_note in enumerate(unique_notes):
                    if (note_value == unique_note):
                        key_index = j
                
                # TODO if there are more than the unique notes self.NUM_OF_KEYS we will get a key error when accessing keys. if this is true, then make it so that the notes higher will just get assigned to the end again 
                key = self.keys[key_index]

                # use the key to gather information inside of the note
                self.notes.append(Note(key, note_number_to_name(int(line[1])), float(line[0]) + buffer_time, float(line[2]) * self.SPEED))
                # this speed thing is a little weird

            self.notes = sorted(self.notes, key=lambda x: x.start_time)

            for note in self.notes:
                print(note)
            f.close()

        def __init__(self, song):
            renpy.Displayable.__init__(self)

            self.score = 0
            self.combo = 0

            self.HEIGHT = 800
            self.WIDTH = 1600
            self.SPEED = 1.5

            self.NOTE_WIDTH = 60
            self.NOTE_HEIGHT = 200
            self.NUM_OF_KEYS = 6

            self.finished = False

            keyboard = ["1", "2", "3", "8", "9", "0"]
            keyboard_key_code = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_8, pygame.K_9, pygame.K_0]
            self.keys = []

            # makes 6 keys for the game object to contain
            for i in range(self.NUM_OF_KEYS):
                x = self.WIDTH/10 + (self.NOTE_WIDTH + self.NOTE_WIDTH/4) * i

                if i > (self.NUM_OF_KEYS/2) - 1:
                    x += self.NOTE_WIDTH * 4

                self.keys.append(Key(keyboard[i], keyboard_key_code[i], x, self.HEIGHT, self.NOTE_WIDTH, self.NOTE_HEIGHT))
            
            self.parsing_notes(song)

        def render_score(score, combo, width, height, st, at):
            score_string = " score " + str(self.score)
            combo_string = " combo " + str(self.combo)
            # check if the score or combo was incremented last time it got checked?
            # if score or combo

        # st meaning start time, is the number of seconds that have passed
        def render(self, width, height, st, at):
            r = renpy.Render(width, height)
            # score_string = " score " + str(self.score)
            # combo_string = " combo " + str(self.combo)

            # text = renpy.render(Text(score_string + combo_string), width, height, st, at)
            # r.blit(text, (width/2, height/2))

            for i, note in enumerate(self.notes):
                # when the note passes by the key, and the key is pressed then register a hit
                if (note.y > (note.key.y - note.key.height)):
                    if note.pressed == False and note.key.pressed:
                        note.set_pressed(True)
                        self.score += 1
                # missed note
                else:
                    self.combo = 0
                
                # the actual spawning of the notes that spawn in when the note in the midi file starts
                if (st >= note.start_time): 
                    render_object = note.render(width, height, st, at)
                    # places the rendered object inside of the big rendered object over the entire window
                    r.blit(render_object, (note.x, note.y))
                    note.y += self.SPEED

                    # if the note's position is below the actual screen then remove the note from the list
                    if (note.y >= height + note.height):
                        self.notes.remove(note)
                        print("removed :) " + note.__str__())
                        print(self.notes)

            for key in self.keys:
                render_object = key.render(width, height, st, at)
                r.blit(render_object, (key.x, key.y))


            # if all the notes have been played then end the game
            if len(self.notes) == 0:
                renpy.timeout(0)
                self.finished = True

            # Ask that we be re-rendered ASAP, so we can show the next frame. refreshes the screen
            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            # figure out if the event is a key up or key down
            pressed = None
            if pygame.KEYDOWN == ev.type:
                pressed = True
            elif pygame.KEYUP == ev.type:
                pressed = False
            
            # if it wasnt keyup or down then ev.key would not exist
            if pressed != None:
                for key in self.keys:
                    if key.key_code == ev.key:
                        key.set_pressed(pressed)

            if self.finished:
                print("bro leave the game")
                return "True"

            

screen jam():
    default jam_game = JamDisplayable("the_lick")

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
    
    "Jamie" "Lemme just practice a little bit first"
    hide eunie neutral

    call screen jam

    show eunie angry
    "Eunie" "bruh"
    "Eunie" "Did you- did you really just play the lick"

    "Jamie" "...maybe"
    show eunie happy
    "Eunie" "Ahhhh what am I going to do with you"
    "Jamie" "You know you love it"

    show eunie neutral
    "Eunie" "Uh-huh sure."
    "Eunie" "Okayyy well you seem ready enough"
    extend "{size=*0.65}...unfortunately."
    show eunie happy:
        yoffset 0
        easein 0.30 yoffset -75
        easeout 0.25 yoffset 0
    "Eunie" "So it's time you meet the gang!"
