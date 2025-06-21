## Markdown Table Creator

In this folder, in the tablecreatorscript.py file, I made a function, createnmarkdowntable3, that creates a markdowntable based on specified parameters. I learned more about the properties of markdown tables. In addition I defined csv creating functions, and csv.

In order to copy the table into something like notion, instead of copying from the markdown document, copy from the stylized preview.

You can copy a csv into an Excel or google sheets document, or open it directly with Excel.

---

### Breaking down the createmarkdowntable3() function:

```python
def createmarkdowntable3(rows, columns, placeholder,headings= True):

```

The function has 4 parameters:

- rows (int)
- columns (int)
- placeholder (string)
- Headings (bool)

Rows and columns should be the number of rows and columns desired in the table.
Placeholder is a string that will fill every non heading box.
Heading is a boolean parameter, which is by default True, which sets the Column Names at the top of the table.

Then the generate_md_with_table() function will also create a .md file with the table, in a directory specificed with the folderpath parameter.

The function returns a tableobject (a list) where each item in the list is a row in the table, which is later used in the generate_md_with_table() function.
The function is createmarkdowntable3 since its the 3rd version of this function, the first two didnt quite work out, and are in the firstdrafts.py file.

### generate_md_with_table function:

```python
def generate_md_with_table(tableobject,folderpath):

```

This function takes a tableobject and a folderpath and generates a markdown file with the table object in it. Each file will be named markdowntable.md by default, but the filename can be changed with the filename parameter.

### Generate csv object:

```python
def create_csv_object(rows, columns, placeholder, headings=True):

```

Creates a csv object(list) which can later be used in the generatecsv function.

### Generate CSV file

```python
def generatecsv(csvobject, folderpath):

```

Uses the csvobject to make a csv file in a specified file path. The csv can then be viewed in vs code in its comma format or opened in an editor to view in tabular format.
