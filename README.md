# bloomberg_py_munge
A Python module that munges Bloomberg xlsx output into a Pandas dataframe

## from_excel

Instead of getting involved in the Bloomberg API, sometimes it's just easier to drag the Bloomberg data into excel. Unfortunately it looks like this:

![Alt text](./img/excelscreen.png?raw=true "Optional Title")

This function would import the above excel sheet into a dataframe with the following column names:
```python
['date','security','PX_LAST','PX_BID','BID_YIELD']
```

### Usage:
```python
import pandas as pd
import bloomberg_py_munge
df = bloomberg_py_munge.from_excel('PATH_TO_FILE', 'Sheet1')
```
## get_cells

This function takes any excel sheet where the objects of interest are all the cells (containing securities identifiers), with the columns being labels. This is used for any kind of Bloomberg output that involves manually dragging securities identifiers into an excel sheet repeatedly, rather than using the API function calls. For example:

![Alt text](./img/excelscreen2.png?raw=true "Optional Title")

This function would import the above excel sheet into a dataframe with the following column names:
```python
['security','label']
```
where label is the column names from the sheet.

### Usage:
```python
import pandas as pd
import bloomberg_py_munge
df = bloomberg_py_munge.get_cell('PATH_TO_FILE', 'Sheet1')
```

# Requirements:
I think it goes without saying that you need *Pandas*. Also, I haven't tested this on Python 3.