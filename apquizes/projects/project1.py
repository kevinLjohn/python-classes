
menu = input('Hello human, welcome to my customizer program. type start to start, type close to crash. ')
if menu == "close":
    print("[PROGRAM TERMINATED]")
elif menu == 'start':
    head = input("Let's get started human,does your character wear anything on their head?(type nothing if nothing for any of the options and also add a space at the end of your options) ")   
    face = input('Do they have anything on their face? ')
    shirt = input('what kind of shirt do they wear, or do they wear a dress(make sure to type shirt or dress at the end)')
    gloves = input('Are they wearing any gloves? ')
    pants = input('What kind of pants are they wearing? (type no if you choose dress before) ')
    shoes = input('what kind of shoes are they wearing? ')
    print('Okay human, You have completed the customiztion progress, This is your character')
    print("Your character wears a " + head + "with " + face + "and a " + shirt + "with " + pants + "pants and " + gloves + "and finally " + shoes)
    like = input('Do you like your creation? ')
    if like == 'yes':
        print("We are glad you like it, restart the TERMMAl to create again")
    elif like == 'no':
        print("YOU BITCH, IT'S YOUR CREATION, WHAT DO YOU MEAN YOU DON'T LIKE IT, YOU MADE IT! YOU HUMANS ARE ALL THE SAME, unless it's just you don't think what you created best fitted you and wanna try again, if that's the case then pay the last statement no mind, it does not aply to you[PROGRAM TERMNATED]")
