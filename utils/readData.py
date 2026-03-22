import re
def readData(fileName):
    """
    read .dta file.
    """
    data = []
    f = open(f"../../datas/{fileName}.dta")
    fileContent = f.readlines()
    ok = 0
    for line in fileContent.split("\n"):
        match line:
            case "#config end":
                ok = 0
                break
            case "#config start":
                ok = 1
            case re.match("([#]\s[-][j]\s[#]\s).*", line):
                pass
            case re.match("[p][r][t][(](.*)[)]", line):
                data.append(line)
                print(re.sub("[p][r][t][(](.*)[)]", "\g<1>", line))
            case _:
                if ok == 1:
                    data.append(line)
                else:
                    pass
    return '\n'.join(data)
