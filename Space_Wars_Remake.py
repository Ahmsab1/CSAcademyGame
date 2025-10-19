

app.background = rgb(0,21,43)

app.current_stage = 1
 
##### variables and lists
 
### checks if stuff has been created/ drawn

app.shapes_created = False #checks if shapes have been drawn for each stage/ the current stage

app.enemies_created = False # checks if the enemies have been drawn 

app.congrats_display = False#

app.loser_display = False#

app.bear_named = False
 
### lists to store game objects 

app.enemies = [] #stage 3

app.bullets = [] #stage 3

app.enemy_bullets = [] #stage 3
 
# used in create_planets()

planet_colors = ['brown','orange','gold','steelblue','lightseagreen','plum','mediumvioletred','paleturquoise']
 
#

app.shot_fired = False

app.enemies_left_bound = True
 
### player

app.player = Circle(200,380,10, fill='white')

app.player.centerX = 200

app.player.centerY = 380

app.player.visible = False

app.player_lives = 3
 
### ammo

app.ammo = 10

app.max_reloads = 2

app.remaining_reloads = app.max_reloads

app.reloading = False

app.reload_timer = 0
 
##### groups
 
# bear

bear = Group(

    Circle(200, 380, 70, fill='white'), #body

    Circle(150, 245, 30, fill='tan'), #l ear

    Circle(250, 245, 30, fill='tan'), #r ear

    Circle(250, 245, 20, fill=gradient('peru','saddlebrown', start='top-right')), #palevioletred

    Circle(150, 245, 20, fill=gradient('peru','saddlebrown', start='top-left')), #inner ear

    Circle(200, 280, 60, fill='tan'), #head

    #eyes

    Circle(175, 265, 7),

    Circle(225, 265, 7),

    Circle(226, 263, 2, fill='white'),

    Circle(176, 263, 2, fill='white'),


    RegularPolygon(200,285,8,3, rotateAngle=180), #nose

    Circle(193,292,8, fill=None, border='black'), #mouth

    Circle(207,292,8, fill=None, border='black'), #also mouth

    RegularPolygon(190,287,12,3, rotateAngle=120, fill='tan'), #triangle to make mouth mouthy

    RegularPolygon(210,287,12,3, rotateAngle=238, fill='tan'), #triangle

    Oval(165,285,20,10, fill='palevioletred', opacity=30), #blush

    Oval(235,285,20,10, fill='palevioletred', opacity=30), #blush

    Circle(200, 260, 90, fill='lightblue', opacity = 30) #astronaut bubble thing
 
 
)
 
bear.visible = False
 
 
# start button
 
start_button = Group(

    Rect(120, 160, 160, 80, fill='white'),

    Arc(120, 200, 80, 80, 180, 180, fill='white'),

    Arc(280, 200, 80, 80, 0, 180, fill='white'),

    Label('START', 200, 200, size=30, fill='black', font='orbitron')

    )
 
start_button.opacity = 80
 
start_button.visible = False
 
 
# check box
 
check_box = Group(

    Circle(345,355,25, fill='green'),

    Circle(345,355,20, fill='forestgreen'),

    Label('ok', 345,355, fill='white', font='orbitron', bold=True, size=18)


    )   

check_box.visible = False
 
 
manual = Group(

    Rect(18,280,65,100,fill='white'),

    Label('Manual', 51, 300, font='orbitron', bold=True),

    Label('🩈', 50, 340, font='symbols',size=50)

    )

manual.visible = False
 
close_box = Group(

    Rect(125,300,150,28, fill='white', opacity=80),

    Label('close', 200, 313,font='orbitron', size=20)

     )

close_box.visible = False
 
instructions = Group(

    Rect(40,40,320,320, fill='white', opacity=30),

    Rect(42,42,316,316, fill=rgb(0,21,43), opacity=50),

    Rect(40,40,320,320, fill=None, border='white'),

    Circle(40,40,20, fill=None, border='white'),

    Arc(40,40,10,20,40,280, fill=None, border='white'),

    Line(30,30,90,30, fill='white'),

    Line(30,30,30,100, fill='white'),


    Circle(360,360,20, fill=None, border='white'),

    Arc(360,360,10,20,40,280, fill=None, border='white', rotateAngle = 180),

    Line(370,370,370,300, fill='white'),

    Line(370,370,310,370, fill='white'),

    Label('Adventures of the', 200,80, font='orbitron', size=28, fill='white'),

    Label('bear', 200, 115, font='orbitron', size=28, fill='white'),

    Label('...',200,140, fill='white',size=20),

    Label('use the arrows', 175, 180, font='orbitron', size=18, fill='white'),

    Label('⇦', 270, 180, size=20, font='symbols', fill='white'),

    Label('⇦',  290, 180,rotateAngle=180, size=20, font='symbols', fill='white'),

    Label('to move your player', 200, 215, size=18, fill='white', font='orbitron'),

    Label('shoot: spacebar',200,250, size=18, fill='white', font='orbitron'),

    close_box

    )

instructions.visible = False
 
speech_bubble = Group(

    Rect(200,50,180,100, fill='white'),

    Polygon(360,145,300,205,335,145, fill='white'),

    Label('CHAAARGE!!!', 290, 100, font='orbitron', size=20)

    #Label('Lets shoot some', 290, 85, font='orbitron', size=15),

    #Label('bastards', 290, 110, font='orbitron', size=20)

    )

speech_bubble.visible = False
 
name_decor = Group(

    Line(35,35,100,35, fill='white'),

    Line(35,35,35,80, fill='white'),

    Arc(35,35,10,20,40,280, fill=None, border='white'),

    Circle(35,35,15, fill=None, border='white')

    )

name_decor.visible = False
 
### helper functions
 
def create_planets():

    for color in planet_colors:

        Circle(randrange(0,400), randrange(0,400), randrange(5,35), fill=gradient(color,'black', start='left'))


def create_stars():
 
 
    for _ in range(50,80):

        Star(randrange(0,400), randrange(0,400), randrange(1,3), randrange(5,10), fill='white')
 
 
### functions for functionality - not aesthetics
 
#spawns enemies in a V - shape (triangle)
 
def spawn_enemies():

    for x in range(5):

       for y in range(5-x):

           enemy = RegularPolygon(x*60+60/2*y+80, y*45+30, 20, 3, fill='white', rotateAngle = 180)

           app.enemies.append(enemy)
 
 
#checks if a bullet has hit an enemy

def hits_enemy(bullet, enemy):

    return bullet.hitsShape(enemy)

#checks if an enemy bullet has hit player

def hits_me(enemy_bullet, player): 

    return enemy_bullet.hitsShape(player)


# function that allows enemeis to fire bullets    

def enemy_fires(enemy): 

    enemy_bullet = RegularPolygon(enemy.centerX, enemy.centerY, 5, 3, fill='red', rotateAngle=180 )

    enemy_bullet.visible = True

    app.enemy_bullets.append(enemy_bullet)
 
### moves the enemies on the x axis
 
def shift_enemies_x(val):  

    for enemy in app.enemies:

        enemy.centerX += val

### moves on the y axis

def shift_enemies_y(val):

    for enemy in app.enemies:

        enemy.centerY += val
 
#####
 
 
###    built in functions:   
 
 
def onMousePress(mouseX, mouseY):

 
    if app.current_stage == 1:

        if start_button.hits(mouseX, mouseY):

            app.current_stage +=1


    elif app.current_stage == 2:

 
        if check_box.hits(mouseX, mouseY):

            app.current_stage +=1


        elif manual.hits(mouseX, mouseY):

            manual.visible = False

            instructions.visible = True

            bear.visible = False

            check_box.visible = False

            speech_bubble.visible = False

        elif instructions.visible == True and close_box.hits(mouseX, mouseY):

            instructions.visible = False

            manual.visible = True

            bear.visible = True

            check_box.visible = True

            name_decor.visible = False



def onKeyHold(keys):

    if 'right' in keys and 'left' in keys:

        return

    elif 'right' in keys:

        app.player.centerX += 5

        if app.player.centerX >= 390:

            app.player.centerX = 385
 
    elif 'left' in keys:

        app.player.centerX -= 5

        if app.player.centerX <= 10:

            app.player.centerX = 15

 
def onKeyPress(keys):

    if 'space' in keys and app.reloading == False:

        if app.ammo > 0:

            bullet = RegularPolygon(app.player.centerX, app.player.centerY, 5, 3, fill='white' )

            bullet.visible = True

            app.bullets.append(bullet)

            app.shot_fired = True

            app.ammo -=1

        else: 

            if app.remaining_reloads > 0:

                app.reloading = True

                app.reload_timer = 60

                app.remaining_reloads -=1


            else: 

                if app.loser_display == False: 

                    app.player.visible = False

                    Label('HAH', 200, 150, font='orbitron', fill='white', size=60)

                    Label('Out of bullets', 200, 220, font='orbitron', fill='white', size=50)

                    Label('you lose :)', 200, 280, font='orbitron', fill='white', size=30 )

                    app.loser_display = True

                    for enemy in app.enemies:

                        enemy.visible = False

 ### onStep
 
def onStep():
 
    
    if app.current_stage == 1:
        start_button.visible = True
        start_button.toFront()

 
        
        if app.shapes_created == False: # ensures that the shapes are only drawn once and not on each step
            create_planets()
            create_stars()
            app.shapes_created = True
 
        
    elif app.current_stage == 2:
        start_button.visible=False
        if instructions.visible == False:
            bear.visible = True
            bear.toFront()
            check_box.visible = True
            manual.visible = True
            speech_bubble.visible = True
 
        else: 
            bear.visible = False
            check_box.visible = False
            manual.visible = False
            app.bear_name.visible = False
            name_decor.visible = False
            speech_bubble.visible = False

        if app.bear_named == False: # same thing as on line 207
            app.name = app.getTextInput('name the bear:')
            app.bear_name = Label(app.name, 100, 72, size = 50, font = 'orbitron', fill='white')
            app.bear_named = True
            name_decor.visible = True

    elif app.current_stage == 3:
        # hides unnecessary stuff from stage 2
        app.player.visible = True
        app.player.toFront()
        bear.visible = False
        manual.visible = False
        check_box.visible = False
        app.bear_name.visible = False
        speech_bubble.visible = False
        name_decor.visible = False

 
        if app.enemies_created == False: 
            spawn_enemies()
            app.enemies_created = True

        if len(app.enemies) > 0:
            leftMostEnemy = min(app.enemies, key = lambda enemy: enemy.centerX) #identifies the enemie furthest to the left
            rightMostEnemy = max(app.enemies, key = lambda enemy: enemy.centerX) #same but right

            if app.loser_display == False and len(app.enemies)>0:
                randomEnemy = app.enemies[randrange(0,len(app.enemies))]
                # chooses a random enemy to fire ^^
                if random() < 0.06: 
                    enemy_fires(randomEnemy)
                #random chance for an enemy to fire (6%)^^

            #print(leftMostEnemy.centerX, rightMostEnemy.centerX)
            if app.enemies_left_bound == True and len(app.enemies)>0:
                if leftMostEnemy.centerX <= 20:
                    app.enemies_left_bound = False
                    shift_enemies_x(1)
                    shift_enemies_y(5)
                else:
                    shift_enemies_x(-1)
            else:
                if rightMostEnemy.centerX >= 380:
                    app.enemies_left_bound = True
                    shift_enemies_x(-1)
                    shift_enemies_y(5)
                else:
                    shift_enemies_x(1)     
            #moves enemies within the allowed space   ^^     
        else: 
            if app.congrats_display == False:
                Label('Congrats', 200,180, size=60, font='orbitron', fill='white')
                app.congrats_display = True
                #displays congrats  if all enemies are gone ^^
        # handles reloading        
        if app.reloading == True:
            if app.reload_timer > 0: 
                app.reload_timer -= 1
            else: 
                app.ammo = 15
                app.reloading = False

        #player and bullet collisions
        if app.shot_fired == True:
            for bullet in app.bullets:
                bullet.centerY -= 3
                for enemy in app.enemies:
                    if hits_enemy(bullet, enemy):
                        print('hit')
                        enemy.visible = False
                        bullet.visible = False
                        app.bullets.remove(bullet)
                        app.enemies.remove(enemy)
                        break
                if bullet.centerY < 0:
                    bullet.visible = False
                    app.bullets.remove(bullet)
                    #removes player bullets from list once out of frame/ canvas



        for enemy_bullet in app.enemy_bullets:
            enemy_bullet.centerY += 3
            if hits_me(enemy_bullet, app.player):
                enemy_bullet.visible = False
                app.enemy_bullets.remove(enemy_bullet)
                # removes enemy bullets from the list 
                if app.player_lives > 0:
                    app.player_lives -= 1
                    app.player.opacity -= 20
                    if app.player_lives <= 0 and app.loser_display == False and app.enemies:
                        Label('HAH', 200, 150, font='orbitron', fill='white', size=60)
                        Label('You suck', 200, 220, font='orbitron', fill='white', size=70)
                        app.loser_display = True
                        app.player.opacity = 0
                        for enemy in app.enemies:
                            enemy.visible = False


            if enemy_bullet.centerY > 400:
                enemy_bullet.visible = False
                app.enemy_bullets.remove(enemy_bullet)
                # removes bullets that didnt hit player but have exited the canvas
