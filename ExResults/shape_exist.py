import arcpy
from arcpy import env
env.workspace = "P:/py3200k/tb3200k/ExResults/Exercise06"
if arcpy.Exists("cities.shp"):
    arcpy.CopyFeatures_management("cities.shp", "results/cities_copy.shp")
    
