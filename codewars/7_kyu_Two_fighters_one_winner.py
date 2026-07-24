# 7 kyu - Two fighters, one winner
# https://www.codewars.com/kata/577bd8d4ae2807c64b00045b
#
# Create a function that returns the name of the winner in a fight between two fighters.
# Each fighter takes turns attacking, and the attacker deals damage equal to their damage_per_attack.
# The first attacker is given. The fight ends when one fighter's health drops to 0 or below.
#
# 1. Моё решение — создаём кортеж `queue` с бойцами в порядке атаки,
#    затем в цикле атакуем первого, проверяем здоровье защитника,
#    и меняем местами для следующего раунда.
# 2. Альтернатива (из комментариев) — используем переменные `cur` и `opp`,
#    после каждой атаки меняем их местами. Возвращаем имя победителя.

class Fighter:
    """Класс Fighter определён в ката, здесь приведён для справки."""
    def __init__(self, name: str, health: int, damage_per_attack: int):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

def declare_winner(
    fighter1: Fighter,
    fighter2: Fighter,
    first_attacker: str
) -> str:
    # Основное решение — с явной очередью
    queue = (fighter1, fighter2) if fighter1.name == first_attacker else (fighter2, fighter1)
        
    while queue[0].health > 0 and queue[1].health > 0:
        attacker = queue[0]
        defender = queue[1]
        
        defender.health -= attacker.damage_per_attack
        
        if defender.health <= 0:
            return attacker.name
            
        queue = (queue[1], queue[0])


# Альтернативное решение — более компактное, с переменными cur/opp
def declare_winner_alternative(
    fighter1: Fighter,
    fighter2: Fighter,
    first_attacker: str
) -> str:
    cur, opp = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while cur.health > 0:
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name