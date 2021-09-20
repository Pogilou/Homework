def get_pairs(lst):
    pair_list = []
    if len(lst) == 1:
        return None
    for i in range((len(lst))-1):
        tuplee = (lst[i],lst[i+1])
        pair_list.append(tuplee)
    return(pair_list)

print(get_pairs(['need', 'to', 'sleep', 'more']))