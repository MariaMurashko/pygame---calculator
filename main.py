import pygame
import button

pygame.init()

bounds = (360, 640)
screen = pygame.display.set_mode(bounds)

pygame.display.set_caption('Calculator')
clock = pygame.time.Clock()

buttons = ['0', ',', '=', '1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', 'x', 'AC', '+/-', '%', '÷']
buttonsObjects = []

mainText = ''

operatorA = 0
operatorB = 0
operand = ''
result = 0


def draw_text( screen, bounds, text):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, 65)
    text_image = font.render(text, True, '#FFFFFF')
    text_rect = text_image.get_rect()
    text_rect.right = bounds[0] - 15
    text_rect.top = bounds[1] - 575
    screen.blit(text_image, text_rect)


i = 1
height = 90
width = 360
for btn in buttons:
    if i % 4 == 0:
        height += 90
        width = 360
buttonsObjects.append(
    buttons.Button('#000000', '#696969', btn, 180 if i == 1 else 90, 90, bounds, bounds[0] - width, bounds[1] - height))

run = True
while run:
    clock.tick(60)

    isCliked = False
    for event in pygame.event.get():
        if event.type == pygame QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            isClicked = False
        if event.type == pygame.MOUSEBUTTONUP:
            isClicked = True

    screen.fill('#000000')
    for btn in buttonsObjects:
        btn.draw(screen, isClicked)


    pygame.display.flip()

pygame.quit()
