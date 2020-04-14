import Tpg
import Opg
import pygame
def hp():
    pygame.init()
    pygame.display.set_caption("pong-Home Page")
    screen = pygame.display.set_mode([800,600])
    pygame.init()
    pygame.display.flip()
    keepgoing = True
    BACKGROUND = pygame.image.load("image.png").convert()
    screen.blit(BACKGROUND, (0,0))
    LOGO = pygame.image.load("q.jpg")
    pygame.display.set_icon(LOGO)
    mousedown = False
    WHITE = (255, 255, 255)
    fonto = pygame.font.SysFont("Times", 100)
    fontt = pygame.font.SysFont("Times", 30)
    draw_stringo = "PONG"
    draw_stringt = "Sing game"
    draw_stringe = "Doudle game"
    texto = fonto.render(draw_stringo, True, WHITE)
    textt = fontt.render(draw_stringt, True, WHITE)
    texte = fontt.render(draw_stringe, True, WHITE)
    texto_recto = texto.get_rect()
    textt_rectt = textt.get_rect()
    texte_recte = texte.get_rect()
    texto_recto.centerx = screen.get_rect().centerx
    textt_rectt.centerx = screen.get_rect().centerx
    texte_recte.centerx = screen.get_rect().centerx
    texto_recto.y = 10
    textt_rectt.y = 200
    texte_recte.y = 400
    screen.blit(texto, texto_recto)
    screen.blit(textt, textt_rectt)
    screen.blit(texte, texte_recte)
    pygame.display.update()
    while keepgoing:
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepgoing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousedown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False
        if mousedown:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if y >= 200 and y <= 230:
                if x <= 460 and x >= 340:
                    Opg.dryx()
            if y > 320 and y < 480:
                if x <= 480 and x >= 320:
                    Tpg.sryx()
   
    pygame.quit()
hp()
                                


