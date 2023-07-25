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

define e = Character("Jamie")

label start:
    # slow scroll after elipse
    "All that matters in a performance"
    extend "...is how it ends."
    # pause for a little bit

    # fade in
    scene bg cliff_bad

    # "Eunie and Jamie are sitting outdoors, Jamie finishes playing a tune on his Melodica. Eunie starts clapping as Jamie looks away slightly embarrassed. "

    show eunie neutral
    "Eunie" "You didn't tell me you played before! You know... you should join the Jamming Society!"

    "Jamie" "Jamming Society?"

    "Jamie" "...What does making jam have to do with music?"

    show eunie angry
    "Eunie" "{size=*0.75} Not actual jam you idiot." 
    show eunie happy:
        yoffset 0
        easein 0.30 yoffset -75
        easeout 0.25 yoffset 0
    "Eunie" "Musical jamming! Playing with people."

    show eunie neutral
    "Jamie" "Ohhhhhhh"
    "Jamie" "That makes more sense." 

    "Eunie" "Seriously though, I think you'd enjoy it."

    "Jamie" "But I don't think I'm that a great player... you really think I'd be able to jam with other people?"

    show eunie blush
    "Eunie" "What kind dumb question is that? Jamming's for everyone!"
    show eunie neutral

    "Jamie" "Maybe I should practice for a few months before I play with you guys. I mean I think everyone there is incredible professional musicians and I'm just messing around with thing. I think I'll just mess up and ruin it for everyone else. Imagine what they sa{nw}"

    "Eunie" "It doesn't matter whether you're a beginner or pro, {nw}"
    show eunie happy
    extend "our jamming welcomes everyone!"

    "{size=*0.75}It's embarrassing to be {i}this{/i} new though"

    # have a different happy pose, happy 1 and happy 2 for variety
    "Eunie" "And playing with other people- it's a really different experience"
    "Eunie" "I can promise you its worth going, at least just once to try it out"
    "Jamie" "Ok... If you say so."
    "I mean... Whats the worst that can happen?"