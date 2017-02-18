# bloomberg_py_munge
A Python module that munges Bloomberg historical xlsx output into Pandas dataframe

# Why is this needed?


| SPY US Equity |      	   |	   |
| ------------- | --------:| -----:|
| Data          | PX_LAST  | PX_BID|
| 1/1/2016      | 152.62   | 152.61|
| 1/2/2106      | 161.35   | 161.34|

# Usage:
```python
import pandas as pd
import bloomberg_py_munge
df = bloomberg_py_munge.from_excel('PATH_TO_FILE', 'Sheet1')
```