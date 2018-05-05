# Costruzione di una trave partendo dalle coordinate

import MEDCoupling as mc
print("an array of 3 tuples with 2 components")
d = mc.DataArrayInt([(1,2), (3,4), (5,6)], 3, 2)   # an array of 3 tuples with 2 components
print("show only second component of the array: 2,4,6")
print d[:,1]                                       # show only second component of the array: 2,4,6
print("and finally all of componets of the array")
print d                                        # show only second component of the array: 2,4,6
print("Proviamo una funzione di help con help(mc.DataArrayInt)")
help(mc.DataArrayInt)


