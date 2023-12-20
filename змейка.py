import pygame, random, pyttsx3
qqqq = pyttsx3.init()
eqqr = qqqq.getProperty('voices')
qq = qqqq.getProperty('rate')
qqqq.setProperty('rate', qq+40)
for ww in eqqr:
    if ww.name == 'Aleksandr':
        qqqq.setProperty('voice', ww.id)
qqqq.say('Если вы врежитесь сами в себя, то игра закончится. А если вы врежитесь в стенку, то пройдёте на другую сторону.')
qqqq.runAndWait()

pygame.init()


disp = pygame.display.set_mode((500, 400))
pygame.display.update()
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()
len_snake = 1
snake_list = []


b = (0, 0, 255)
r = (255, 0, 0)
fon = (165, 138, 243)
f = (35, 255, 23)
ff = (255, 255, 22)


y, x = 300, 300
x_c, y_c = 0, 0
fx = round(random.randrange(0, 490)/10)*10
fy = round(random.randrange(0, 390)/10)*10
qqqwwweee = 0
qqqqqqqqq = (111, 111, 111)
wwwwwwwww = pygame.font.SysFont("cosmeticians", 30)


def body(xxx, yyy):
    for cc in yyy:
        pygame.draw.rect(disp, b, [cc[0], cc[1], xxx, xxx])


def score(alexey):
    a = wwwwwwwww.render('очки: '+str(alexey), True, qqqqqqqqq)
    disp.blit(a, [0, 0])


go = False
while not go:
    for q in pygame.event.get():
        if q.type == pygame.QUIT:
            go = True
        if q.type == pygame.KEYDOWN:
            if q.key == pygame.K_LEFT:
                x_c = -10
                y_c = 0
            if q.key == pygame.K_RIGHT:
                x_c = 10
                y_c = 0
            if q.key == pygame.K_UP:
                x_c = 0
                y_c = -10
            if q.key == pygame.K_DOWN:
                x_c = 0
                y_c = 10
    x += x_c
    y += y_c
    disp.fill(fon)
    x %= 500
    y %= 400
    pygame.draw.rect(disp, b, [x, y, 10, 10])
    s_h = []
    s_h.append(x)
    s_h.append(y)
    snake_list.append(s_h)
    if len_snake < len(snake_list):
        del snake_list[0]
    for qqqwwweeerrrtttyyyuuuiiioooppp in snake_list[:-1]:
        if qqqwwweeerrrtttyyyuuuiiioooppp == s_h:
            go = True
    body(10, snake_list)
    if qqqwwweee == 9:
        pygame.draw.rect(disp, ff, [fx, fy, 10, 10])
    else:
        pygame.draw.rect(disp, f, [fx, fy, 10, 10])
    score(len_snake - 1)
    pygame.display.update()
    if x == fx and y == fy:
        fx = round(random.randrange(0, 490) / 10) * 10
        fy = round(random.randrange(0, 390) / 10) * 10
        if qqqwwweee == 9:
            len_snake += 10
            qqqwwweee = 0
        else:
            len_snake += 1
        qqqwwweee += 1
    clock.tick(5)
pygame.quit()
quit()
