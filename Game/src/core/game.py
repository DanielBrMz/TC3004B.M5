import pygame
import random

from builder.director import EnemyDirector
from builder.enemy_builder import EnemyBuilder
from core.config import Config
from entities.player import Player
from utils.check_collision import check_collision

pygame.init()

# Configuration
config = Config()
WIDTH, HEIGHT = config.get("WIDTH"), config.get("HEIGHT")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

#Jugador
player = Player(WIDTH//2 , HEIGHT - 80)

# Enemies
director = EnemyDirector()
builder = EnemyBuilder()

enemies = [
    director.construct_enemy(builder,"normal"),
    director.construct_enemy(builder, "fast"),
    director.construct_enemy(builder, "strong"),

]

bullets=[]
enemy_speed = 1
enemy_spawn_timer = 0

running = True

while running:
    pygame.time.delay(30)
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    player.move(keys, WIDTH)
    
    #Balas
    if keys[pygame.K_SPACE]:
        bullet.append(player.shoot())
        
    for bullet in bullets[:]:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)

    #Enemigos
    for enemy in enemies:
        enemy.move()

        if check_collision(player, enemy):
            running = False
    

    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if check_collision(bullet, enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    enemy_spawn_timer += 1
    enemy_types = ["normal", "fast", "strong"]

    if enemy_spawn_timer >= 100:
        random_enemy_type= random.choice(enemy_types)

        enemies.append(director.construct_enemy(builder, random_enemy_type))
        enemy_spawn_timer = 0
    
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    
    pygame.display.update()

pygame.quit()