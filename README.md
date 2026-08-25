<img src="figures/abmi_logo.png" alt="ABMI Logo" width="300" style="margin-top: 40px;">


# Geospatial Data Management Guide
![In Development](https://img.shields.io/badge/Status-In%20Development-yellow)
![Lifecycle](https://img.shields.io/badge/Lifecycle-Experimental-orange)
![Languages](https://img.shields.io/badge/Languages-R-blue)


> [!IMPORTANT]
> This reposotory is developed by and for the Science Centre at the Alberta Biodiversity Monitoring
Institute (ABMI). It is intended for internal use.
> 

Guidelines for the internal management of geospatial data at the ABMI Science Centre, along with a catalogue snapshot of the geospatial datasets the Science Centre holds and maintains.

---

## Table of Contents
- [Data Catalogs](#data-catalogs)
- [Scripts for Extracting and Processing Spatial Data](#scripts-for-extracting-and-processing-spatial-data)
- [Data Storage](#data-storage)
- [Metadata Standards](#metadata-standards)

---

## Data Catalogs

### Internal Catalog
- Spatial data stored on the Science Centre's server: 
  - [Predictor Variable List](predictor_variable_list.csv)

### External Catalogs

- [Alberta Government Open Data](https://open.alberta.ca/opendata)
- [AltaLIS Open Data](https://www.altalis.com/)
- [Arctic-Boreal Vulnerability Experiment (ABoVE) Products](https://daac.ornl.gov/cgi-bin/dataset_lister.pl?p=34)
- [Awesome GEE Community Catalog](https://developers.google.com/earth-engine/datasets)
- [Google Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets)
- [National Terrestrial Ecosystem Monitoring System for Canada (NTEMS)](https://opendata.nfis.org/mapserver/nfis-change_eng.html)

**Spectral Indices**

- [Awesome Spectral Indices](https://github.com/awesome-spectral-indices/awesome-spectral-indices?tab=readme-ov-file)

---

## Scripts for Extracting and Processing Spatial Data

- [internal `sciSpatialR` package](https://github.com/ABbiodiversity/sciSpatialR)

---

## Data Storage

Once downloaded, data should be stored in a spatial data directory in folders organized by data thematic type. The script [create_spatial_data_dir.py](scripts/create_spatial_data_dir.py) can be used to create an empty directory. Each spatial dataset should be stored in a subfolder stored within the corresponding thematic folder. Thematic folders are based on [ISO 19115 Topic Categories](https://nap.geogratis.gc.ca/metadata/register/registerItems-eng.html#RI_653). 

**Table 1.** Thematic directories for organizing geospatial data, directory descriptions, and examples of corresponding geospatial data.

| **Folder (ISO Topic Category Name)** | **Description**                                                                  | **Examples**                                                                                                                                                                       |
| ------------------------------------ | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **farming**                          | Rearing of animals and/or cultivation of plants.                                 | Agriculture, irrigation, aquaculture, plantations, herding, pests and diseases affecting crops and livestock.                                                                      |
| **biota**                            | Flora and/or fauna in natural environments.                                      | Wildlife, vegetation, biological sciences, ecology, wilderness areas, wetlands, habitat.                                                                                           |
| **boundaries**                       | Legal land descriptions.                                                         | Political and administrative boundaries.                                                                                                                                           |
| **climatologyMeteorologyAtmosphere** | Processes and phenomena of the atmosphere.                                       | Cloud cover, weather, climate, atmospheric conditions, climate change, precipitation.                                                                                              |
| **economy**                          | Economic activities, conditions, and employment.                                 | Production, labor, revenue, commerce, industry, tourism, forestry, fisheries, commercial or subsistence hunting.                                                                   |
| **elevation**                        | Height above or below sea level.                                                 | Altitude, bathymetry, digital elevation models, slope, derived products.                                                                                                           |
| **environment**                      | Environmental resources, protection, and conservation.                           | Environmental pollution, waste storage and treatment, environmental impact assessment, monitoring environmental risk, nature reserves.                                             |
| **geoscientificInformation**         | Information pertaining to earth sciences.                                        | Geology, minerals, geophysical features and processes, hydrology, glacial geology, erosion, geomorphology, sedimentation.                                                          |
| **health**                           | Health, health services, human ecology, and safety.                              | Disease, illness, public health, health services.                                                                                                                                  |
| **imageryBaseMapsEarthCover**        | Base maps.                                                                       | Land cover, topographic maps, imagery.                                                                                                                                |
| **intelligenceMilitary**             | Military bases, structures, activities.                                          | Barracks, training grounds, military transportation, information collection.                                                                                                       |
| **inlandWaters**                     | Inland water features, drainage systems, and their characteristics.              | Rivers and glaciers, salt lakes, water utilization plans, dams, currents, floods, water quality, hydrographic charts.                                                              |
| **location**                         | Positional information and services.                                             | Addresses, geodetic networks, control points, postal zones, place names.                                                                                                           |
| **oceans**                           | Features and characteristics of salt water bodies (excluding inland waters).     | Tides, tidal waves, coastal information, reefs.                                                                                                                                    |
| **planningCadastre**                 | Information used for appropriate actions for future use of the land.             | Land use maps, zoning maps, cadastral surveys, land ownership.                                                                                                                     |
| **society**                          | Characteristics of society and culture.                                          | Settlements, anthropology, archaeology, education, traditional beliefs, manners and customs, demographic data, recreational areas and activities.                                  |
| **structure**                        | Man-made construction.                                                           | Buildings, museums, churches, factories, housing, monuments, shops, towers.                                                                                                        |
| **transportation**                   | Means and aids for conveying persons and/or goods.                               | Roads, airports, airstrips, shipping routes, tunnels, nautical charts, vehicle and vessel locations, aeronautical charts, railways, trails.                                        |
| **utilitiesCommunication**           | Energy, water and waste systems, and communications infrastructure and services. | Hydro-electricity, geothermal, solar and nuclear sources of energy, water purification, sewage treatment, electricity and gas distribution, data communication, telecommunication. |

### Products and variants

Within a thematic folder, each product gets one folder. A product
is the thing the provider published: ClimateNA, ABMI Human Footprint,
NTEMS land cover. Inside it, each variant gets its own subfolder. A
variant is that same product at one resolution, CRS, and grid
alignment.

```
geoscientificInformation/
└── soilgrids_250_v2_ab/                                 # product
    ├── readme.txt                              # ← product record
    ├── native/                                 # variant
    │   ├── readme.txt                          # ← variant record
    │   └── soilgrids_250_v2_ab_native.tif
    └── abmi1km/                                # variant
        ├── readme.txt                          # ← variant record
        └── soilgrids_250_v2_ab_abmi1km.tif
```

Rules:

- **One folder per variant.** Never mix resolutions or grids in one
  folder. If the resolution, CRS, or grid origin differs, it is a
  different variant.
- **`native`** holds the data as delivered by the provider, converted
  in format only. It is the reference against which every derived
  variant can be checked.
- **Variant folder names are short and describe the grid**, not the
  processing: `native`, `abmi1km`, `abmi250m`. The full variant
  identifier is `{product_id}__{variant}`, e.g. `climate_na__abmi1km`.
- **Data filenames carry the variant suffix** so a file remains
  identifiable once it is copied out of the directory:
  `{product_id}_{measure}_{period}_{variant}.tif`.
- **Every folder at both levels holds a `readme.txt`.** A variant
  folder without one is undocumented data.

### The _temp folder

`create_spatial_data_dir.py` also creates a `_temp/` folder alongside the
thematic folders. It is the staging area for anything not yet ready to
be filed. Data sits in `_temp/` for one of three reasons:

- **It still needs preprocessing.** Raw downloads, GEE exports pulled
  from Google Drive, and raster tiles waiting to be mosaicked.
- **It has no readme yet.** The files may be final, but until the
  product and variant records are written the data cannot be filed.
- **It is being staged.** Processing and documentation are done, and
  the variant is being checked — grid alignment verified, filenames
  and sizes confirmed — before it moves.

Give each item its own subfolder in `_temp/`, named for its
`product_id`, so partly finished work is not mixed together.

Nothing in `_temp/` is catalogued, and nothing in it should be used in
an analysis or referenced by a script. It is not a second storage
location; it is a queue. Something moves out of `_temp/` once it has a
product folder with at least one variant subfolder, a `readme.txt` at
both levels, and files named with the variant suffix. Delete the
staged copy once the move is verified.

---

## Metadata Standards

Metadata is recorded in plain-text `readme.txt` files that comply with
the [North American Profile (NAP) of the ISO 19115: Geographic
Information – Metadata
Standard](https://www.fgdc.gov/standards/projects/incits-l1-standards-projects/NAP-Metadata).

Metadata is split across two levels, matching the product/variant
directory structure described in
[Section 3](#3-data-storage). Each fact is recorded once, at the level
where it is actually true.

| Record | Template | Describes |
| --- | --- | --- |
| **Product readme** — `{product}/readme.txt` | [product_metadata_template.txt](product_metadata_template.txt) | The data as published by the provider: what it is, who made it, when it covers, how it may be used, how to cite it. |
| **Variant readme** — `{product}/{variant}/readme.txt` | [variant_metadata_template.txt](variant_metadata_template.txt) | The geometry and provenance of one processed copy: resolution, CRS, extent, grid alignment, derivation, format. |

The two records read together as the full description of a file. A
variant readme does not repeat the product's title, abstract, licence,
contacts, or citation; it points at the parent record instead.

**Table 2.** Which record holds which metadata block.

| Block | Product | Variant |
| --- | :---: | :---: |
| Title, Abstract, Purpose, Credits, Language, Topic Category, Keywords | ✓ | — |
| Layers and bands (measure, units, scale, valid range, class definitions) | ✓ | — |
| Variant list | ✓ | — |
| Temporal information (publication date, extent, resolution, version) | ✓ | — |
| Lineage — the provider's processing | ✓ | — |
| Positional accuracy — as stated by the provider | ✓ | — |
| Use and access constraints | ✓ | — |
| Online resource (provider URL) | ✓ | — |
| Contact and internal steward | ✓ | — |
| Citation, DOI | ✓ | — |
| Spatial resolution | — | ✓ |
| Geographic information (CRS, extent, native extent) | — | ✓ |
| Reference grid alignment | — | ✓ |
| Derivation (input, operation, method, script, commit, version) | — | ✓ |
| Lineage — this processing step | — | ✓ |
| Positional accuracy — of this variant | — | ✓ |
| Known caveats | — | ✓ |

Two rules keep the split honest:

1. **Never repeat a product field in a variant record.** If the
   provider states ±10 m horizontal accuracy, that belongs in the
   product record. Do not restate it in a variant record; aggregating
   to 1 km invalidates it.
2. **Never put measured geometry in the product record.** The
   provider's published resolution can be described as prose in the
   product abstract, but the measured resolution, CRS, and extent of a
   file belong only to the variant that holds that file.

## Contact

For questions regarding the contents of this repository or data
access, please contact Dr. Brendan Casey at
brendan.casey@ualberta.ca.

