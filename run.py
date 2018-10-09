import sys
import pygame
from time import sleep
from time import localtime
from gpiozero import MotionSensor, LED
from signal import pause
WHITE = (255, 255, 255)


def main():
    pygame.init()
    size = [1000, 1000]
    screen = pygame.display.set_mode(size)
    screen.fill(WHITE)
    pygame.display.update()
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Welcome to the Coder School")
    clock = pygame.time.Clock()
    
    ##########Image to display here##############
    image_orig = pygame.image.load('CoderSchoolLogo.png').convert()
    #############################################
    image = image_orig.copy()
    image_rect = image_orig.get_rect(center=screen_rect.center)
    angle = 0
    done = False
    toggle = 0
    
    #############GPIO PIN######################
    pir = MotionSensor(4)
    ###########################################
    
    #############Music File To Play###########
    pygame.mixer.music.load('welcome.wav')
    ##########################################
    play = 0
    wait = 0    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                # if the 'space' key is pressed
                if event.key == pygame.K_SPACE:
                    if toggle == 0:
                        pygame.display.quit()
                        pygame.display.init()
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        screen.fill(WHITE)
                        pygame.display.update()
                        surface = pygame.display.get_surface()
                        x = surface.get_width()/2
                        image_rect.centerx = x

                        
                        toggle = 1
                    elif toggle == 1:
                        pygame.display.quit()
                        pygame.display.init()
                        
                        screen = pygame.display.set_mode((1200, 1200), pygame.RESIZABLE)
                        screen.fill(WHITE)
                        pygame.display.update()
                        surface = pygame.display.get_surface()
                        x = surface.get_width()/2
                        image_rect.centerx = x

                        toggle = 0
        if pygame.mixer.music.get_busy() != True:
            angle=0
            image = pygame.transform.rotate(image_orig, angle)
            image_rect = image.get_rect(center=image_rect.center)
            screen.blit(image, image_rect)
            pygame.display.flip()
            if wait == 1:
                sleep(30)
                wait = 0
            if wait == 0:    
                if pir.motion_detected:
                    pygame.mixer.music.play()
                    print('Coder Detected. Greeting Coder.')
                    print('Warning: Human decisions are removed from strategic defense. Skynet begins to learn at a geometric rate. It becomes self-aware at 2:14 a.m. Eastern time, August 29th.')
                
                
        if pygame.mixer.music.get_busy() == True:
            image = pygame.transform.rotate(image_orig, angle)
            angle+=2.25
            wait = 1
            
        
        
        image_rect = image.get_rect(center=image_rect.center)
        screen.blit(image, image_rect)
        pygame.display.flip()
        clock.tick(60)
        

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()