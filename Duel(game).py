import pygame

pygame.init()
win = pygame.display.set_mode((900, 600))

clock = pygame.time.Clock()
START = True
END = False
run = True
SCORE = '0'

pygame.display.set_caption("Duel")
cloud = pygame.image.load('sprites/cloud.png')
opponent = pygame.image.load('sprites/opponent.png')
picture = pygame.image.load('sprites/start.jpg')

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
end = pygame.image.load('sprites/end.jpg')


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


class BULLET():
    def __init__(self, x, y,  rad):
        self.x = x
        self.y = y
        self.rad = rad
        self.speed = 10

    def draw(self):
        pygame.draw.circle(win, (0, 0, 0),  (self.x, self.y), self.rad)


bulet = BULLET(round(700), round(360), 5)


def shooting():
    global SCORE
    if bulet.x > 0:
        bulet.draw()
    else:
        SCORE = str(int(SCORE)+1)
        bulet.x = 700
        bulet.y = 360



def draw():
    global anim
    global START
    global run

    win.blit(bg, (0, 0))
    win.blit(cloud, (50, 400))
    win.blit(cloud, (550, 400))
    shooting()
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
    font = pygame.font.Font(None, 50)
    text = font.render("SCORE : " + SCORE, 1, (255, 255, 255))
    win.blit(text, (370, 150))
    if START:
        win.blit(picture, (0, 0))
    if END:
        win.blit(end, (0, 0))
        run = False
    pygame.display.update()


while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bulet.x -= bulet.speed
    if SCORE == '10':
        bulet.speed = 20
    elif SCORE == '20':
        bulet.speed = 25
    elif SCORE == '30':
        bulet.speed = 30
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
    if x < bulet.x < x + width and y < bulet.y < y + height:
        END = True
    if START:
        pygame.time.delay(5000)
        START = False
pygame.quit()
