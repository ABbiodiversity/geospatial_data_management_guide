"""
---
title: Create Spatial Data Directory
author: Brendan Casey
created: 2024-12-11
inputs: None
outputs: Creates a structured directory based on ISO topic categories. 
         Generates `readme.txt` files with default descriptions of 
         each top level folder in the directory. 
notes: 
  This script creates a structured directory for spatial data
  based on ISO topic categories. Each top-level folder corresponds
  to a topic category and contains subfolders for specific data
  types. Each top-level folder includes a `readme.txt` file with
  the category's description and example data types. A `_temp`
  folder is created for staging data that is not yet ready to
  be filed.
---
"""

# 1. Setup
# --------

## 1.1 Import Required Libraries
import os
import textwrap

## 1.2 Define Helper Function
def wrap_text(text, width=70):
    """
    Wraps the input text to a specified line width.

    Parameters
    ----------
    text : str
        The input text to be wrapped.
    width : int, optional
        The line width to wrap the text to (default is 70).
    
    Returns
    -------
    str
        The wrapped text.
    """
    return "\n".join(textwrap.wrap(text, width=width))

# 2. Define ISO Topic Categories
# ------------------------------

iso_topic_categories = {
    "farming": {
        "description": "Rearing of animals and/or cultivation of "
                       "plants.",
        "examples": "Agriculture, irrigation, aquaculture, plantations, "
                    "herding, pests and diseases affecting crops and "
                    "livestock.",
        "subfolders": ["agriculture", "irrigation"]
    },
    "biota": {
        "description": "Flora and/or fauna in natural environments.",
        "examples": "Wildlife, vegetation, biological sciences, ecology, "
                    "wilderness areas, wetlands, habitat.",
        "subfolders": ["wildlife", "vegetation", "ecology", "wetlands"]
    },
    "boundaries": {
        "description": "Legal land descriptions.",
        "examples": "Political and administrative boundaries.",
        "subfolders": ["administrativeBoundaries"]
    },
    "climatologyMeteorologyAtmosphere": {
        "description": "Processes and phenomena of the atmosphere.",
        "examples": "Cloud cover, weather, climate, atmospheric conditions, "
                    "climate change, precipitation.",
        "subfolders": ["temperature", "atmosphericConditions", 
                       "precipitation"]
    },
    "economy": {
        "description": "Economic activities, conditions, and employment.",
        "examples": "Production, labor, revenue, commerce, industry, tourism, "
                    "forestry, fisheries, commercial or subsistence hunting.",
        "subfolders": ["forestry", "energy"]
    },
    "elevation": {
        "description": "Height above or below sea level.",
        "examples": "Altitude, bathymetry, digital elevation models, slope, "
                    "derived products.",
        "subfolders": ["DEM", "terrainAnalysis"]
    },
    "environment": {
        "description": "Environmental resources, protection, and "
                       "conservation.",
        "examples": "Environmental pollution, waste storage and treatment, "
                    "environmental impact assessment, monitoring "
                    "environmental risk, nature reserves.",
        "subfolders": ["pollution", "environmentalImpact", 
                       "riskMonitoring"]
    },
    "geoscientificInformation": {
        "description": "Information pertaining to earth sciences.",
        "examples": "Geology, minerals, geophysical features and processes, "
                    "hydrology, glacial geology, erosion, geomorphology, "
                    "sedimentation.",
        "subfolders": ["geology", "soil"]
    },
    "imageryBaseMapsEarthCover": {
        "description": "Base maps.",
        "examples": "Land cover, topographic maps, imagery, annotations.",
        "subfolders": ["landCover", "satelliteImagery"]
    },
    "inlandWaters": {
        "description": "Inland water features, drainage systems, and their "
                       "characteristics.",
        "examples": "Rivers and glaciers, salt lakes, water utilization plans, "
                    "dams, currents, floods, water quality, hydrographic "
                    "charts.",
        "subfolders": ["rivers", "lakes", "waterQuality"]
    },
    "transportation": {
        "description": "Means and aids for conveying persons and/or goods.",
        "examples": "Roads, airports, airstrips, shipping routes, tunnels, "
                    "nautical charts, vehicle and vessel locations, "
                    "aeronautical charts, railways, trails.",
        "subfolders": ["roads"]
    }
}

# 3. Create Directory Structure
# -----------------------------

## 3.1 Define Base Directory
base_dir = "spatialData"
os.makedirs(base_dir, exist_ok=True)

## 3.2 Create Temp Folder
temp_dir = os.path.join(base_dir, "_temp")
os.makedirs(temp_dir, exist_ok=True)

temp_readme_path = os.path.join(temp_dir, "readme.txt")
with open(temp_readme_path, "w") as temp_readme:
    temp_text = (
        "Staging area for spatial data that is not yet ready to be "
        "filed. Data belongs here while it still needs preprocessing, "
        "while its product and variant readme files are being written, "
        "or while a finished variant is being checked before it moves. "
        "Give each item its own subfolder named for its product_id. "
        "Nothing here is catalogued, and nothing here should be used "
        "in an analysis or referenced by a script. Move an item to its "
        "thematic folder once it has a product folder with at least "
        "one variant subfolder and a readme.txt at both levels, then "
        "delete the staged copy."
    )
    temp_readme.write(wrap_text(temp_text))
print("Created _temp folder and its readme.txt file.")

## 3.3 Create Topic Category Folders
for category, content in iso_topic_categories.items():
    category_path = os.path.join(base_dir, category)
    os.makedirs(category_path, exist_ok=True)

    # Create subfolders for each category
    for subfolder in content["subfolders"]:
        subfolder_path = os.path.join(category_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)

    # Create readme.txt file for the category
    readme_path = os.path.join(category_path, "readme.txt")
    with open(readme_path, "w") as readme_file:
        category_text = (
            f"Category: {category}\n\n"
            f"Description: {wrap_text(content['description'])}\n\n"
            f"Examples: {wrap_text(content['examples'])}\n"
        )
        readme_file.write(category_text)
    
    print(f"Created folder structure and readme.txt for: {category}")

# End of script
# -------------
print("Spatial data directory structure with readme.txt files created "
      "successfully.")
