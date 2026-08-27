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
  based on ISO topic categories, mirroring the layout of
  \\\\ABMI-DATA2\\science\\spatial_data. Each top-level folder
  corresponds to a topic category and holds a `readme.txt` with
  the category's description and example data types.

  Each dataset gets its own folder directly beneath the category
  matching its primary thematic content.

  A `_temp` folder is created for staging data that is not yet
  ready to be filed.

  Only the categories currently in use on the share are created.
  The management guide defines seven more -- health,
  intelligenceMilitary, oceans, planningCadastre, society,
  structure, utilitiesCommunication -- which are deliberately
  omitted.
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

## Listed in ISO 19115 register order. Names are lowerCamelCase and
## must match the register exactly -- do not rename, abbreviate, or
## re-case them.

iso_topic_categories = {
    "farming": {
        "description": "Rearing of animals and/or cultivation of "
                       "plants.",
        "examples": "Agriculture, irrigation, aquaculture, plantations, "
                    "herding, pests and diseases affecting crops and "
                    "livestock."
    },
    "biota": {
        "description": "Flora and/or fauna in natural environments.",
        "examples": "Wildlife, vegetation, biological sciences, ecology, "
                    "wilderness areas, wetlands, habitat."
    },
    "boundaries": {
        "description": "Legal land descriptions.",
        "examples": "Political and administrative boundaries."
    },
    "climatologyMeteorologyAtmosphere": {
        "description": "Processes and phenomena of the atmosphere.",
        "examples": "Cloud cover, weather, climate, atmospheric conditions, "
                    "climate change, precipitation."
    },
    "economy": {
        "description": "Economic activities, conditions, and employment.",
        "examples": "Production, labor, revenue, commerce, industry, tourism, "
                    "forestry, fisheries, commercial or subsistence hunting."
    },
    "elevation": {
        "description": "Height above or below sea level.",
        "examples": "Altitude, bathymetry, digital elevation models, slope, "
                    "derived products."
    },
    "environment": {
        "description": "Environmental resources, protection, and "
                       "conservation.",
        "examples": "Environmental pollution, waste storage and treatment, "
                    "environmental impact assessment, monitoring "
                    "environmental risk, nature reserves."
    },
    "geoscientificInformation": {
        "description": "Information pertaining to earth sciences.",
        "examples": "Geology, minerals, geophysical features and processes, "
                    "hydrology, glacial geology, erosion, geomorphology, "
                    "sedimentation."
    },
    "imageryBaseMapsEarthCover": {
        "description": "Base maps.",
        "examples": "Land cover, topographic maps, imagery, annotations."
    },
    "inlandWaters": {
        "description": "Inland water features, drainage systems, and their "
                       "characteristics.",
        "examples": "Rivers and glaciers, salt lakes, water utilization plans, "
                    "dams, currents, floods, water quality, hydrographic "
                    "charts."
    },
    "location": {
        "description": "Positional information and services.",
        "examples": "Addresses, geodetic networks, control points, postal "
                    "zones, place names, and reference grids."
    },
    "transportation": {
        "description": "Means and aids for conveying persons and/or goods.",
        "examples": "Roads, airports, airstrips, shipping routes, tunnels, "
                    "nautical charts, vehicle and vessel locations, "
                    "aeronautical charts, railways, trails."
    }
}

# 3. Create Directory Structure
# -----------------------------

## 3.1 Define Base Directory
base_dir = "spatial_data"
os.makedirs(base_dir, exist_ok=True)

## 3.2 Create Temp Folder
temp_dir = os.path.join(base_dir, "_temp")
os.makedirs(temp_dir, exist_ok=True)

temp_readme_path = os.path.join(temp_dir, "readme.txt")
with open(temp_readme_path, "w") as temp_readme:
    temp_text = (
        "Staging area for spatial data that is not yet ready to be "
        "filed. Data belongs here while it still needs preprocessing, "
        "while its readme files are being written, or while finished "
        "data is being checked before it moves. "
        "Give each item its own subfolder named for its product_id. "
        "Nothing here is catalogued, and nothing here should be used "
        "in an analysis or referenced by a script. Move an item to its "
        "thematic folder once it has a product folder with a complete "
        "readme.txt -- and, where the product is held at more than one "
        "resolution, CRS, or grid alignment, a variant subfolder with "
        "its own readme.txt -- then delete the staged copy."
    )
    temp_readme.write(wrap_text(temp_text))
print("Created _temp folder and its readme.txt file.")

## 3.3 Create Topic Category Folders
## Each category holds only its readme.txt. Dataset folders are added
## beneath it as data is acquired; there are no sub-theme folders.
for category, content in iso_topic_categories.items():
    category_path = os.path.join(base_dir, category)
    os.makedirs(category_path, exist_ok=True)

    # Create readme.txt file for the category
    readme_path = os.path.join(category_path, "readme.txt")
    with open(readme_path, "w") as readme_file:
        category_text = (
            f"Category: {category}\n\n"
            f"Description: {wrap_text(content['description'])}\n\n"
            f"Examples: {wrap_text(content['examples'])}\n"
        )
        readme_file.write(category_text)

    print(f"Created folder and readme.txt for: {category}")

# End of script
# -------------
print("Spatial data directory structure with readme.txt files created "
      "successfully.")
