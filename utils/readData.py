import re
def readData(fileName):
    """
    read .dta file.
    """
    data = []
    f = open(fr"D:\Leo\git\MathQ with Dani\datas\{fileName}.dta")
    fileContent = f.readlines()
    ok = 0
    p1 = re.compile("([#]\s[-][j]\s[#]\s).*")
    p2 = re.compile("[p][r][t][(](.*)[)]")
    for line in fileContent:
        if line == "#config end":
            ok = 0
            break
        elif line == "#config start":
            ok = 1
        elif p1.match(line):
            pass
        elif p2.match(line):
            print(p2.sub("\g<1>", line))
        else:
            if ok == 1:
                data.append(line)
            else:
                pass
    return '\n'.join(data)