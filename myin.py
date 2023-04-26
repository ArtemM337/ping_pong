from pygame import*
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))





class Player(GameSprite):
    def update(self):
        # TODO Написати управління гравцем для руху в сторони (ширина гравця 80 px)
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x = self.rect.x - self.speed
        if keys[K_RIGHT] and self.rect.x < width - 85:
            self.rect.x = self.rect.x + self.speed


class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y > height:
            self.rect.y = 0
            self.rect.x = randint(0, width-85)
            lost = lost + 1


img_player = "raketka.png"
img_back = "fon.png"
img_pon = "pon.jpg"


width, height = 700, 500
window = display.set_mode((width, height))
display.set_caption("Shooter")
background = transform.scale(image.load(img_back), (width, height))

player = Player(img_player, 250, height-100, 80, 100, 10)
finish = False
pon = Enemy(img_pon, 50, height-100, 40, 50, 5)


clock = time.Clock()
FPS = 60
lost = 3

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if not finish:
        window.blit(background, (0, 0))
        player.update()
        player.reset()
        pon.update()
        pon.reset()

    display.update()
    clock.tick(FPS)