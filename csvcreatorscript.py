import csv
import os
import re


def create_csv_object(rows, columns, placeholder, headings=True):
    csvobject=[]
    # initialize the row stuff
    for i in range(rows):
        csvobject.append('')
    for i in range(rows):
        if headings and i==0:
            for j in range(columns):
                # make it so that so that the last column doesnt have a comma, or that will throw off the CSV
                if j==columns-1:
                    csvobject[i]+=f'Column {j}'
                else:
                    csvobject[i]+=f'Column {j},'
        else:
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
    


def generatecsv(csvobject, folderpath):
    '''
    Makes the csv file with the csv object to a folderpath , and with the csv object the rows and columns are specified already
    '''
    lastnum=folderpath.split('/')[-1].split('e')[-1]
    filename=f'{folderpath}/csvfile{lastnum}.csv'

    with open(filename,'w',newline='') as csv_file:
        writer=csv.writer(csv_file)
        for row in csvobject:
            row=row.split(',')
            writer.writerow(row)
        print(f'Made {filename}\n')
    return "return this so no errors"



# need to finish this function still

def csv_testcases():
    print('\n')

    print(f'Test1:\n')
    test1=create_csv_object(3,3,'a')
    print(f'Test2:\n')
    test2=create_csv_object(10,2,'csv')

    print(f'Test3:\n')

    # this one is saved


    test3csvobject=create_csv_object(3,9,'3rd')
    print('\nThe following is teset3 csv object\n')
    print(test3csvobject)

    print("\nNext is the creation of a csv document based on the csv object")
    csvtest1=generatecsv(csvobject=test3csvobject, folderpath=os.getcwd())
    
# this returns nothing but runs all the prints and calls
csv_testcases()


#-----------------------------------------------------------------------------------------------


# automating some md and csv creation for my website project
'''Website Automation Stuff:'''



# I can just use abspath for working in the same directory though
folderpath=('../../../../Projects/website_programming_project/website/assets')

def automate_csv_creation(folderpath):
    '''
    Generates sample files for website programming project.
    '''
    


    maindirs=[item for item in os.listdir(folderpath) if os.path.isdir(f'{folderpath}/{item}')]
    maindirs=[item for item in maindirs if "50" not in item]
    # first get sorted lists
    for dir in maindirs:
        dirs1_5=maindirs[0]
        dirs6_10=maindirs[1]

    # only get folders in the in lists. Unecessary since the bug was in main dirs not these. Anyway good for assurance now I guess.
    in_dirs1_5=[item for item in os.listdir(f'{folderpath}/{dirs1_5}') if os.path.isdir(f'{folderpath}/{dirs1_5}/{item}')]
    in_dirs6_10=[item for item in os.listdir(f'{folderpath}/{dirs6_10}') if os.path.isdir(f'{folderpath}/{dirs6_10}/{item}')]

    # damn both of these work lmao
    example='assetfolder1'
    # this is what Im doing down below
    getlastdigits=example.split('e')[-1]

    in_dirs1_5=sorted(in_dirs1_5,key=lambda x:int(x.split('e')[-1]))

    # tried new method with re.split()
    in_dirs6_10=sorted(in_dirs6_10,key=lambda x:int(re.split(r'(\d+)', x)[1]))

    # then add it all to the assets folder

    # in_dirs is the actual folders. dirs1_5 is the storage folder
    for folder in in_dirs1_5:
        # get num from the foldername
        num=int(folder.split('e')[-1])

        fullpath=f'{folderpath}/{dirs1_5}/{folder}'

        csvobject=create_csv_object(rows=num,columns=num,placeholder=num,headings=False)
        generatecsv(csvobject=csvobject,folderpath=fullpath)
    for folder in in_dirs6_10:
        num=int(folder.split('e')[-1])

        fullpath=f'{folderpath}/{dirs6_10}/{folder}'

        csvobject=create_csv_object(rows=num,columns=num,placeholder=num,headings=False)
        generatecsv(csvobject=csvobject,folderpath=fullpath)

def runthecsvcreation():
    print(f'automate_csv_creation:\n{automate_csv_creation(folderpath=folderpath)}')



# runthecsvcreation()



print(f'Does folderpath exist? \n{os.path.exists(folderpath)}')

def generate50():
    fiftyobject=create_csv_object(rows=50,columns=50,placeholder=50, headings=False)
    generatecsv(fiftyobject,'/Users/shalevwiden/Downloads/Projects/website_programming_project/website/assets/webassetfolder50')
