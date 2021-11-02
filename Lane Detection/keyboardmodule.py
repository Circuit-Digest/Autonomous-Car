import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))

def getKey(keyName):
    ans= False
    running = True
    for event in pygame.event.get():  # error is here
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    if running:
        pygame.display.flip()

    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey('LEFT'):
        print('LEFT')
    if getKey('RIGHT'):
        print('RIGHT')
    if getKey('q'):
        pygame.quit()


if __name__ == '__main__':
    init()
    while True:
        main()