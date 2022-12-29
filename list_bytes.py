def in_byts(lists): # из списка строк в список байтов
    lists_byts = []
    for i in range(len(lists)):
        str_b = lists[i].encode()
        lists_byts.append(str_b)
    return lists_byts

def in_str(byts): # из списка байтов в список строк
    lists_str = []
    for i in range(len(byts)):
        str_b = byts[i].decode()
        lists_str.append(str_b)
    return lists_str 

def inp_str(): # проверка ввода
    s = (input("\nВведите строку: "))
    return s       

def str_list_f():
    list_str = []      
    a = 1
    while a == 1:
        
        str_q = str(input("\nДля ввода числа нажмите +, для окончания любую клавишу: "))
        if str_q == '+':
            
            list_str.append(inp_str())
            continue
        
        else:
            return list_str
            break

new__str_list = str_list_f()
while True:
    if new__str_list == []:
        print("\nВы ничего не ввели!")
        new__str_list = str_list_f()
    else:
        print("\nСписок байт кодов:",in_byts(new__str_list))
        print("\nСписок cтрок, преобразованный из списка байт кодов:",in_str(in_byts(new__str_list)))
        break