# Unstructured mesh and image making with paraview python ui

#import os
import MEDCoupling as mc
import MEDLoader as ml

mfl=ml.MEDFileMeshes("results_2D.med")
meshesNames = ml.MEDFileMeshes.getMeshesNames(mfl)
print("Nomi delle mesh...")
print meshesNames

mff=ml.MEDFileFields("results_2D.med")
fileldsNames = ml.MEDFileFields.getFieldsNames(mff)
print("Nomi dei campi...")
print fileldsNames

m2D = ml.ReadUMeshFromFile("results_2D.med","mesh",0)
m2D.writeVTK("results_2D_only_mesh.vtu")

field1=ml.ReadFieldNode("results_2D.med","mesh",0,"DZ",1,1)

file_name = mc.MEDCouplingFieldDouble.WriteVTK( "results_2D_field_DZ", field1 )

