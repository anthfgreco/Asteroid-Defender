import pygame, random

# Define some colors
WHITE = (255, 255, 255)
BLACK = (  0,  0,    0)
GREY  = (     0x7A797B)
RED   = (     0xAC1212)
GREEN = (     0x5AC52B)

# Initialize Pygame library
pygame.init()

# Create a 800x800 screen
screen = pygame.display.set_mode([800, 800])

# This sets the name of the window
pygame.display.set_caption('Asteroid Defender')

clock = pygame.time.Clock()

# Set background position
background_position = [0, 0]

# Set all image url's, sound url's, asteroid position list, laser position
background_image = pygame.image.load("space.png").convert()
player_image = pygame.image.load("spaceShips_006.png")
player_image.set_colorkey(BLACK)
asteroid = pygame.image.load("asteroid.png")
asteroid_list = []

for i in range(25):
    xx = random.randrange(0, 750)
    yy = random.randrange(1000, 1800)
    asteroid_list.append([xx, yy])

click_sound = pygame.mixer.Sound("laser5.ogg")
hit_sound = pygame.mixer.Sound("collisionsound.ogg")
laser_position = (1000, 1000)

def drawLaser(screen, x, y):
    pygame.draw.rect(screen,RED,[x, y,5,42],0)
    
y_Laser_Change = 0
pygame.mixer.music.load('techno.ogg')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

done = False
pygame.mouse.set_visible(False)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True # Quits program if user clicks exit
        elif event.type == pygame.constants.USEREVENT:
            pygame.mixer.music.play() # Continues loop of background music
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play() # Plays laser sound
            laser_position = pygame.mouse.get_pos() # Gets position of mouse when button is clicked
            y_Laser_Change = 0 # Changes speed of laser to 0 if a laser already exists

    # Set background image
    screen.blit(background_image, background_position)

    # Set x and y coordinates for mouse position
    player_position = pygame.mouse.get_pos()
    x_Player = player_position[0]
    y_Player = player_position[1]

    # Sets laser speed, draws laser where button was pressed
    y_Laser_Change += 40
    drawLaser(screen, laser_position[0] - 3, laser_position[1] + y_Laser_Change)

    # Draw player image
    screen.blit(player_image, [x_Player-25, y_Player-20.5])

    # Draw random asteroids
    for i in range(len(asteroid_list)):
        screen.blit(asteroid, asteroid_list[i])

        # Move each asteroid up 9 pixels
        asteroid_list[i][1] -= 9

        # Checks if player is colliding with an asteroid, plays collision sound if True
        if x_Player >= asteroid_list[i][0] and x_Player  <= asteroid_list[i][0] + 85 and y_Player >= asteroid_list[i][1] and y_Player <= asteroid_list[i][1] + 72:
            hit_sound.play()

        # Resets asteroid when past the top of screen
        if asteroid_list[i][1] < -50:
            # Reset to bottom
            y = random.randrange(800, 870)
            asteroid_list[i][1] = y
            # Reset to a random x coordinate
            x = random.randrange(-40, 785)
            asteroid_list[i][0] = x

    pygame.display.flip()

    clock.tick(75)

pygame.quit()