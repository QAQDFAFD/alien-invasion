import sys
import pygame
from setting import Setting
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        self.setting = Setting()
        pygame.init()
        # self 上面设置了一个 screen ，给定了大小
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.bg_color = self.setting.bg_color
        pygame.display.set_caption(self.setting.caption)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            # 用于飞船的移动
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))

    def _check_events(self):
        # 响应按键和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    # 更新屏幕
    def _update_screen(self):
        # 设置背景颜色，每次都会重新配置
        self.screen.fill(self.bg_color)

        # 绘制飞船
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.setting.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
