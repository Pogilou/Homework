def translate(line):
    intab = """ '" """
    outtab = ''' "' '''
    trantab = line.maketrans(intab, outtab) 
    return (line.translate(trantab))

