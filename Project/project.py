import pygame

# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (700,500)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
game_over = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

class Block(pygame.sprite.Sprite):
# Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref, life):
# Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.life = life
        #self.dying = dying

class Chaser(pygame.sprite.Sprite):
# Define the constructor for invader
    def __init__(self, face, width, height, x_ref, y_ref, speed):
# Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.face = face
        self.image = pygame.image.load(self.face).convert()
        self.image = pygame.transform.scale(self.image, (width,height))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = speed

        def update(self):
            self.rect.x = self.rect.x + self.speed
            
class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x_ref, y_ref, speed, jump, gravity):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = speed
        self.jump = jump
        self.gravity = gravity
        

    def update(self):
        #self.rect.x += self.speed    ##causes constanr movement
        self.rect.y += self.gravity

    def horizontal(self, val):
        self.speed = val
        self.rect.x += self.speed

    def vertical(self,val):
        self.jump = val
        self.rect.y = self.rect.y + self.jump


all_sprites_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
crumbling_list = pygame.sprite.Group()

block1 = Block(WHITE, 210, 30, 0, 270, 0)
block_list.add(block1)
all_sprites_list.add(block1)
crumbling_block = Block(WHITE, 90, 30, 270, 210, 180)
crumbling_list.add(crumbling_block)
all_sprites_list.add(crumbling_block)
lava = Block(RED, 700, 30, 0, 470, 0)
block_list.add(lava)
all_sprites_list.add(lava)

player = Player(30, 30, BLUE, 60, 240, 0, 0, 1)
all_sprites_list.add(player)
        
hades = "HADES.png"

dying = False
# -- Game Loop
while not game_over:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        #End If
    #Next event
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.horizontal(1)
        #pacman.vertical(0)
    if keys[pygame.K_LEFT]:
        player.horizontal(-1)
        #pacman.vertical(0)
    if keys[pygame.K_SPACE]:
        player.vertical(-5)
        #pacman.horizontal(0)
   # if keys[pygame.K_DOWN]
    #    pacman.vertical(1)
     #   pacman.horizontal(0)
 
    contact_list = pygame.sprite.spritecollide(player, block_list, False)
    break_list = pygame.sprite.spritecollide(player, crumbling_list, False)

    for x in contact_list:
        player.vertical(-1)

    for x in break_list:
        player.vertical(-1)
        crumbling_block.life = crumbling_block.life - 1
        if crumbling_block.life < 0:
            all_sprites_list.remove(crumbling_block)
            all_sprites_list.update()
        
    if player.rect.y > 470:
        pygame.wait(1000)
        pygame.quit()
        
        
    all_sprites_list.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)
    
    # -- Draw here
    all_sprites_list.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # -- The clock ticks over
    clock.tick(60)
    
#End While - End of game loop
pygame.quit()     
      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
