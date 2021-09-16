x = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
new_list = []
new_list2 = []

for i in x :
    values = list(i.values())
    new_list.append(values)

for i in new_list:
    new_list2.append(i[0])

print(list(set(new_list2)))

