##Copyright 2010-2014 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU Lesser General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.

from OCC.Display.SimpleGui import init_display
from OCC.BRepTools import breptools_Read
from OCC.TopoDS import TopoDS_Shape
from OCC.BRep import BRep_Builder

Line_1 = TopoDS_Shape()
Vertex_1 = TopoDS_Shape()
Vertex_2 = TopoDS_Shape()
builder = BRep_Builder()
breptools_Read(Line_1, 'Line_1.brep', builder)
breptools_Read(Vertex_1, 'Vertex_1.brep', builder)
breptools_Read(Vertex_2, 'Vertex_2.brep', builder)

display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(Line_1, update=True)
display.DisplayShape(Vertex_1, update=True)
display.DisplayShape(Vertex_2, update=True)
start_display()
