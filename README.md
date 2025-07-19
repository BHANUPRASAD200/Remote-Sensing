# Remote Sensing and Satellite Imagery Analysis

This project focuses on the application of remote sensing and satellite imagery techniques for land cover classification and change detection. It utilizes **Google Earth Engine (GEE)** to retrieve satellite data (Sentinel-2 for NDVI and Sentinel-1 for backscatter) and **Python** with libraries like `rasterio`, `numpy`, `matplotlib`, and `scikit-learn` for image processing and analysis, including **K-Means clustering**.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Getting Started](#getting-started)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Results](#results)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

## Project Overview

Remote sensing plays a crucial role in monitoring Earth's surface without direct contact. This project demonstrates various digital image processing (DIP) techniques applied to remote sensing images obtained from satellite sensors.

**Core stages covered:**

- **Image Pre-processing**: Correcting radiometric, atmospheric, and geometric distortions.
- **Enhancement**: Techniques to effectively display images for visual interpretation.
- **Transformation**: Generating NDVI to highlight vegetation.
- **Classification**: Grouping pixels into thematic land cover maps.

This project analyzes two study areas: **Berambadi Watershed** and **Chennai**, comparing NDVI values and applying **K-Means clustering**.

---

## Features

- 🌍 **Google Earth Engine Integration**  
- 📍 **AOI Definition**: Berambadi & Chennai  
- 🌿 **NDVI Calculation (Sentinel-2)**  
- 📡 **Backscatter Retrieval (Sentinel-1 VV & VH)**  
- 📤 **Export to Google Drive (GeoTIFFs)**  
- 🗺️ **Interactive Map Visualization using Folium**  
- 🧮 **NDVI Classification**  
  - 0: Barren land (NDVI < 0.2)  
  - 1: Sparse vegetation (0.2 ≤ NDVI < 0.5)  
  - 2: Healthy vegetation (0.5 ≤ NDVI < 0.8)  
  - 3: Dense vegetation (NDVI ≥ 0.8)
- 🎯 **K-Means Clustering for Land Cover Segmentation**  
- 📊 **NDVI Trend Comparison between AOIs**  
- 🖼️ **GeoTIFF Output and Visualization**

---

## Getting Started

Follow these instructions to get the project up and running on your local machine.

---

## Prerequisites

- Python 3.x  
- Google Earth Engine (GEE) account and authentication setup

---

## Installation

### Install Required Libraries:

```bash
pip install earthengine-api folium matplotlib numpy rasterio scikit-learn
```

### Or use the full stack:

```bash
pip install geemap ee gdal rasterio numpy opencv-python geopandas matplotlib
```

---

## Google Earth Engine Authentication

### Authenticate GEE:

```python
import ee
ee.Authenticate()
```

### Initialize GEE:

```python
ee.Initialize(project='remote-sensing-454607')  # Replace with your actual GEE project ID if needed
```

---

## Usage

### Jupyter Notebook (`remote-sensing-2.ipynb`)

#### Launch the notebook:

```bash
jupyter notebook remote-sensing-2.ipynb
```

#### Run cells step-by-step:

1. Install dependencies  
2. Define AOIs (Berambadi & Chennai)  
3. Retrieve NDVI (Sentinel-2)  
4. Retrieve Backscatter (Sentinel-1)  
5. Export to Drive  
6. Display AOIs on interactive maps  

---

### Python Script (`ndvi_analysis.py`)

Ensure exported files like `NDVI_Berambadi.tif` and `NDVI_Chennai.tif` are present in the script directory.

#### Run:

```bash
python ndvi_analysis.py
```

This will:

- Display raw NDVI images  
- Classify NDVI into 4 vegetation classes  
- Save classified NDVI GeoTIFFs  
- Perform K-Means clustering  
- Compare NDVI between regions via bar plots  

---

## Project Structure

```bash
.
├── remote sensing and satellite imangery jounrial papers FINAL.pdf
├── remote-sensing-2.ipynb
├── ndvi_analysis.py
├── Berambadi.jpg
├── chennai.jpg
├── k-means clustering.jpg
├── NDVI maps of Berambadi & Chennai.jpg
├── NDVI_VALUES.jpg
├── READ.ME
└── README.md
```

---

## Results

### Visual Outputs:

- ✅ **NDVI Maps**: Vegetation health  
- ✅ **Classified NDVI**: 4-class vegetation maps  
- ✅ **K-Means Clustered Maps**  
- ✅ **AOI Maps**: Folium-based visuals  
- ✅ **NDVI Trend Comparison**: Bar plots  

---

## Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a branch:  
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit changes:  
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to GitHub:  
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License**.

---

## Contact

**R. Bhanu Prasad**  
📧 raminenibhanu2004@gmail.com
🌐 https://bhanuprasad.vercel.app/
