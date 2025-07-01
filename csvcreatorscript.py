import csv
import os
def create_csv_object(rows, columns, placeholder, headings=True):
    csvobject=[]
    # initialize the row stuff
    for i in range(rows):
        csvobject.append('')
    for i in range(rows):
        for j in range(columns):
            # make it so that so that the last column doesnt have a comma. 
            if j==columns-1:
                csvobject[i]+=f'{placeholder}'
            else:
                csvobject[i]+=f'{placeholder},'
   # print the csv object, can comment this out:
    for generatedrow in csvobject:
        print(generatedrow)
    return csvobject
    


def generatecsv(csvobject, folderpath,csvname='generatedcsv'):
    '''
    Makes the csv file with the csv object to a folderpath , and with the csv object the rows and columns are specified already
    '''
    fullpath=f'{folderpath}/{csvname}.csv'
    with open(fullpath,'w',newline='') as csv_file:
        writer=csv.writer(csv_file)
        for row in csvobject:
            row=row.split(',')
            writer.writerow(row)
        print(f'Made {fullpath}')
    return "return this so no errors"



# need to finish this function still

def csv_testcases():
    print('\n')

    print(f'Test1:\n')
    test1=create_csv_object(3,3,'a')
    print(f'Test2:\n')
    test2=create_csv_object(10,2,'csv')

    print(f'Test3:\n')
    test3csvobject=create_csv_object(3,9,'3rd')
    print('\nThe following is teset3 csv object\n')
    print(test3csvobject)

    print("\nNext is the creation of a csv document based on the csv object")
    csvtest1=generatecsv(csvobject=test3csvobject, folderpath=os.getcwd())
    
# this returns nothing but runs all the prints and calls
csv_testcases()


folderpath='/Users/shalevwiden/Downloads/Projects/website_programming_project/website/assets'
def automate_csv_creation(folderpath):
    '''
    Generates sample files for website programming project
    '''
    pass