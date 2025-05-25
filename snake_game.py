import pygame
import sys
import random

# 초기화
pygame.init()

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 뱀 크기
SNAKE_SIZE = 10

# 위치
snake_x = SCREEN_WIDTH // 2
snake_y = SCREEN_HEIGHT // 2

# 속도
snake_dx = 10
snake_dy = 0

# 음식 위치
food_x = random.randint(0, SCREEN_WIDTH - SNAKE_SIZE)
food_y = random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE)

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# 시계 설정
clock = pygame.time.Clock()

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 방향키 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -10
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = 10
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -10
            elif event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = 10

    # 뱀 이동
    snake_x += snake_dx
    snake_y += snake_dy

    # 화면 초기화
    screen.fill(BLACK)

    # 뱀과 음식 그리기
    pygame.draw.rect(screen, WHITE, [snake_x, snake_y, SNAKE_SIZE, SNAKE_SIZE])
    pygame.draw.rect(screen, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

    pygame.display.update()

    # 프레임 속도 (게임 속도)
    clock.tick(10)
