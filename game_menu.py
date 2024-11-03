def menu_principal():
    import pygame
    import sys
    import os
    import time

    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    pygame.display.set_caption("Jogo de Montar Palavras")

    ALICE_BLUE = (240, 248, 255)
    NAVY = (0, 0, 128)
    WHITE = (255, 255, 255)
    STEEL_BLUE = (70, 130, 180)
    CADET_BLUE = (95, 158, 160)
    LIGHT_PINK = (255, 200, 255)
    BLACK = (0, 0, 0)
    ORANGE = (215, 115, 30)
    PURPLE = (135, 91, 121)
    CIAN = (101, 155, 164)

    font = pygame.font.Font("./fontes/Copyduck.ttf", 74)
    small_font = pygame.font.Font("./fontes/Copyduck.ttf", 60)
    big_font = pygame.font.Font("./fontes/Copyduck.ttf", 90)

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)

    def draw_loading_screen():
        background = pygame.image.load(os.path.join('./imagens/bg_inst.png'))
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(background, (0, 0))
        big_font = pygame.font.Font("./fontes/Copyduck.ttf", 90)
        draw_text('Regras', big_font, NAVY, screen, SCREEN_WIDTH // 2, 100)
        draw_text('1. Use os blocos para completar as palavras.', small_font, BLACK, screen, SCREEN_WIDTH // 2, 250)
        draw_text('2. Seus pontos aumentam quando escolhe a letra certa.', small_font, BLACK, screen, SCREEN_WIDTH // 2, 350)
        draw_text('3. Se atente com o tempo!!.', small_font, BLACK, screen, SCREEN_WIDTH // 2, 450)
        text = big_font.render("Carregando...", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//1.5))
        screen.blit(text, text_rect)
        pygame.display.flip()

    def load_resources():
        for i in range(10):
            time.sleep(0.5)
            draw_loading_screen()

    def main_menu():
        click = False
        background = pygame.image.load(os.path.join('./imagens/background_menu.jpg'))
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        while True:
            screen.blit(background, (0, 0))
            mx, my = pygame.mouse.get_pos()
            button_1 = pygame.Rect((SCREEN_WIDTH/2-150), (SCREEN_HEIGHT/1.6-40), 400, 90)
            button_2 = pygame.Rect((SCREEN_WIDTH/2-150), button_1.bottom + 20, 400, 90)
            button_3 = pygame.Rect((SCREEN_WIDTH/2-150), button_2.bottom + 20, 400, 90)

            if button_1.collidepoint((mx, my)):
                if click:
                    game()
            if button_2.collidepoint((mx, my)):
                if click:
                    instructions()
            if button_3.collidepoint((mx, my)):
                if click:
                    pygame.quit()
                    sys.exit()

            pygame.draw.rect(screen, CIAN if button_1.collidepoint((mx, my)) else PURPLE, button_1)
            pygame.draw.rect(screen, CIAN if button_2.collidepoint((mx, my)) else PURPLE, button_2)
            pygame.draw.rect(screen, CIAN if button_3.collidepoint((mx, my)) else PURPLE, button_3)

            draw_text('Iniciar', font, BLACK, screen, button_1.centerx, button_1.centery)
            draw_text('Regras', font, BLACK, screen, button_2.centerx, button_2.centery)
            draw_text('Sair', font, BLACK, screen, button_3.centerx, button_3.centery)

            logo_titulo = pygame.image.load("./imagens/logo-integrador.png")
            logo_width = SCREEN_WIDTH/1.2
            logo_height = SCREEN_HEIGHT/3
            res_logo = pygame.transform.scale(logo_titulo, (logo_width, logo_height))
            screen.blit(res_logo, (SCREEN_WIDTH/2-(logo_width/2), 80))

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()

    def game():
        load_resources()
        import game_logica as GL
        GL.main()

    def instructions():
        click = False
        running = True
        while running:
            background = pygame.image.load(os.path.join('./imagens/bg_inst.png'))
            background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(background, (0, 0))
            draw_text('Regras', font, NAVY, screen, SCREEN_WIDTH // 2, 100)
            draw_text('1. Use os blocos para completar as palavras.', small_font, BLACK, screen, SCREEN_WIDTH // 2, 250)
            draw_text('2. Seus pontos aumentam quando escolhe a letra certa.', small_font, BLACK, screen, SCREEN_WIDTH // 2, 350)
            draw_text('3. Se atente com os blocos!!.', small_font, BLACK, screen, SCREEN_WIDTH // 2, 450)
            mx, my = pygame.mouse.get_pos()
            button_back = pygame.Rect((SCREEN_WIDTH/2-150), (SCREEN_HEIGHT/1.6-40), 400, 90)

            if button_back.collidepoint((mx, my)):
                if click:
                    running = False

            pygame.draw.rect(screen, CIAN if button_back.collidepoint((mx, my)) else PURPLE, button_back)
            draw_text('Voltar', small_font, WHITE, screen, button_back.centerx, button_back.centery)

            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()

    if __name__ == "__main__":
        main_menu()

menu_principal()

