# Unstructured mesh and image making with paraview python ui

#import os
import MEDCoupling as mc
import MEDLoader as ml

mfl=ml.MEDFileMeshes("results_1D.med")
meshesNames = ml.MEDFileMeshes.getMeshesNames(mfl)
print("Nomi delle mesh...")
print meshesNames

mff=ml.MEDFileFields("results_1D.med")
fileldsNames = ml.MEDFileFields.getFieldsNames(mff)
print("Nomi dei campi...")
print fileldsNames

m2D = ml.ReadUMeshFromFile("results_1D.med","mesh",0)
m2D.writeVTK("results_1D_only_mesh.vtu")

field1=ml.ReadFieldNode("results_1D.med","mesh",0,"reslin__DEPL",1,1)

file_name = mc.MEDCouplingFieldDouble.WriteVTK( "results_1D_field_reslin__DEPL", field1 )
