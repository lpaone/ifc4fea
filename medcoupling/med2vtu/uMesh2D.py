# Unstructured mesh and image making with paraview python ui

import os
import MEDCoupling as mc
import MEDLoader as ml

# Connectivity

coords = [
  -0.3,-0.3,0.,
   0.2,-0.3,0.,
   0.7,-0.3,0.,
  -0.3,0.2,0.,
   0.2,0.2,0.,
   0.7,0.2,0.,
  -0.3,0.7,0.,
   0.2,0.7,0.,
   0.7,0.7,0.
]

nodalConnOfCell = [
  0,3,4,1,
  1,4,2,
  4,5,2,
  6,7,4,3,
  7,8,5,4
]

# Making mesh

mesh=mc.MEDCouplingUMesh("My2DMesh",2)

# Allocating resources

mesh.allocateCells(5) #You can put more than 5 if you want but not less.

# Building cells

print("Cella n.1 formata dai nodi --> ", nodalConnOfCell[:4])
mesh.insertNextCell( mc.NORM_QUAD4 , nodalConnOfCell[:4])
print("Cella n.2 formata dai nodi --> ", nodalConnOfCell[4:7])
mesh.insertNextCell( mc.NORM_TRI3  , nodalConnOfCell[4:7])
print("Cella n.3 formata dai nodi --> ", nodalConnOfCell[7:10])
mesh.insertNextCell( mc.NORM_TRI3  , nodalConnOfCell[7:10])
print("Cella n.4 formata dai nodi --> ", nodalConnOfCell[10:14])
mesh.insertNextCell( mc.NORM_QUAD4 , nodalConnOfCell[10:14])
print("Cella n.5 formata dai nodi --> ", nodalConnOfCell[14:])
mesh.insertNextCell( mc.NORM_QUAD4 , nodalConnOfCell[14:])

# Restore mesh instance.

mesh.finishInsertingCells()

# Store coords in reshape array
coordsArr = mc.DataArrayDouble(coords,9,3)

mesh.setCoords(coordsArr)

mesh.writeVTK("uMesh2D.vtu")

ml.WriteUMesh("uMesh2D.med",mesh,True)

# Python ui in paraview
cmd = 'pvpython uMesh2Dpvcomm.py'
os.system(cmd) # returns the exit status
