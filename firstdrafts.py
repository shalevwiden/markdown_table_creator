
def createmarkdown_table(rows,columns,placeholder,headings=True):
    '''
    rows and columns should be the number of rows and columns desired in the table.
    placeholder is a string that will fill every non heading box.
    Heading is a parameter, which is by default true, which sets the Column Names at the top of the table
    '''
    tableobject=[]
    if headings:
        firstrowlen=len(f'Column {columns} |'*columns)
        rowbox=len(f' Column {columns} ')
        # returns a boolean true or false
        elongateheadings = (rowbox % 2 != 0)

        if elongateheadings:
            rowbox+=1
            
        # initialize table object
    for row in range(rows):
        tableobject.append('')
    for i in range(rows):
        tableobject[i]='|'
        for j in range(columns):
            if headings:
                if i==0:
                    if elongateheadings:
                        tableobject[i]+=f' Column {j}  |'*columns

                    else:
                        tableobject[i]+=f' Column {j} |'*columns
                else:
                    tableobject[i]+=f'{rowbox/2*' '}{placeholder}{rowbox/2*' '}|'*columns
            else:
                tableobject[i]+=f' {placeholder} |'*columns


    print(tableobject[i])
    print('-'*len(tableobject[i]))
        

# x=createmarkdown_table(3,3,'a')

def createmarkdown_table2(rows,columns,placeholder,headings=True):
    '''
    rows and columns should be the number of rows and columns desired in the table.
    placeholder is a string that will fill every non heading box.
    Heading is a parameter, which is by default true, which sets the Column Names at the top of the table
    '''
    tableobject=[]
    if headings:
        firstrowlen=len(f'Column {columns} |'*columns)
        rowbox=len(f' Column {columns} ')
        # returns a boolean true or false
        elongateheadings = (rowbox % 2 != 0)

        if elongateheadings:
            rowbox+=1
            
        # initialize table object
    for row in range(rows):
        tableobject.append('')
    for j in range(rows):
        for i in range(columns):
            tableobject[i]='|'
            if headings:
                if i==0:
                    if elongateheadings:
                        tableobject[i]+=f' Column {i}  |'*columns

                    else:
                        tableobject[i]+=f' Column {i} |'*columns
                else:
                    tableobject[i]+=f'{(rowbox//2)*' '}{placeholder}{(rowbox//2)*' '}|'*columns
            else:
                tableobject[i]+=f' {placeholder} |'*columns

    for i in range(len(tableobject)):
        print(tableobject[i])
        print('-'*len(tableobject[i]))

x=createmarkdown_table2(3,3,'a')