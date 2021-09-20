def method_split (line, elem, max_split=None):
    storing_element_indices = []
    line_split = []
    if max_split != '':
        for num, i in enumerate(line):
            if i == elem:
                storing_element_indices.append(num)
        storing_element_indices = storing_element_indices[:max_split]
    else:
        for num, i in enumerate(line):
            if i == elem:
                storing_element_indices.append(num)

    y = 0
    for i in (storing_element_indices):
        x = line[y:i]
        line_split.append(x)
        y = i+1
    line_split.append(line[y:])

    return line_split

print(method_split(".23.34225.pdf.q1.", ".", 3))