from pygame import*



img_back = "fon.png"

width, height = 700, 500
window = display.set_mode((width, height))
display.set_caption("Shooter")
background = transform.scale(image.load(img_back), (width, height))

finish = False



clock = time.Clock()
FPS = 60


game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if not finish:
        window.blit(background, (0, 0))


    display.update()
    clock.tick(FPS)