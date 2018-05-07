# http://docs.salome-platform.org/latest/dev/MEDCoupling/medcouplingpyexamples.html#medcouplingpyexamplesUmeshStdBuild1
# Standard build of an unstructured mesh from scratch

import os
import MEDCoupling as mc
import MEDLoader as ml

# Firstly retrieve basic data in full interlace mode for coordinates, and nodal
# connectivity cell per cell.

l = 2000; 
nbEl = 15;

oords = [
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

'''
nodalConnOfCell = [
  0,3,4,1,
  1,4,2,
  4,5,2,
  6,7,4,3,
  7,8,5,4
]

# Then create MEDCoupling::MEDCouplingUMesh UMesh instance giving its mesh
# dimension (2 here) and a name.

mesh=mc.MEDCouplingUMesh("My2DMesh",2)

# Gives an upper bound of the number of cells to be inserted into the
# unstructured mesh.

mesh.allocateCells(5) #You can put more than 5 if you want but not less.

# MEDCoupling::MEDCouplingUMesh::insertNextCell
# UMesh method.

mesh.insertNextCell( mc.NORM_QUAD4 , nodalConnOfCell[:4])
mesh.insertNextCell( mc.NORM_TRI3  , nodalConnOfCell[4:7])
mesh.insertNextCell( mc.NORM_TRI3  , nodalConnOfCell[7:10])
mesh.insertNextCell( mc.NORM_QUAD4 , nodalConnOfCell[10:14])
mesh.insertNextCell( mc.NORM_QUAD4 , nodalConnOfCell[14:])

# When the nodal connectivity cell per cell has been finished, call
# MEDCoupling::MEDCouplingUMesh::finishInsertingCells UMesh method in order
# to restore mesh instance.

mesh.finishInsertingCells()

# At this level the connectivity part of the mesh mesh as been defined.
# Now let's set the coordinates using array coords defined above.

# here coordsArr are declared to have 3 components, mesh will deduce that its
# spaceDim==3.
coordsArr = mc.DataArrayDouble(coords,9,3)

#coordsArr contains 9 tuples, that is to say mesh contains 9 nodes.
mesh.setCoords(coordsArr)

mesh.writeVTK("uMesh2D.vtu")

ml.WriteUMesh("uMesh2D.med",mesh,True)

# Python ui in paraview
cmd = 'pvpython uMesh2Dpvcomm.py'
os.system(cmd) # returns the exit status
'''
