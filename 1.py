import pygame, sys, os

def load_image(name, colorkey=-1):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Car(pygame.sprite.Sprite):
    image = load_image('game_over.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = -650
        self.rect.y = 0
        self.size = (600, 300)
        self.speed = 1

    def update(self, *args):
        if self.rect.x < width - self.size[0]:
            self.rect.x += self.speed


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    all_sprites = pygame.sprite.Group()
    Car(all_sprites)
    # размеры окна:
    try:
        size = width, height = (600, 300)
    except ValueError:
        print('Неправильный формат ввода')
        exit(-1)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 200
    running = True
    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()





