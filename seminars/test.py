adv = [100, 125, -90, 345, 655, -1, 0, 200]

# Введите ваше решение ниже

def sorter(adv):
    new_adv = [i in adv if i > 0]
    return sum(new_adv)

print(sorter(adv))