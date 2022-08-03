from random import randint

from .enemy import Boss


def shop_section(section_name, items_array, hero):
    print(f'---/  {section_name}  /---')
    print(f'Your money: {hero.money}')
    for item in items_array:
        print(f'{item["item"].name} --- ${item["item"].price} [{item["index"]}]')

    print('Back [0]')
    selected_item_index = int(input('Select index: '))
    if selected_item_index != 0:
        selected_item = items_array[selected_item_index - 1]['item']
        if hero.money > selected_item.price:
            hero.money -= selected_item.price
            if section_name == 'Weapon':
                hero.change_right_hand_weapon(selected_item.price)
            else:
                hero.add_hit_points(selected_item.recovery_value)
        else:
            print('You have no money!')
    else:
        print('Back!')


def fight_process(request, hero_class, enemy_class, shop):
    while enemy_class.hit_points != 0:
        print(f'{enemy_class.name} HP: {enemy_class.hit_points}')
        print('----------------------------------')
        print(f'{hero_class.name} HP: {hero_class.hit_points}')
        print('---  /  Actions  /  ---')
        for i, attack in enumerate(hero_class.attacks):
            print(f'{i}) Здiбностi {attack["name"]}')
        hero_action = str(input('Виберiть дiю: '))

        for i, attack in enumerate(hero_class.attacks):
            if str(i) == hero_action:
                if isinstance(enemy_class, Boss):
                    if attack['id'] == 4:
                        print(f'Дiя {attack["name"]} - {hero_class.attack(i)} dmg')
                        enemy_class.change_hip_points(hero_class.attack(i))
                    else:
                        print(enemy_class.block_skills(i))
                else:
                    print(f'Дiя {attack["name"]} - {hero_class.attack(i)} dmg')
                    enemy_class.change_hip_points(hero_class.attack(i))

        if enemy_class.hit_points == 0:
            if isinstance(enemy_class, Boss):
                quiz_index = 0
                while quiz_index <= 2:
                    print('-------------------------------------------')
                    print(f'{enemy_class.quiz[int(quiz_index)]["text"]}')
                    print('-------------------------------------------')
                    question_index = 0
                    for question in enemy_class.quiz[int(quiz_index)]['questions']:
                        print(f'{question_index}) {question}')
                        question_index = question_index + 1
                    print('-------------------------------------------')
                    hero_answer = input('Ответ: ')

                    print(enemy_class.quiz[int(quiz_index)]['questions'][int(hero_answer)])
                    print(enemy_class.quiz[int(quiz_index)]['good'])

                    if enemy_class.quiz[int(quiz_index)]['questions'][int(hero_answer)] == enemy_class.quiz[int(quiz_index)]['good']:
                        quiz_index = quiz_index + 1
                        continue
                    else:
                        print('Ти прогдав iди пиляй хiдер')
                        break
                else:
                    print('You Won!')
            else:
                hero_class.set_experience(enemy_class.experience)
                hero_class.money += enemy_class.money
                while True:
                    print('---/  SHOP  /---')
                    print('Seller: Welcome in my shop!')
                    print('Weapon [1]')
                    print('Food [2]')
                    print('Exit [3]')
                    shop_map = int(input('Select shop option: '))

                    if shop_map == 1:
                        shop_section('Weapon', shop.weapons, hero_class)
                    elif shop_map == 2:
                        shop_section('Food', shop.foods, hero_class)
                    else:
                        break
        else:
            print(f'{enemy_class.dialogs[int(randint(0, 3))]}')
            if hero_class.hit_points <= enemy_class.damage:
                print('You Die...')
                break
            else:
                hero_class.change_hip_points(enemy_class.damage)
