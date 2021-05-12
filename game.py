import pygame as pg
from random import randrange


try:
    pg.init()
except:
    print('Não foi possivel iniciar o PyGame.')


def game():
    playing = True
    game_over = False

    #criando tela do jogo
    largura = 320
    altura = 280
    surface = pg.display.set_mode((largura, altura))
    pg.display.set_caption('Snake')
    placar = 20
    pontuacao = 0


    #posicai inicial cobra
    pixel = 10
    xs = randrange(0, largura, 10)
    ys = randrange(0, altura, 10)
    body_size = 1
    snake_body = []
    velocidade_x = pixel
    velocidade_y = 0
    relogio = pg.time.Clock()
    tick = 7

    def text(msg, color, tam, x, y):
        font = pg.font.SysFont(None, tam)
        txt_1 = font.render(msg, True, color)
        surface.blit(txt_1, [x, y])

    #posição da fruta
    xf = randrange(0, largura, 10)
    yf = randrange(0, altura, 10)
    fruit = []

    def draw_snake(color, s):
        for c in s:
            pg.draw.rect(surface, color, (c[0], c[1], pixel, pixel), border_radius=2)

    def draw_fruit(color, f):
        pg.draw.rect(surface, color, (f[0], f[1], pixel, pixel), border_radius=10)

    def draw_placar():
        pg.draw.rect(surface, (255, 255, 255), [0, 0, largura, placar])

    while playing:
        while game_over:
            surface.fill((0, 0, 0))
            text('GAME OVER!!! PRESS C TO CONTINUE.', (255, 0, 0), 18, 50, 100)
            pg.draw.rect(surface, (255, 255, 255), [118, 125, 90, 20])
            text(f'POINTS: {pontuacao}', (0, 0, 0), 15, 130, 130)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False
                    game_over = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_c:
                        game()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT and velocidade_x != pixel:
                    velocidade_y = 0
                    velocidade_x = -pixel
                if event.key == pg.K_RIGHT and velocidade_x != -pixel:
                    velocidade_y = 0
                    velocidade_x = pixel
                if event.key == pg.K_UP and velocidade_y != pixel:
                    velocidade_x = 0
                    velocidade_y = -pixel
                if event.key == pg.K_DOWN and velocidade_y != -pixel:
                    velocidade_x = 0
                    velocidade_y = pixel

        surface.fill((0, 0, 0))
        xs += velocidade_x
        ys += velocidade_y

        snake_head = []
        fruit.append(xf)
        fruit.append(yf)
        snake_head.append(xs)
        snake_head.append(ys)
        snake_body.append(snake_head)

        if xs == fruit[0] and ys == fruit[1]:
            fruit[0] = randrange(0, largura, 10)
            fruit[1] = randrange(50, altura, 10)
            body_size += 1
            tick += .25

        if snake_head[0] > largura-pixel:
            game_over = True
        elif snake_head[0] < 0:
            game_over = True
        if snake_head[1] > altura-pixel:
            game_over = True
        elif snake_head[1] < placar:
            game_over = True


        if len(snake_body) > body_size:
            del snake_body[0]
        if any(block == snake_head for block in snake_body[:-1]):
            game_over = True

        draw_placar()
        text(f'Pontuação: {pontuacao}', (255, 0, 0), 15, 10, 5)
        draw_snake((184, 134, 11), snake_body)
        if any(block != fruit for block in snake_body):
            draw_fruit((148, 0, 211), fruit)

        pontuacao += 2
        relogio.tick(tick)
        pg.display.update()

game()
pg.quit()
