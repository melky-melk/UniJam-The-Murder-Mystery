init python:
    class Person:
        def __init__(self, character, name, relationship = 0, romance = 0):
            self.c = character
            self.name = name
            self.relationship = relationship
            self.romance = romance

    # class Inventory:

define e = Character("Eunie")

label start:
    "All that matters in a performance"
    # slow scroll after elipse
    extend "...is how it ends."
    # pause for a little bit
    # OPENING CREDITS WITH MELODICA
    # A game by UniJam Studios
    # Directed by miguel
    # Edited by Chiara

    # "Eunie and Jamie are sitting outdoors, Jamie finishes playing a tune on his Melodica. Eunie starts clapping as Jamie looks away slightly embarrassed. "
    # building up of sound then sudden cut
    pause 1.5
    scene bg cliff_bad
    show eunie neutral

    play music "music/Pirouette_Among_the_Stars_WIP.mp3" fadein 0.75 # loop
    play sound "sound effects/night_ambiance.mp3" volume 0.1 fadein 0.75 loop
    "Eunie" "You didn't tell me you played before! That was awesome!"

    "Jamie" "Well I'm still pretty new to it."
    
    "Eunie" "You know... you should join the Jamming Society!"

    "Jamie" "Jamming Society?"
    "Jamie" "...What does making jam have to do with music?"

    show eunie angry
    "Eunie" "{size=*0.65}Not actual jam you idiot." 
    show eunie happy:
        yoffset 0
        easein 0.30 yoffset -75
        easeout 0.25 yoffset 0
    "Eunie" "Musical jamming! Playing with people."

    "Jamie" "Ohhhhhhh"
    "Jamie" "That makes more sense." 

    show eunie neutral
    "Eunie" "Seriously though, I think you'd enjoy it."

    "Jamie" "But I don't think I'm that a great player... you really think I'd be able to jam with other people?"

    show eunie blush
    "Eunie" "What kind dumb question is that? Jamming's for everyone!"
    show eunie neutral

    "Jamie" "Maybe I should practice for a few months before I play with you guys. I mean I think everyone there is incredible professional musicians and I'm just messing around with thing. I think I'll just mess up and ruin it for everyone else. Imagine what they sa-{nw}"

    "Eunie" "It doesn't matter whether you're a beginner or pro, {nw}"
    show eunie happy
    extend "our jamming welcomes everyone!"

    "Jamie" "..."

    "{size=*0.75}It's embarrassing to be {i}this{/i} new though"

    "Eunie" "You don't even have to know how to play music. It's all about the {i}vibe{/i}"
    "Eunie" "And playing with other people- it's a really different experience"
    show eunie neutral:
        yoffset 0
        easein 0.30 yoffset -75
        easeout 0.25 yoffset 0
    "Eunie" "I can promise you its worth going, at least just once to try it out"

    "Jamie" "hm."

    "Eunie" "Actually, I command you to go, consider it an older sister's demand!"

    "Well... I guess if she's so insistent on it I should probably at least give it a try."

    "Jamie" "Ok... If you say so."
    hide eunie neutral
    hide bg cliff_bad
    show bg black-screen

    stop music
    stop sound
    "I mean... what's the worst that can happen?"
    pause 1.5

    jump morning_scene

label morning_scene:
    scene bg bedroom

    "Alrighty, let's see what we need to bring for later's jam."

    # Jamie can interact with three things in a normal bedroom background. He can interact with the desk (which will lead to more interactables), his bookshelf, his keyboard. 
    menu:
        "Keyboard":
            "Jamie" "My keyboard, Chad. I got it from a dodgy website that fortunately did not lead to an axe murder when I purchased it. I'll haul it to the jams and see how it works out." # Put keyboard in inventory
            jump morning_scene
        "Bookshelf":
            "Jamie" "Books that I never had the energy to read. Always had the time but never had enough energy. I should probably sell these at some point and see if I could get some cool stuff from the money I make."
            jump morning_scene
        "Desk":
            "Jamie" "What's in here..."
            jump desk
        "I think I'm ok":
            jump eunie_enters_room

label desk:
    menu:
        "School ID":
            "Jamie" "Can't go anywhere in uni without this... God, the photo they took of me is actually horrendous" #Put ID in inventory
            jump desk
        "Half-eaten rice ball":
            "Jamie" "Dinner from last night... hmmm..."
            "That was somehow still kinda tasty for some reason?"
            jump desk
        "Headphones":
            "Jamie" "I don't think the bus ride will be bearable without listening to some bangers on the way to uni. You're coming with me."
            jump desk
        "Nah I'll go back":
            jump morning_scene

# Upon interacting with all interactables
label eunie_enters_room:
    # From outside 
    "Eunie" "{size=*0.65}Hey, so I'm gonna go in without your permission-" 
    show eunie happy:
        yoffset 0
        easein 0.30 yoffset -75
        easeout 0.25 yoffset 0

    extend "{size=*2}-and hand you your uni schedule!"
    
    "Jamie" "{size=*2}JESUS CHRIST"

    "Eunie" "Hahaaaa..." 
    extend "{size=*0.75}-I'm not sorry"

    "Eunie" "It actually looks pretty alright for now. A couple shitty classes here and there but you'll be aight. Eventually, you'll probably stop giving enough f's to actually ditch those classes, but for now, word of advice: just follow that sched so you can stay on top of things." 
    
    "Jamie" "Ha thats easy for you to say"

    show eunie neutral
    "Eunie" "When I was at your point in uni, I just stopped going to the classes that bored me and I still got good marks!"

    "Jamie" "So much for you being a straight A's student. How'd you even manage to get good grades?"

    show eunie blush
    "Eunie" "Procrastination, mental breakdowns, and this wonder drug called caffeine." 

    # show eunie salute and leaving 
    show eunie happy:
        yoffset 0
        easein 0.30 yoffset -75
        easeout 0.25 yoffset 0
    
    "Eunie" "Now if you'll excuse me, I'm headed off to get a quadruple shot of espresso! Ciao~"

    hide eunie neutral

    "Oh my god she's going to kill herself..."

    "Welp, I stink. Gonna hit the showers, head to uni and have a personal tour."

label ren_meeting:
    scene bg quadrangle

    "I could literally smell the fungi all the way back in the 1900s. Still looks cool though"

    "???" "I was told this building becomes a sentient monster at night and devours all those who stay inside till 8:43 PM."

    "Jamie" "What the hell-"

    # Stranger offers his hand for Jamie to shake

    show ren neutral
    "Ren" "Haha! Hope I didn't pull your leg a bit too hard. It's just a way to creep out prospective students so they don't enroll in this hellhole. The name's Ren."

    "Ren" "Hmm… you look kinda familiar... Do you happen to be- WAIT-are you the long lost Tiago sibling???"

    "Tiago? That's dad's last name."

    "Jamie" "Ma and Pa kinda split a couple years back, so I don't take Pa's name. It's Jamie Hugo for me. You know Eunie?"

    "Ren" "Bro, she's, like, actual Jamming Society history! Like she is the stuff of legends!"

    # Ren kneels in front of Jamie, bowing sprite
    show ren neutral:
        yoffset 0
        easeout 0.40 yoffset 50   
    "Ren" "My prince, we have awaited your arrival. To be in the presence of royal blood is too much of an honour for a lowly peasant like myself."

    "Jamie" "Oh god, we're in the middle of uni get up"

    "Eunie seems to be a big shot, huh... Never knew about that. Do more people know about her?"

    show ren neutral:
        yoffset 0
    "Ren" "You, my friend, are officially the second coolest person in this university. After your sis, of course. In any case, I assume you'll be in the jams later, considering the massive black case on your back?"

    "Jamie" "I guess..."

    "Ren" "Alright, sweet. I'll smell 'ya later then! I'll screw off for a bit, but you can find me here in the quad every day."

    "Jamie" "Ah… bye then!"

    jump first_jam