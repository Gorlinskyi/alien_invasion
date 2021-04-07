class Settings:
    """
    Класс для хранения всех настроек игры Инопланетное вторжение
    """

    def __init__(self):
        """
        Инициализирует настройки игры
        """

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # настройки корабля
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # параметры пуль
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 128, 255
        self.bullet_allowed = 3

        # настройки пришельцев
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево
        self.fleet_direction = 1