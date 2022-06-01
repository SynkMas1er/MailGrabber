#----------==========mail extractor==========-----------

import re
defect = []
final = []
with open("C:\\all.csv", "r", encoding="UTF-8") as inputfile:
    for i in inputfile:
#        strload = inputfile.readline()
        defstr = re.findall(r'cid:[-_.\w]+@[-.a-z0-9]+\.[-.a-z0-9]+', i)  #removing trash begins with cid:...
        if len(defstr) > 0:
#            print(defstr)
            for mail in defstr:
                defect.append(mail)                                       #saving removed info for analysis
        else:
            mainstr = re.findall(r'[-_.\w]+@[-.a-z0-9]+\.[-.a-z0-9]+', i) #getting mails
            if len(mainstr) > 0:
 #               print(mainstr)
                for mail in mainstr:
                    final.append(mail)
finfinal = set(final)							  #deleting dublicates 
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
#print(finfinal)
with open("C:\\users\\public\\2.txt", "w") as outfile:			  #writing to file string by string
    for str in finfinal:
        outfile.writelines(str + "\n")
with open("C:\\users\\public\\def.txt", "w") as outfile:		  #writing trash to file
    for str in defect:
        outfile.writelines(str + "\n")
