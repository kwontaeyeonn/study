import pygame
import sys

pygame.init()
width = 480
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("블록 깨기")

block_width = 50
block_height = 20
block_color = (0, 128, 128)
blocks = []

for y_pos in range(100, 200, block_height):
    for x_pos in range(1, width - block_width, block_width):
        blocks.append(pygame.Rect(x_pos, y_pos, block_width, block_height))

ball_color = (255,255,0)
ball_radius = 10
ball_pos = [width//2, height//2]
ball_speed = [5,5]

paddle_width = 80
paddle_height = 20
paddle_color = (255,0,0)
paddle_pos = [width//2, height//2]

ball_pos[0] += ball_speed[0]
ball_pos[1] += ball_speed[1]

if ball_pos[1] < ball_radius:
    ball_speed[1] = -ball_speed[1]
elif ball_pos[1] > height - ball_radius:
    pygame.quit()
    sys.exit()
if ball_pos[0] < ball_radius or ball_pos[0] > width - ball_radius:
    ball_speed[0] = -ball_speed[0]
for block in blocks:
    if block.collidepoint(ball_pos):
        blocks.remove(block)
        ball_speed[1] = -ball_speed[1]

paddle_pos[0] = pygame.mouse.get_pos()[0]
paddle_pos[0] = max(paddle_pos[0], paddle_width//2)
paddle_pos[0] = min(paddle_pos[0], width - paddle_width//2)

if ball_pos[1] > height - ball_radius - paddle_height:
    if abs(ball_pos[0] - paddle_pos[0] < paddle_width//2):
        ball_speed[1] = -ball_speed[1]

screen.fill((255,25,255))
for block in blocks:
    pygame.draw.rect(screen, block_color, block)

pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
paddle_rect = pygame.Recxt(paddle_pos[0] - paddle_width//2, height - paddle_height*2, paddle_width, paddle_height,)
pygame.draw.rect(screen, paddle_color, paddle_rect)
pygame.display.update()