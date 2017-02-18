# bloomberg_py_munge
A Python module that munges Bloomberg historical xlsx output into Pandas dataframe

# Why is this needed?

![Alt text](./img/exceelscreen.png?raw=true "Optional Title")

# Usage:
```python
import pandas as pd
import bloomberg_py_munge
df = bloomberg_py_munge.from_excel('PATH_TO_FILE', 'Sheet1')
```