import os

class Gamestats():
    """Статистика игры"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.filename = 'absolute_record.txt'
        self.high_score = 0
        self.check_record()
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует изменяющуся во время игры статистику"""
        self.ships_left = self.ai_settings.ship_limit
        self.game_active = False
        self.score = 0
        self.level = 1

    def update_absolute_record(self):
        if self.high_score > self.absolute_record:
            self.absolute_record = self.high_score

    def save_absolute_record(self):
        self.absolute_record = self.high_score
        self.absolute_record_str = str(self.high_score)
        self.update_absolute_record()
        with open(self.filename, 'w') as file_object:
            file_object.write(self.absolute_record_str)

    def check_file(self):
        if os.stat(self.filename).st_size > 0:
            return True
        else:
            return False

    def check_record(self):
        if self.check_file():
            with open(self.filename) as f_obj:
                self.high_score = int(f_obj.read())

