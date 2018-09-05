import os
import sys
print('\nWELCOME TO GitAuto')
print('\nTool is developed by Nika Chitashvili for Developers!\n')
static_answer = 'n'
try:
    data_lines = []
    check = False
    os.system('git branch > branches.txt')
    branch = sys.argv[1]
    with open('branches.txt') as branches:
        for line in branches:
            data_lines.append(line.split('\n'))
        for extra in range(len(data_lines)):
            while check == False:
                if ('* '+branch in data_lines[extra]):
                    check = True
                    break
                branch = input('No such branch, Enter The branch name again: ')
    os.system('rm branches.txt')
    answer = input('Are you sure, that you finished working in "'+branch+'" branch? [y/n] (default n): ')
    if(answer == 'y'):
        os.system('git add .')
        comment = input('Please enter comment for commit: ')
        os.system('git commit -m "%s"' % (comment))
        os.system('git push origin %s' % (branch))
        print('\nSuccess!')
    else:
        print('Ok, Bye')
except:
    print('Usage: ./update.py \'branch_name\'')
