def queue(*args):
    data = list(args)
    while data:
        next = data.pop(0)
        new_value = (yield next)
        if new_value is not None:
            data.append(new_value)

shop_queue = queue('Vasya', 'Maria', 'Victor', 'Ars')
for name in shop_queue:
    print(f'приглашается {name}')
    if name == 'Maria':
        print('А кто последний?')
        name = shop_queue.send('Volodya')
        print(f'К кассе приглашается {name}')