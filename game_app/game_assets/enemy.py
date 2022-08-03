class Enemy:

    def __init__(self, name, level, dialogs):
        self.name = name
        self.level = level
        self.damage = 10 * self.level
        self.hit_points = 10 * self.level * 3.6
        self.dialogs = dialogs

    def change_hip_points(self, damage_value):
        if self.hit_points <= int(damage_value):
            self.hit_points = 0
        else:
            self.hit_points -= int(damage_value)


class Monster(Enemy):
    def __init__(self, name, level, dialogs):
        super().__init__(name, level, dialogs)
        self.experience = 100 * self.level
        self.money = 10 * self.level * 1.2


class Boss(Enemy):
    def __init__(self, name, level, dialogs):
        super().__init__(name, level, dialogs)
        self.block_skills_dialog = ['Не хочу я слухати цей бред', 'Какой Курить нiякого курить', 'Тебе шо в гуглi забанили']
        self.quiz = [
            {
                'text': 'Шо таке полiморфiзм?',
                'questions': [
                    'Бред',
                    'Шось на бекендськом',
                    'це здатність обєкта використовувати методи похідного класу',
                    'це здатність обєкта використовувати методи класу'
                ],
                'good': 'це здатність обєкта використовувати методи похідного класу'
            },
            {
                'text': 'Шо таке ООП?',
                'questions': [
                    'Опорно Ональный Проход',
                    'Офiгенний Олексiйович Петро',
                    'Обєктно Орієнтоване Питання',
                    'Обєктно Орієнтоване Програмування',
                ],
                'good': 'Обєктно Орієнтоване Програмування'
            },
            {
                'text': 'Шо зробив Петро Порошенко для Українаи?',
                'questions': [
                    'Викопав чорне море i насыпав Карпати',
                    'Всього по трошку',
                    'Поставив ПВО',
                    'Нiчього',
                ],
                'good': 'Викопав чорне море i насыпав Карпати'
            },
        ]

    def block_skills(self, attack_index):
        return self.block_skills_dialog[int(attack_index)]
