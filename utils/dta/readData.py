import re
import getpass

def readData(fileName):
    """
    read .dta file.
    """
    data = []
    username = getpass.getuser()
    f = open(fr"D:\{username}\git\MathQ with Dani\data\{fileName}.dta")
    fileContent = f.readlines()
    ok = 0
    p1 = re.compile("([#]\s[-][j]\s[#]\s).*[;]")
    p2 = re.compile("[p][r][t][(](.*)[)][;]")
    for line in fileContent:
        if line == "#config end;" or line == "#config end;\n":
            ok = 0
            break
        elif line == "#config start;\n":
            ok = 1
        elif p1.match(line):
            pass
        elif p2.match(line):
            if line == "prt(--es);\n":
                print("이스터에그발견!")
            else:
                print(p2.sub("\g<1>", line))
        else:
            if ok == 1:
                data.append(line)
            else:
                pass
    return ''.join(data)
