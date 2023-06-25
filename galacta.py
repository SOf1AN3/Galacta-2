import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()


# Constantes et initialisations ---------------------------------------------------------------------------------------
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GALACTA 2")

GREY = (30, 30, 30)
WHITE = (255, 255, 255)

SCORE_FONT = pygame.font.SysFont('arial', 40)
LOSE_FONT = pygame.font.SysFont('arial', 150)


FPS = 60

VEL = 13
ENNEMY1_VEL = 17
BULLET_VEL = 25
ENNEMY_BULLET_VEL = 15

# Ennemy Var
ennemy_count = 0
nb_ennemies = 15


LEVEL = 1
current_level = 1

SCORE = 0

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 130, 100
ENNEMY_SPACESHIP_WIDTH, ENNEMY_SPACESHIP_HEIGHT = 110, 80

ENNEMY1_START_X_POSITION = WIDTH + 20
ENNEMY1_START_Y_POSITION = 0


# Images ------------------------------------------------------------------------------------------------------------
player_spaceship_image = pygame.image.load(os.path.join('textures', 'player.png'))
player_spaceship = pygame.transform.scale(player_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

space = pygame.transform.scale(pygame.image.load(os.path.join('textures', 'space.png')), (WIDTH, HEIGHT))
ennemy_spaceship_image = pygame.image.load(os.path.join('textures', 'ship1.png'))
ennemy2_spaceship_image = pygame.image.load(os.path.join('textures', 'ship2.png'))
ennemy3_spaceship_image = pygame.image.load(os.path.join('textures', 'ship3.png'))
ennemy4_spaceship_image = pygame.image.load(os.path.join('textures', 'ship4.png'))

ennemy_spaceship = pygame.transform.rotate(pygame.transform.scale(ennemy_spaceship_image, (ENNEMY_SPACESHIP_WIDTH, ENNEMY_SPACESHIP_HEIGHT)), 180)
ennemy2_spaceship = pygame.transform.rotate(pygame.transform.scale(ennemy2_spaceship_image, (ENNEMY_SPACESHIP_WIDTH, ENNEMY_SPACESHIP_HEIGHT)), 180)
ennemy3_spaceship = pygame.transform.rotate(pygame.transform.scale(ennemy3_spaceship_image, (ENNEMY_SPACESHIP_WIDTH, ENNEMY_SPACESHIP_HEIGHT)), 180)
ennemy4_spaceship = pygame.transform.rotate(pygame.transform.scale(ennemy4_spaceship_image, (ENNEMY_SPACESHIP_WIDTH, ENNEMY_SPACESHIP_HEIGHT)), 180)


health_1 = pygame.transform.scale(pygame.image.load(os.path.join('textures', '1.png')),(250, 50))
health_2 = pygame.transform.scale(pygame.image.load(os.path.join('textures', '2.png')),(250, 50))
health_3 = pygame.transform.scale(pygame.image.load(os.path.join('textures', '3.png')),(250, 50))
health_4 = pygame.transform.scale(pygame.image.load(os.path.join('textures', '4.png')),(250, 50))
health_5 = pygame.transform.scale(pygame.image.load(os.path.join('textures', '5.png')),(250, 50))

# Audio --------------------------------------------------------------------------------------------------------------

SOUND_BULLET_HIT =  pygame.mixer.Sound(os.path.join('audio', 'laser_hit.wav'))
SOUND_BULLET_HIT.set_volume(0.5)

SOUND_BULLET_SHOT = pygame.mixer.Sound(os.path.join('audio', 'laser_shot.wav'))
SOUND_BULLET_SHOT.set_volume(0.15)

SOUND_PLAYER_LOSE = pygame.mixer.Sound(os.path.join('audio', 'player_dies.wav'))
SOUND_PLAYER_LOSE.set_volume(0.5)

SOUND_ENNEMY_DIE = pygame.mixer.Sound(os.path.join('audio', 'ennemy_dies.wav'))
SOUND_ENNEMY_DIE.set_volume(0.5)

pygame.mixer.music.load(os.path.join('audio', "mattashi.mp3"))
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# Events --------------------------------------------------------------------------------------------------------------
ennemy_hit = pygame.USEREVENT + 1
player_hit = pygame.USEREVENT + 2

# Fonctions --------------------------------------------------------------------------------------------------------------
    # Player --------------------------------------------------------------------------------------------------------------
def player_handle_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x > 0:
        player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player.x + SPACESHIP_WIDTH < WIDTH:
        player.x += VEL
    if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_LEFT] and player.x > 0:
        player.x -= VEL
    if keys_pressed[pygame.K_a] and keys_pressed[pygame.K_RIGHT] and player.x + SPACESHIP_WIDTH < WIDTH:
        player.x += VEL

    # Ennemies --------------------------------------------------------------------------------------------------------------
 #ANCHOR ennemy_movement
def ennemy1_movement(ennemy):
    if ennemy['state'] == 1:
        if ennemy['rect'].x > -120:
            ennemy['rect'].x -= ENNEMY1_VEL
        else:
            ennemy['state'] = 2
    elif ennemy['state'] == 2:
        if ennemy['rect'].y < HEIGHT - (ENNEMY_SPACESHIP_HEIGHT + ENNEMY_SPACESHIP_HEIGHT):
            ennemy['rect'].y += ENNEMY1_VEL
        else:
            ennemy['state'] = 3
    elif ennemy['state'] == 3:
        if ennemy['rect'].x < ENNEMY1_START_X_POSITION + 100:
            ennemy['rect'].x += ENNEMY1_VEL
            ennemy['rect'].y -= ENNEMY1_VEL // 2.5
        else:
            ennemy['state'] = 1
            ennemy['rect'].x = ENNEMY1_START_X_POSITION
            ennemy['rect'].y = ENNEMY1_START_Y_POSITION

def ennemy2_movement(ennemy):
    if ennemy['state'] == 1:
        if ennemy['rect'].y > -SPACESHIP_HEIGHT - 10:
            ennemy['rect'].y -= ENNEMY1_VEL
        else:
            ennemy['state'] = 2
    elif ennemy['state'] == 2:
        if ennemy['rect'].x > -50:
            ennemy['rect'].x -= ENNEMY1_VEL
        else:
            ennemy['state'] = 3
    elif ennemy['state'] == 3:
        if ennemy['rect'].x < WIDTH:
            ennemy['rect'].x += ENNEMY1_VEL
            ennemy['rect'].y += ENNEMY1_VEL / 3.5
        else:
            ennemy['state'] = 4
    elif ennemy['state'] == 4:
        if ennemy['rect'].x > -ENNEMY_SPACESHIP_WIDTH - 10:
            ennemy['rect'].x -= ENNEMY1_VEL
        else:
            ennemy['state'] = 5
    elif ennemy['state'] == 5:
        if ennemy['rect'].x < WIDTH:
            ennemy['rect'].x += ENNEMY1_VEL
            ennemy['rect'].y -= ENNEMY1_VEL / 4
        else:
            ennemy['state'] = 1

def ennemy3_movement(ennemy):
    if ennemy['state'] == 1:
        if ennemy['rect'].x > WIDTH / 2:
            ennemy['rect'].x -= ENNEMY1_VEL
            ennemy['rect'].y += ENNEMY1_VEL / 3
        else:
            ennemy['state'] = 2
    elif ennemy['state'] == 2:
        if ennemy['rect'].x > -SPACESHIP_WIDTH:
            ennemy['rect'].x -= ENNEMY1_VEL
            ennemy['rect'].y -= ENNEMY1_VEL / 3 
        else:
            ennemy['state'] = 3
    elif ennemy['state'] == 3:
        if ennemy['rect'].x < WIDTH / 2:
            ennemy['rect'].x += ENNEMY1_VEL
            ennemy['rect'].y += ENNEMY1_VEL / 3
        else:
            ennemy['state'] = 4
    elif ennemy['state'] == 4:
        if ennemy['rect'].x < WIDTH:
            ennemy['rect'].x += ENNEMY1_VEL
            ennemy['rect'].y -= ENNEMY1_VEL / 3
        else:
            ennemy['state'] = 1

def ennemy4_movement(ennemy):
    if ennemy['state'] == 1:
        ennemy['rect'].x              

#ANCHOR spawn_ennemies           
def spawn_ennemies(ennemies):
    for ennemy in ennemies:
        if LEVEL == 1:
            WIN.blit(ennemy_spaceship, (ennemy['rect'].x, ennemy['rect'].y))
        if LEVEL == 2:
            WIN.blit(ennemy2_spaceship, (ennemy['rect'].x, ennemy['rect'].y))
        if LEVEL == 3:
            WIN.blit(ennemy3_spaceship, (ennemy['rect'].x, ennemy['rect'].y))
        if LEVEL == 4:
            WIN.blit(ennemy4_spaceship, (ennemy['rect'].x, ennemy['rect'].y))

def ennemy_shot(ennemy, ennemy_bullets):
    current_time = pygame.time.get_ticks()
    if current_time - ennemy['last_shot_time'] >= ennemy['shot_interval']:
        bullet = pygame.Rect(ennemy['rect'].x + ennemy['rect'].width // 2, ennemy['rect'].y, 8, 24)
        ennemy_bullets.append(bullet)       
        ennemy['last_shot_time'] = current_time
        SOUND_BULLET_SHOT.play()

# General --------------------------------------------------------------------------------------------------------------
def draw_window(player, ennemies, player_bullets, ennemy_bullets, player_health):
    WIN.blit(space, (0,0))

    display_health(player_health)
    score_text = SCORE_FONT.render('SCORE : ' + str(SCORE), 1, WHITE)
    WIN.blit(score_text, (0, 50))

    level_text = SCORE_FONT.render('LEVEL : ' + str(LEVEL), 1, WHITE)
    WIN.blit(level_text, (0, 0))

    WIN.blit(player_spaceship, (player.x, player.y))
    spawn_ennemies(ennemies)

    for bullet in player_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)
    
    for bullet in ennemy_bullets:
        pygame.draw.rect(WIN, WHITE, bullet)

    pygame.display.update()

def handle_bullets(player_bullets, ennemy_bullets, player, ennemies):
    global SCORE
    for bullet in player_bullets:
        bullet.y -= BULLET_VEL
        if bullet.y <= 0:
            player_bullets.remove(bullet)
        for ennemy in ennemies:
            if ennemy['rect'].colliderect(bullet):
                pygame.event.post(pygame.event.Event(ennemy_hit, {'ennemy': ennemy}))  # Passer l'ennemi touché dans l'événement
                SCORE += 10
                if bullet in player_bullets:
                    player_bullets.remove(bullet)

    for bullet in ennemy_bullets:
        bullet.y += ENNEMY_BULLET_VEL
        if player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(player_hit))
            ennemy_bullets.remove(bullet)

def display_health(player_health):
    if player_health == 5:
        WIN.blit(health_5, (0, HEIGHT - 55))
    if player_health == 4:
        WIN.blit(health_4, (0, HEIGHT - 55))
    if player_health == 3:
        WIN.blit(health_3, (0, HEIGHT - 55))
    if player_health == 2:
        WIN.blit(health_2, (0, HEIGHT - 55))
    if player_health == 1:
        WIN.blit(health_1, (0, HEIGHT - 55))

def lose():
     SOUND_PLAYER_LOSE.play()
     draw_text = LOSE_FONT.render('GAME OVER', 1, WHITE)
     WIN.blit(draw_text, (WIDTH / 2 - 450, HEIGHT / 2 - 150))
     pygame.display.update()
     pygame.time.delay(3000)
     pygame.quit()

#   ---------------------------------------------------------------------------------------------------------------
#   ---------------------------------------------------------------------------------------------------------------
#   ---------------------------------------------------------------------------------------------------------------
# Main ---------------------------------------------------------------------------------------------------------------
def main():

    # Global variables
    global LEVEL
    global SCORE
    # variables ================
    player = pygame.Rect(WIDTH // 2 - SPACESHIP_WIDTH // 2, HEIGHT - 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    ennemies = []
    player_bullets = []
    ennemy_bullets = []

    player_health = 5

    clock = pygame.time.Clock()
    run = True
    ennemy_count = 0
    ennemy_interval = 300  # Intervalle en millisecondes
    last_ennemy_time = pygame.time.get_ticks()  # Temps du dernier ennemi apparu
    #===========================

    while run:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()

        #Events : =======================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL or event.key == pygame.K_UP:
                    bullet = pygame.Rect(player.x + player.width//2, player.y, 8, 24)
                    player_bullets.append(bullet)
                    SOUND_BULLET_SHOT.play()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_r:
                    LEVEL = 1
                    SCORE = 0
                    ennemies.clear()
                    ennemy_bullets.clear()
                    player_health = 5
                    
            if event.type == player_hit:
                player_health -= 1
                SOUND_ENNEMY_DIE.play()

            if event.type == ennemy_hit:
                ennemy = event.__dict__.get('ennemy')  # Récupérer l'ennemi touché depuis l'événement
                if ennemy:
                    SOUND_BULLET_HIT.play()
                    ennemies.remove(ennemy)
  # Supprimer l'ennemi de la liste
        #========================================

        # Vérification de l'intervalle pour AFFICHER un nouvel ennemi =================================
        if current_time - last_ennemy_time >= ennemy_interval and ennemy_count < nb_ennemies:
            new_ennemy = {
                'rect': pygame.Rect(ENNEMY1_START_X_POSITION, ENNEMY1_START_Y_POSITION, ENNEMY_SPACESHIP_WIDTH, ENNEMY_SPACESHIP_HEIGHT),
                'state': 1,
                'last_shot_time': current_time,  # Ajouter l'attribut 'last_shot_time'
                'shot_interval': random.randint(1000, 2300),  # Ajouter l'attribut 'shot_interval'
            }
            ennemies.append(new_ennemy)
            ennemy_count += 1
            last_ennemy_time = current_time

        # DEPLACEMENT des ennemis=================================
        #ANCHOR movement_type_select
        if LEVEL == 1:
            for ennemy in ennemies:
                ennemy1_movement(ennemy)
        if LEVEL == 2:
            for ennemy in ennemies:
                ennemy2_movement(ennemy)
        if LEVEL == 3:
            for ennemy in ennemies:
                ennemy3_movement(ennemy)

        # Mouvement du joueur et collisions=================================
        keys_pressed = pygame.key.get_pressed()
        player_handle_movement(keys_pressed, player)
        handle_bullets(player_bullets, ennemy_bullets, player, ennemies)
        #==================================================================
        for ennemy in ennemies:
            ennemy_shot(ennemy, ennemy_bullets)

        #Condition de victoire ========================================
        if player_health == 0:
            lose()
            
        if not ennemies:
            ennemy_count = 0
        
        if LEVEL == SCORE/(nb_ennemies*10):
            LEVEL += 1
        #========================================


        draw_window(player, ennemies, player_bullets, ennemy_bullets, player_health)
    pygame.quit()
    
    

if __name__ == "__main__":
    main()