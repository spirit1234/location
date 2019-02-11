# -*- coding:utf-8 -*-
import sys
import pygame
from bullet import Bullet


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    # 键盘按下事件
    if event.key == pygame.K_d:
        # 飞船向右移动
        ship.moving_right = True

    elif event.key == pygame.K_a:
        # 飞船向左移动
        ship.moving_left = True

    elif event.key == pygame.K_w:
        # 飞船向上移动
        ship.moving_up = True

    elif event.key == pygame.K_s:
        # 飞船向下移动
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 按空格键发射子弹
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_event(event, ship):
    # 键盘抬起事件
    if event.key == pygame.K_d:
        ship.moving_right = False

    elif event.key == pygame.K_a:
        ship.moving_left = False

    elif event.key == pygame.K_w:
        ship.moving_up = False

    elif event.key == pygame.K_s:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    # 监视键盘鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # 绘制屏幕可见
    pygame.display.flip()


def update_bullet(bullets):
    bullets.update()
    # 在子弹到达顶端时移出消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
