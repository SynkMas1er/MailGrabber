#----------==========mail extractor==========-----------

import re
defect = []
final = []
with open("C:\\all.csv", "r", encoding="UTF-8") as inputfile:
    for i in inputfile:
#        strload = inputfile.readline()
        defstr = re.findall(r'cid:[-_.\w]+@[-.a-z0-9]+\.[-.a-z0-9]+', i)
        if len(defstr) > 0:
            print(defstr)
            for defe in defstr:
                defect.append(defe)
        else:
            mainstr = re.findall(r'[-_.\w]+@[-.a-z0-9]+\.[-.a-z0-9]+', i)
            if len(mainstr) > 0:
 #               print(mainstr)
                for sre in mainstr:
                    final.append(sre)
fifinal = set(final)
#                print(sre)
#                for ass in final:
#                    print(ass)
#                    if ass == sre:
#                        print('If')
#                        break
#                    else:
#                        final.append(sre)
#                        print(final)
#                print('for')
#print(fifinal)
with open("C:\\users\\public\\2.txt", "w") as outfile:
    for fd in fifinal:
        outfile.writelines(fd + "\n")
with open("C:\\users\\public\\def.txt", "w") as outfile:
    for fdw in defect:
        outfile.writelines(fdw + "\n")
