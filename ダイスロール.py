import random

def player():
    my_dice = random.randint(1,6)
    #print(f"私の出目は{my_dice}です。")
    return my_dice
def enemy():
    enemy_dice = random.randint(1, 6)
    #print(f"{enemy_dice}")
    return enemy_dice


my_roll = player()
enemy_roll = enemy()
print(f"私の出目は{my_roll}です")

def judge():
    print(f"相手の出目は{enemy_roll}でした")

your_answer = input('勝負する?(y/n)')
if your_answer == 'y':
    judge()
    if my_roll > enemy_roll:
        print('あなたの勝ちです')
    elif my_roll < enemy_roll:
        print('あなたの負けです')
    else:
        print('ヒキワケ！')

elif your_answer == 'n':
    judge()
    if my_roll > enemy_roll:
        print('実は勝っていました')
    elif my_roll < enemy_roll:
        print('戦略的撤退成功')
    else:
        print('ヒキワケ！')
else:
    print('ゲーム終了です')