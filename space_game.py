import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats



def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Sun defenders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    ino = Group()
    controls.create_army(screen, ino)
    stats = Stats()



    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        bullets.update()
        controls.update(bg_color, screen, gun,  ino, bullets)
        controls.update_bullets(screen, ino, bullets)

        controls.update_inos(stats, screen, gun, ino, bullets)
run()
