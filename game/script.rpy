init python:
    class Person:
        def __init__(self, character, name, relationship = 0, romance = 0):
            self.c = character
            self.name = name
            self.relationship = relationship
            self.romance = romance

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character. this is a final statement

define e = Character("Eunie")

# The game starts here.

label start:
    "All that matters in a performance... is how it ends."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg cafe

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "You see an empty cafe with a peculiar looking man"
    "Oh no he's walking towards you"

    menu:
        "Run away and hide":
            jump ran_away
        "Stand still and hope he doesnt see you":
            show eunie neutral

    "Random Guy?" "Oh my God hi! Fancy seeing you here"
    "...You've never seen this guy before in your life. At least you dont think so?"

    show eunie opening

    "Random Guy?" "sooooo... hows the fit?"

    $ mean = False

    menu:
        "SLAYYY its serving cunt":
            show eunie happy
            "Random Guy?" "i knew youd like it hunty"
        "...ew":
            show eunie angry
            "Random Guy?" "ur a piece of shit"
            $ mean = True
            "Eugh whatever who even is this guy"
            return
        "uhhhh who are you again?":
            show eunie neutral

# labels are just points you can jump to
label introduce:
    show eunie neutral
    e "Oh where are my manners im Eunie!"
    return

label ran_away:
    scene bg cafeteria
    "Ok you lost him. At least you think so?"