import pygame

pygame.init()
win = pygame.display.set_mode((900, 600))

clock = pygame.time.Clock()

pygame.display.set_caption("Duel")
cloud = pygame.image.load('sprites/cloud.png')

opponent = pygame.image.load('sprites/opponent.png')

walkRight = [pygame.image.load('sprites/anim_r_1.png'),
             pygame.image.load('sprites/anim_r_2.png'),
             pygame.image.load('sprites/anim_r_3.png'),
             pygame.image.load('sprites/anim_r_4.png'),
             pygame.image.load('sprites/anim_r_5.png'),
             pygame.image.load('sprites/anim_r_6.png'),
             ]

walkLeft = [pygame.image.load('sprites/anim_l_1.png'),
            pygame.image.load('sprites/anim_l_2.png'),
            pygame.image.load('sprites/anim_l_3.png'),
            pygame.image.load('sprites/anim_l_5.png'),
            pygame.image.load('sprites/anim_l_4.png'),
            pygame.image.load('sprites/anim_l_6.png'),
            ]

bg = pygame.image.load('sprites/bg.jpg')
playerStand = pygame.image.load('sprites/anim_stay.png')

x = 50
y = 252
width = 150
height = 200
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
anim = 0

def draw():
    global anim
    win.blit(bg, (0, 0))
    win.blit(cloud, (50, 400))
    win.blit(cloud, (550, 400))
    win.blit(opponent, (700, 305))
    if anim + 1 > 30:
        anim = 0
    if left:
        win.blit(walkLeft[anim // 5], (x, y))
        anim += 1
    elif right:
        win.blit(walkRight[anim // 5], (x, y))
        anim += 1
    else:
        win.blit(playerStand, (x, y))

    pygame.display.update()


run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 30 and keys[pygame.K_RIGHT] == 0:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 400 - width:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    draw()
pygame.quit()
