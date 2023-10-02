import pandas as pds
import openpyxl
import itertools as iter

workbook = openpyxl.load_workbook('example.xlsx')
worksheet = workbook.active
newData = pds.read_excel("example.xlsx")
#print(newData)

#add for loop based on number of opt
Op0 = "comd.pl "
Op1 = "comd.pl "
Op2 = "comd.pl "
Op3 = "comd.pl "

Opz = "comd.pl "

colList = newData.columns

for r in range(1,len(colList)):
    #print(colList[r]+"\n")
    for i in range(0,len(newData['Option'])):
        Opz += (str(newData['Option'][i]) + str(newData[colList[r]][i])) + " "
        if(i == len(newData['Option'])-1):
           print(Opz)
           Opz = "comd.pl "

#for col in worksheet.iter_cols():
 #   for cell in col:
 #       for i in range(0,len(newData['Val1'])):
 #           Op1 += print(str(cell.value)+ str(newData['Val1'][i])+" ")
#for r in newData.iterrows():
    #print(r)
    #for i in it.chain(range(0,len(newData['Val0']))):
        #Opz += (str(newData['Val0'][i]) + str(newData['r'][i])) + " "

for i in iter.chain(range(0,len(newData['Option']))):
     Opz += (str(newData['Option'][i]) + "=" + str(newData['Val1'][i])) + " "

for i in range(0,len(newData['Option'])):
    for j in range(0,len(newData['Val1'])):
        Op0 += str(newData['Option'][i]) + "=" + str(newData['Val1'][j]) + " "

for i in range(0,len(newData['Val1'])):
    Op1 += str(newData['Val1'][i])+" "

for i in range(0,len(newData['Val2'])):
    Op2 += str(newData['Val2'][i])+" "

for i in range(0,len(newData['Val3'])):
    Op3 += str(newData['Val3'][i])+" "

print(Opz)
print(Op0)
print(Op1)
print(Op2)
print(Op3)