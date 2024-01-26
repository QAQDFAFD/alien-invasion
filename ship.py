import pygame

class Ship:
    # 这里的 ai_game 是游戏的实例
    def __init__(self, ai_game):
        # 初始化飞船、设置其位置
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting

        # 加载飞船图像，并且获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.image = pygame.transform.scale(self.image,
                                            (100, int(self.image.get_height() * 100 / self.image.get_width())))
        self.rect = self.image.get_rect()

        # 对于每一艘飞船都放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    # 移动飞船的位置
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.speed
        self.rect.x = self.x
