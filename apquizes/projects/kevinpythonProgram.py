
menu = input('Hello human, welcome to my customizer program. type start to start, type close to crash. ')
if menu == "close":
    print("[PROGRAM TERMINATED]")
elif menu == 'start':
    start = input ('Lets start off simple human, is your character a boy or girl? ')

    if start == 'boy':
        head = input("Let's get started human,does your character wear anything on their head?(if nothing type 'no head gear') ")   
        face = input('what facewear do they have on? (if nothing type no facewear) ')
        shirt = input('what kind of shirt do they wear ')
        gloves = input('Are they wearing any gloves? ')
        pants = input('What kind of pants are they wearing? (type no if you choose dress before) ')
        shoes = input('what kind of shoes are they wearing? ')
        print('Okay human, You have completed the customiztion progress, This is your character')
        print("Your character wears " + head + " with " + face + " and " + shirt + " with " + pants + " pants and " + gloves + " and finally " + shoes)
        like = input('Do you like your creation? ')
        if like == 'yes':
            print("We are glad you like it, restart the TERMMAl to create again")
        elif like == 'no':
            print("YOU [banned word], IT'S YOUR CREATION, WHAT DO YOU MEAN YOU DON'T LIKE IT, YOU MADE IT! YOU HUMANS ARE ALL THE SAME, unless it's just you don't think what you created best fitted you and wanna try again, if that's the case then pay the last statement no mind, it does not aply to you[PROGRAM TERMNATED]")

    if start == 'girl':
        head = input("Let's get started human,does your character wear anything on their head?(if nothing type 'no head gear') ")   
        face = input('what facewear do they have on? (glasses, makeup, etc)? (if nothing type no facewear) ')
        dress = input("what kind of dress do they wear (if nothing type 'no dress')")
        gloves = input('what kind of gloves are they wearing? ')
        shoes = input('what kind of shoes are they wearing? ')
        print('Okay human, You have completed the customiztion progress, This is your character')
        print("Your character wears " + head + " with " + face + " and " + dress + " with " + pants + " pants and " + gloves + " and finally " + shoes)
        like = input('Do you like your creation? ')
        if like == 'yes':
            print("We are glad you like it, restart the TERMMAl to create again")
        elif like == 'no':
            print("YOU [banned word], IT'S YOUR CREATION, WHAT DO YOU MEAN YOU DON'T LIKE IT, YOU MADE IT! YOU HUMANS ARE ALL THE SAME, unless it's just you don't think what you created best fitted you and wanna try again, if that's the case then pay the last statement no mind, it does not aply to you[PROGRAM TERMNATED]")