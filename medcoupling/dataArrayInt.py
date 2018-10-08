# Costruzione di una trave partendo dalle coordinate
'''
an array of 3 tuples with 2 components
show only second component of the array: 2,4,6
Name of int array : ""
Number of components : 1
Info of these components : ""   
Number of tuples : 3
Internal memory facts : 3/3
Data content :
Tuple #0 : 2 
Tuple #1 : 4 
Tuple #2 : 6 

and finally all of componets of the array
Name of int array : ""
Number of components : 2
Info of these components : ""   ""   
Number of tuples : 3
Internal memory facts : 6/6
Data content :
Tuple #0 : 1 2 
Tuple #1 : 3 4 
Tuple #2 : 5 6 

Proviamo una funzione di help con help(mc.DataArrayInt)
'''
import MEDCoupling as mc
print("an array of 3 tuples with 2 components")
d = mc.DataArrayInt([(1,2), (3,4), (5,6)], 3, 2)   # an array of 3 tuples with 2 components
print("show only second component of the array: 2,4,6")
print d[:,1]                                       # show only second component of the array: 2,4,6
print("and finally all of componets of the array")
print d                                        # show only second component of the array: 2,4,6
print("Proviamo una funzione di help con help(mc.DataArrayInt)")
help(mc.DataArrayInt)


