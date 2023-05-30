ln='\n----------------------------\n'
print(ln,'Welcome to the Accountant',ln)
ic,icr,ict=[],[],0
ex,exr,ext=[],[],0
while(True):
    print('\n1.Income\n2.Expense\n3.Total\n')
    inp=int(input('Enter your option : '))
    if(inp==1):
        print('Income :')
        ic.append(input('\tSource : '))
        it=int(input('\tAmount : '))
        icr.append(it)
        ict+=it
    elif(inp==2):
        print('Expense :')
        ex.append(input('\tSource : '))
        iv=int(input('\tAmount : '))
        exr.append(iv)
        ext+=iv
    elif(inp==3):
        break
    else:
        print('INVALID OPTION')
sav=ict-ext
print(ln,'\tINCOME\n\t------\n')
for i in range(0,len(ic)):
    print(ic[i],'\n\t',icr[i])
print('\nTOTAL INCOME :\t',ict,'\n')
print(ln,'\tEXPENSE\n\t-------\n')
for i in range(0,len(ex)):
    print(ex[i],'\n\t',exr[i])
print('\nTOTAL EXPENSE :\t',ext,ln)
print('BALANCE : ',sav,ln)
