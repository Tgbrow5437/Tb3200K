import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "P:/py3200k/tb3200k/ExResults/Exercise06"
arcpy.CreateFileGDB_management("P:/py3200k/tb3200k/ExResults/Exercise06/Results", "NM.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdesc = arcpy.Describe(fc)
    arcpy.CopyFeatures_management(fc, "P:/py3200k/tb3200k/ExResults/Exercise06/Results" + fc)
    
    
