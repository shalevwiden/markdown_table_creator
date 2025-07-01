
import csv
import os

import re


'''

:--- → left-aligned

:---: → center-aligned

---: → right-aligned
'''

def createmarkdowntable3(rows, columns, placeholder,headings= True):
    '''
    rows and columns should be the number of rows and columns desired in the table.
    placeholder is a string that will fill every non heading box.
    Heading is a parameter, which is by default true, which sets the Column Names at the top of the table.

    Then this function will also create a .md file with the table, in a directory specificed with the folderpath parameter, through the generate_md_with_table subfunction
    The function is markdowntable3 since its the 3rd version of this function, the first two had problems.
    Returns a table object
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
    # this return statement at the end of the function
    return tableobject

def mdtestcases():
    # column length is bigger and remainder should be even at 6
    print('\nFirst Test Case\n')
    firsttestcase=createmarkdowntable3(3,3,'1234')
    print('\nSecond Test Case\n')
    # value length is bigger
    # even if the column lines arent perfectly aligned it will still create a table.
    secondtestcase=createmarkdowntable3(3,3,'123456789')

    return "return this so no errors"



printtestcases=mdtestcases()

def generate_md_with_table(tableobject,folderpath):
        
    filename=f'{folderpath}/markdowntable.md'
    with open(filename,'w') as mdfile:
        mdfile.write('# Markdowntable Outcome\n')
        mdfile.write('## The generated markdown table is below:\n')

        for row in tableobject:
            mdfile.write(row+'\n')
    print(f'Generated {filename[-17:]} at {folderpath}')

    return "return this so no errors"


generate_md_with_table(tableobject=createmarkdowntable3(3,3,'box'),folderpath=os.getcwd())

# automating some markdown folder creation for my website project

'''Website Automation Stuff:'''
# I can also borrow the delete script from my animation project to clear out mishaps

def modified_generate_md_with_table(tableobject,folderpath):
    # the folderpath will be the assetstorage{num} folder
        
    lastnum=folderpath.split('/')[-1].split('e')[-1]

    filename=f'{folderpath}/markdowntablefile{lastnum}.md'
    with open(filename,'w') as mdfile:
        mdfile.write(f'# Markdown Table File {lastnum}\n')
        mdfile.write('### The generated markdown table is below:\n')

        for row in tableobject:
            mdfile.write(row+'\n')
        mdfile.write("\n")
        mdfile.write(f'It has {lastnum} rows and {lastnum} columns  \n')
        mdfile.write('Generated from the `modified_generate_md_with_table()` function.  \nAnd the `automate_md_and_csv_creation()` function.\n')
        mdfile.write(f'''
    ```python
                     modified_generate_md_with_table(tableobject,folderpath)
                     automate_md_and_csv_creation(folderpath)
                     ```  \n
''')
    print(f'Generated {filename.split('/')[-1]} at {folderpath}')

    return "return this so no errors"

folderpath='/Users/shalevwiden/Downloads/Projects/website_programming_project/website/assets'
def automate_md_creation(folderpath):
    '''
    Generates sample files for website programming project
    '''
    maindirs=os.listdir(folderpath)
    # first get sorted lists
    for dir in maindirs:
        dirs1_5=maindirs[0]
        dirs6_10=maindirs[1]

    in_dirs1_5=os.listdir(f'{folderpath}/{dirs1_5}')
    in_dirs6_10=os.listdir(f'{folderpath}/{dirs6_10}')

    # damn both of these work lmao
    example='assetfolder1'
    # this is what Im doing down below
    num=example.split('e')[-1]
    in_dirs1_5=sorted(in_dirs1_5,key=lambda x:int(x.split('e')[-1]))
    
    # tried new method with re.split()
    in_dirs6_10=sorted(in_dirs6_10,key=lambda x:int(re.split(r'(\d+)', x)[1]))

    # then add it all to the assets folder

    # in_dirs is the actual folders. dirs1_5 is the storage folder
    for folder in in_dirs1_5:
        fullpath=f'{folderpath}/{dirs1_5}/{folder}'

        tableobject=createmarkdowntable3(rows=num,columns=num,placeholder=num)
        modified_generate_md_with_table(tableobject=tableobject,folderpath=fullpath)
    for folder in in_dirs6_10:
        fullpath=f'{folderpath}/{dirs1_5}/{folder}'

        tableobject=createmarkdowntable3(rows=num,columns=num,placeholder=num)
        modified_generate_md_with_table(tableobject=tableobject,folderpath=fullpath)


print(f'automate_md_creation:\n{automate_md_creation(folderpath=folderpath)}')