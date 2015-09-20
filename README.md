# Optimal Scaling in Python

This is a a quick and dirty Python package for optimal scaling. It is 
actually just a wrapper around an R implementation called [optiscale]
(https://github.com/cran/optiscale) by William G. Jacoby. Further 
information is available in the [optiscale documentation (PDF)]
(http://polisci.msu.edu/jacoby/icpsr/scaling/computing/alsos/Jacoby,%20opscale%20MS.pdf).

Licensed under GNU GPL version 2.

## Example

Example taken from the documentation linked above.

```python
from pyopscale.opscale import OpScale

x1 = [1,1,1,1,2,2,2,3,3,3,3,3,3]
x2 = [3,2,2,2,1,2,3,4,5,2,6,6,4]
os = OpScale()
print(os.opscale(x1, x2, rescale=False))
```

The result of the above should be
`[2.25, 2.25, 2.25, 2.25, 2.0, 2.0, 2.0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5]`.