# Costruzione di una trave partendo dalle coordinate

import MEDCoupling as mc

d = mc.DataArrayInt([(1,2), (3,4), (5,6)], 3, 2)   # an array of 3 tuples with 2 components
print d[:,1]                                       # show only second component of the array: 2,4,6


