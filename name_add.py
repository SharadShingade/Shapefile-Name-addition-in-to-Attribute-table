import arcpy
import os

# Set the ArcPy workspace to the directory that contains your input shapefiles
arcpy.env.workspace = r'D:\#Indian_Urban_Expansion\#Processing\Boundaries_Additional_10_cities\10_add_cities_shapefile'


# Get a list of shapefiles in the workspace
fcs_in = arcpy.ListFeatureClasses()
print 'fcs_in:', fcs_in

fn_source_field = 'CITY_NAME'

# Iterate over the shapefiles
for fc in fcs_in:
    print 'fc:', fc
    # Get the shapefile's name without the extension
    name = os.path.splitext(fc)[0]
    # Add the source field to the shapefile
    arcpy.AddField_management(fc, fn_source_field, 'TEXT')
    # Iterate over the rows, populating the source field with the shapefile's
    #   name
    with arcpy.da.UpdateCursor(fc, fn_source_field) as cur:
        for row in cur:
            row[0] = name
            cur.updateRow(row)

# The path/name of your output, merged shapefile
fc_output = r'D:\#Indian_Urban_Expansion\#Processing\Boundaries_Additional_10_cities\10_add_cities_merge.shp'
# Merge the shapefiles
arcpy.Merge_management(fcs_in, fc_output)
