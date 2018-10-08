# Da una mesh completa di risultati, vengono prodotti
# dei file di ParaView.
# TODO: capire come mai non si riesce a creare un file unico con le mesh
# dei due ordini

#import os
import MEDCoupling as mc
import MEDLoader as ml

mfl=ml.MEDFileMeshes("results_1D2D.med")
meshesNames = ml.MEDFileMeshes.getMeshesNames(mfl)
print("Nomi delle mesh...")
print meshesNames

mff=ml.MEDFileFields("results_1D2D.med")
fileldsNames = ml.MEDFileFields.getFieldsNames(mff)
print("Nomi dei campi...")
print fileldsNames

m2D = ml.ReadUMeshFromFile("results_1D2D.med","mesh",0) # solo faccie
m1D = ml.ReadUMeshFromFile("results_1D2D.med","mesh",-1) # solo edges

m2D.writeVTK("results_2D_only_mesh.vtu")
m1D.writeVTK("results_1D_only_mesh.vtu")

field2D=ml.ReadFieldNode("results_1D2D.med","mesh",0,"reslin__DEPL",1,1)
field1D=ml.ReadFieldNode("results_1D2D.med","mesh",-1,"reslin__DEPL",1,1)

file_name_2D = mc.MEDCouplingFieldDouble.WriteVTK( "results_2D_field_DZ", field2D )
file_name_1D = mc.MEDCouplingFieldDouble.WriteVTK( "results_1D_field_DZ", field1D )

