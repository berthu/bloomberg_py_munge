# bloomberg_py_munge
A Python module that munges Bloomberg historical xlsx output into Pandas dataframe

## Why is this needed?

Instead of getting involved in the Bloomberg API, sometimes it's just easier to drag the Bloomberg data into excel. Unfortunately it looks like this:

![Alt text](./img/excelscreen.png?raw=true "Optional Title")

This module would import the above excel sheet into a dataframe with the following column names:
```python
['date','security','PX_LAST','PX_BID','BID_YIELD']
```

## Usage:
```python
import pandas as pd
import bloomberg_py_munge
df = bloomberg_py_munge.from_excel('PATH_TO_FILE', 'Sheet1')
```