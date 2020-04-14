import pygame
import home_page
def sryx():
    pygame.init()
    screen = pygame.display.set_mode([800,600])
    pygame.display.set_caption("pong-double game")
    keepgoing = True
    lukeydown = False
    rukeydown = False
    ldkeydown = False
    rdkeydown = False
    picx = 400
    picy = 300
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    timer = pygame.time.Clock()
    speedx = 2.5
    speedy = 2.5
    paddleh = 200
    paddlew = 25
    paddolex = 25
    paddoley = 150
    pic = pygame.image.load("cd.bmp")
    paddtlex = 750
    paddtley = 150
    qx = 400
    qy = 300
    swsfso = 0
    fso = 0
    fst = 0
    picw = 10
    LOGO = pygame.image.load("q.jpg")
    oh = pygame.image.load("cdd.bmp")
    pygame.display.set_icon(LOGO)
    pich = 10
    font = pygame.font.SysFont("Times", 72)
    while keepgoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepgoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    paddtley -= 5
                if event.key == pygame.K_DOWN:
                    paddtley += 5
                if event.key == pygame.K_w:
                    paddoley -= 5
                if event.key == pygame.K_s:
                    paddoley += 5
        qx += speedx

        qy += speedy

        if qx <= 0:
            fst += 1
            speedx = -speedx
        if qx >= 800:
            fso += 1
            speedx = -speedx
        if qy <= 0 or qy + pic.get_width() >= 600:
        
            speedy = -speedy
        if qx + pich >= 750 and qx + pich <= paddtlex + paddleh\
           and speedx > 0:
  
            if qx + picw/2 >= paddtley and qy + picw/2 <= paddtley + \
               paddleh:
        
                speedx = -speedx


            

        if qx <= 50:

   
            if qy >= paddoley and qy <= paddoley + 200:
          
                speedx = -speedx

        screen.fill(BLACK)
        screen.blit(pic, (qx, qy))
        screen.blit(oh, (400,0))

        pygame.draw.rect(screen, WHITE, (paddolex, paddoley, paddlew, paddleh))
        pygame.draw.rect(screen, WHITE, (paddtlex, paddtley, paddlew, paddleh))
        timer.tick(60)
        draw_string = str(fso) + "               " + str(fst)
        text = font.render(draw_string, True, WHITE)
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.y = 10
        screen.blit(text, text_rect)
        pygame.display.update()
    home_page.hp()
    pygame.quit()



    
    
