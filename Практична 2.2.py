def insert_after(lst, target, new_elem):
    index = lst.index(target)
    lst.insert(index + 1, new_elem)
    return lst


spisok = input("Введіть елементи списку через пробіл: ").split()
target = input("Після якого елемента вставити? ")
new_elem = input("Який елемент вставити? ")

spisok = insert_after(spisok, target, new_elem)

print("Результат:", spisok)