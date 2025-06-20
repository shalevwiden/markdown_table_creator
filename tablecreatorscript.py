
import csv
import os


'''

:--- → left-aligned

:---: → center-aligned

---: → right-aligned
'''

def createmarkdowntable3(rows, columns, placeholder, folderpath,headings= True):
    '''
    rows and columns should be the number of rows and columns desired in the table.
    placeholder is a string that will fill every non heading box.
    Heading is a parameter, which is by default true, which sets the Column Names at the top of the table.

    Then this function will also create a .md file with the table, in a directory specificed with the folderpath parameter, through the generate_md_with_table subfunction
    The function is markdowntable3 since its the 3rd version of this function, the first two had problems.
    '''
    headings_bigger=len(f' {placeholder} ')<len( f' Column {columns}')
    if headings_bigger:
        colspacing=len(f' Column {columns} ')
    else:
        colspacing=len(f' {placeholder} ')
    tableobject=[]
    for i in range(rows):
        tableobject.append(i)
    
    for i in range(rows):
        tableobject[i]='|'
        if headings and i==0:
            for j in range(columns):
                tableobject[i]+=f' Column {j} |'
        elif i==1:
            for j in range(columns):
                tableobject[i]+=f'{"-"*colspacing}|'
        else:
            for j in range(columns):
                if headings_bigger:
                    remainder=len(f' Column {columns} ')-len(f' {placeholder} ')
                    # if remainder is evein
                    if remainder%2==0:
                        tableobject[i]+=f'{int(remainder/2)*' '} {placeholder} {int(remainder/2)*' '}|'
                    elif remainder%2!=0:
                        tableobject[i]+=f'{int(remainder//2)*' '} {placeholder} {(int(remainder//2)+1)*' '}|'
                else:
                    tableobject[i]+=f' {placeholder} |'
    for i in tableobject:
        print(i)
    def generate_md_with_table(tableobject,folderpath):
        filename=f'{folderpath}/markdowntable.md'
        with open(filename,'w') as mdfile:
            for row in tableobject:
                mdfile.write(row+'\n')
        print(f'Generated {filename[-17:]} at {folderpath}')

    # --------------------------------------------------------------
    # TESTING STUFF:
    # set teststatus above 0 to test
    test_status=0
    tests=True if test_status>0 else False
    if tests:
        print('current func:')
        print(f'colspacing is {colspacing}')
        if headings_bigger:
            print(f'remainder is {remainder}')
        print(f' headings bigger is {headings_bigger}')
        collen=len(f' Column {columns} ')
        placeholderlen=len(f' {placeholder} ')

        if headings_bigger:
            print(f'this means column headings are bigger at {collen} vs placeholderlen of {placeholderlen}')
        else:
            print(f'this means placeholder boxes are bigger at {placeholderlen} vs collen of {collen}')

def testcases():
    # column length is bigger and remainder should be even at 6
    print('\nFirst Test Case\n')
    firsttestcase=createmarkdowntable3(3,3,'1234',os.getcwd())
    print('\nSecond Test Case\n')
    # value length is bigger
    # even if the column lines arent perfectly aligned it will still create a table.
    secondtestcase=createmarkdowntable3(3,3,'123456789',os.getcwd())



printtestcases=testcases()

def create_csv_object(rows, columns, placeholder, headings=True):
    csvobject=[]
    for i in range(rows):
        csvobject.append('')
    for i in range(rows):
        for j in range(columns):
            csvobject[i]+=f'{placeholder},'
    return csvobject
def generatecsv(csvobject, folderpath):
    pass

def csv_testcases():
    print('\nFirst Test Case\n')
    test1=create_csv_object(3,3,'a')

print(csv_testcases())