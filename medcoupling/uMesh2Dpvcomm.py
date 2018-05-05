#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Unstructured Grid Reader'
uMesh2Dvtu = XMLUnstructuredGridReader(FileName=['uMesh2D.vtu'])

# set active source
SetActiveSource(uMesh2Dvtu)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [794, 587]

# show data in view
uMesh2DvtuDisplay = Show(uMesh2Dvtu, renderView1)
# trace defaults for the display properties.
uMesh2DvtuDisplay.ColorArrayName = [None, '']
uMesh2DvtuDisplay.GlyphType = 'Arrow'
uMesh2DvtuDisplay.ScalarOpacityUnitDistance = 0.8270371084000276

# reset view to fit data
renderView1.ResetCamera()

# change representation type
uMesh2DvtuDisplay.SetRepresentationType('Surface With Edges')

# current camera placement for renderView1
renderView1.CameraPosition = [0.5267926415027674, -1.4023409836780156, 0.9011135604362469]
renderView1.CameraFocalPoint = [0.16163138737724111, 0.16666181632204152, -0.040664524982356814]
renderView1.CameraViewUp = [-0.10137084354441804, 0.49454628882078217, 0.8632195087535294]
renderView1.CameraParallelScale = 0.7071067811865476

# save screenshot
SaveScreenshot('uMesh2D.png', magnification=1, quality=100, view=renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.558643393096727, -1.3230701115705277, 1.0219006480695363]
renderView1.CameraFocalPoint = [0.1782057042181937, 0.13591052775340323, -0.0775088066177419]
renderView1.CameraViewUp = [-0.11661913617593396, 0.5781303714756785, 0.8075674898452594]
renderView1.CameraParallelScale = 0.7071067811865476

#### uncomment the following to render all views
RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
