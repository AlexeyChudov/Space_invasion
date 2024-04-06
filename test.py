import pygame


def game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    run = True
    color = (255, 100, 255)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                print(event.key)
        screen.fill(color)
        pygame.display.flip()


game()
