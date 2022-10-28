from collections import defaultdict
tupl_one = (1, 3, 5, 7, 9, 16, 34, 63, 74, 114, 432)
tupl_two = (1, 45, 5, 34, 9, 54, 57, 4, 67, 114, 432)
tupl_three = (1, 3, 5, 34, 9, 532, 45, 364, 134, 114, 432)
tupl_all = defaultdict(int)
for i in tupl_one:
    if i in tupl_two:
        if i in tupl_three:
                tupl_all[i] += 1
print(tupl_all)#Выводит числа и количество их повторений


tupl_four = []
for i in tupl_one:
    tupl_five = tupl_two+tupl_three
    if i not in tupl_five:
        tupl_four.append(i)
for i in tupl_two:
    tupl_five = tupl_one+tupl_three
    if i not in tupl_five:
        tupl_four.append(i)
for i in tupl_three:
    tupl_five = tupl_one+tupl_two
    if i not in tupl_five:
        tupl_four.append(i)
print(tupl_four)#вывод уникальных чисел

tupl_six = []
for i in range(len(tupl_one)):
    if tupl_one[i] != tupl_two[i] != tupl_three[i]:
        continue
    else:
        tupl_six.append(tupl_one[i])
print(tupl_six)