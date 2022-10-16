
f = open('values.txt', 'r')
content = f.read()
all_courses_list = []
fall_courses_list = []
lists = []
unique_fall_classes = []
for i in content.rstrip('\n').split(','):
#    print(i)
    if i[0] == '(':
#         print(int(i[1:]))
         lists.append(int(i[1:]))
    elif i[-1] == ')':
#        print(i,i[:-1])
        lists.append(int(i[:-1]))
    elif i[-2:] == ')\\n':
        print(i)
        lists.append(int(i[:-3]))
    else:
        lists.append(int(i))
    if len(lists) == 4:
        all_courses_list.append(lists)
        lists = []
for i in range(len(all_courses_list)):
#    print(all_courses_list[i])
    if all_courses_list[i][2] == 2:
        fall_courses_list.append(all_courses_list[i])

for i in range(len(fall_courses_list)):
    if fall_courses_list[i][1] not in unique_fall_classes:
        unique_fall_classes.append(fall_courses_list[i][1])
print(unique_fall_classes)
print(len(unique_fall_classes))
f.close()
