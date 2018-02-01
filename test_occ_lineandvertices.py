# =============================================================================
# Packages to import
# =============================================================================
import sys
from OCC.Display.SimpleGui import *
from OCC.BRepTools import breptools_Read, breptools_Write
from OCC.TopoDS import * #TopoDS_Shape, TopoDS_Compound
from OCC.BRep import BRep_Builder
# =============================================================================
# Functions called from some menu-items
# =============================================================================
def draw_nothing(event=None):
    pass

def draw_lineandvertices(event=None):
    Line_1 = TopoDS_Shape()
    Vertex_1 = TopoDS_Shape()
    Vertex_2 = TopoDS_Shape()
    builder = BRep_Builder()
    builder1 = BRep_Builder()
    compound = TopoDS_Compound()
    builder1.MakeCompound(compound)
    breptools_Read(Line_1, 'Line_1.brep', builder)
    breptools_Read(Vertex_1, 'Vertex_1.brep', builder)
    breptools_Read(Vertex_2, 'Vertex_2.brep', builder)
    builder1.Add(compound,Line_1)
    builder1.Add(compound,Vertex_1)
    builder1.Add(compound,Vertex_2)

    #display.DisplayShape({Line_1, Vertex_1, Vertex_2}, update=True)
    #display.DisplayShape(Group_1, update=True)
    display.DisplayShape(compound, update=True)
    breptools_Write(compound, 'compound.brep')

    display.FitAll()

def save(event=None):

    breptools_Write(display)

def exit(event=None):
    sys.exit()
# =============================================================================
# Main-part: If this script is running as a main script, i.e. it
# is directly called by Python the following is executed.
# =============================================================================
if __name__ == '__main__':
# OCC.Display.SimpleGui.init_display() returns multiple
# values which are assigned here
    display, start_display, add_menu, add_function_to_menu = \
    init_display()
# This is the place where we hook our functionality to menus
# ----------------------------------------------------------
    add_menu('File')
    add_function_to_menu('File', exit)
    add_function_to_menu('File', save)
    add_menu('Draw')
    add_function_to_menu('Draw', draw_nothing)
    add_function_to_menu('Draw', draw_lineandvertices)
    start_display()
