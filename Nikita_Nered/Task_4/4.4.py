def split_by_index (s: str, indexes):
    index = 0
    line = []
    for i in indexes:
        if i > len(s) or i < index:
            continue
        part_of_string = s[index:i]
        line.append(part_of_string)
        index = i
    line.append(s[index:])
    return line
print(split_by_index ("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))