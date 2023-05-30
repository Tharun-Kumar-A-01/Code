ln='\n----------------------------\n'
print(ln,'Welcome to the Accountant',ln)
ic,icr,ict=[],[],0
ex,exr,ext=[],[],0
while(True):
    print('\n1.Income\n2.Expense\n3.Total\n')
    inp=int(input('Enter your option : '))
    if(inp==1):
        ic.append(input('Source : '))
        it=int(input('Amount : '))
        icr.append(it)
        ict+=it
    elif(inp==2):
        ex.append(input('Source : '))
        iv=int(input('Amount : '))
        exr.append(iv)
        ext+=iv
    elif(inp==3):
        break
    else:
        print('INVALID OPTION')
sav=ict-ext
print(ln,'\tINCOME\n')
for i in range(0,len(ic)):
    print(ic[i],'\n\t',icr[i])
print('\nTOTAL INCOME :\t',ict,'\n')
print(ln,'\tEXPENSE\n')
for i in range(0,len(ex)):
    print(ex[i],'\n\t',exr[i])
print('\nTOTAL EXPENSE :\t',ext,ln)
print('BALANCE : ',sav,ln)
