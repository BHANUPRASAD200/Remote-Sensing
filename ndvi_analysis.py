import rasterio
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load NDVI images
ndvi_berambadi_file = "NDVI_Berambadi.tif"
ndvi_chennai_file = "NDVI_Chennai.tif"

# Read Berambadi NDVI
with rasterio.open(ndvi_berambadi_file) as src:
    ndvi_berambadi = src.read(1)

# Read Chennai NDVI
with rasterio.open(ndvi_chennai_file) as src:
    ndvi_chennai = src.read(1)

# ✅ Step 1: Display NDVI Images
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].imshow(ndvi_berambadi, cmap='RdYlGn')
ax[0].set_title("NDVI - Berambadi")
ax[0].axis("off")

ax[1].imshow(ndvi_chennai, cmap='RdYlGn')
ax[1].set_title("NDVI - Chennai")
ax[1].axis("off")

plt.colorbar(ax[1].imshow(ndvi_chennai, cmap='RdYlGn'), ax=ax, orientation="horizontal")
plt.show()


# ✅ Step 2: NDVI Classification for Vegetation Health
def classify_ndvi(value):
    if value < 0.2:
        return 0  # Barren land
    elif 0.2 <= value < 0.5:
        return 1  # Sparse vegetation
    elif 0.5 <= value < 0.8:
        return 2  # Healthy vegetation
    else:
        return 3  # Dense vegetation

# Apply classification
ndvi_classified_berambadi = np.vectorize(classify_ndvi)(ndvi_berambadi)
ndvi_classified_chennai = np.vectorize(classify_ndvi)(ndvi_chennai)

# Display Classified NDVI
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].imshow(ndvi_classified_berambadi, cmap="viridis")
ax[0].set_title("Classified NDVI - Berambadi")
ax[0].axis("off")

ax[1].imshow(ndvi_classified_chennai, cmap="viridis")
ax[1].set_title("Classified NDVI - Chennai")
ax[1].axis("off")

plt.colorbar(ax[1].imshow(ndvi_classified_chennai, cmap="viridis"), ax=ax, orientation="horizontal")
plt.show()


# ✅ Step 3: Save Processed NDVI as GeoTIFF
def save_ndvi(output_file, data, src_file):
    with rasterio.open(src_file) as src:
        profile = src.profile
        profile.update(dtype=rasterio.uint8, count=1)

        with rasterio.open(output_file, "w", **profile) as dst:
            dst.write(data.astype(rasterio.uint8), 1)

save_ndvi("NDVI_Classified_Berambadi.tif", ndvi_classified_berambadi, ndvi_berambadi_file)
save_ndvi("NDVI_Classified_Chennai.tif", ndvi_classified_chennai, ndvi_chennai_file)

print("Classified NDVI images saved!")


# ✅ Step 4: K-Means Clustering for Land Cover Segmentation
# Flatten NDVI data for clustering
ndvi_flattened_berambadi = ndvi_berambadi.reshape(-1, 1)
ndvi_flattened_chennai = ndvi_chennai.reshape(-1, 1)

# Apply K-Means Clustering (3 land classes)
kmeans_berambadi = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_chennai = KMeans(n_clusters=3, random_state=42, n_init=10)

kmeans_berambadi.fit(ndvi_flattened_berambadi)
kmeans_chennai.fit(ndvi_flattened_chennai)

ndvi_kmeans_berambadi = kmeans_berambadi.labels_.reshape(ndvi_berambadi.shape)
ndvi_kmeans_chennai = kmeans_chennai.labels_.reshape(ndvi_chennai.shape)

# Display K-Means Classified Images
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].imshow(ndvi_kmeans_berambadi, cmap="coolwarm")
ax[0].set_title("K-Means Clustering - Berambadi")
ax[0].axis("off")

ax[1].imshow(ndvi_kmeans_chennai, cmap="coolwarm")
ax[1].set_title("K-Means Clustering - Chennai")
ax[1].axis("off")

plt.colorbar(ax[1].imshow(ndvi_kmeans_chennai, cmap="coolwarm"), ax=ax, orientation="horizontal")
plt.show()


# ✅ Step 5: Compare NDVI Trends Between Berambadi & Chennai
# Compute mean NDVI values
mean_ndvi_berambadi = np.mean(ndvi_berambadi)
mean_ndvi_chennai = np.mean(ndvi_chennai)

# Plot NDVI Comparison
plt.figure(figsize=(8, 5))
plt.bar(["Berambadi", "Chennai"], [mean_ndvi_berambadi, mean_ndvi_chennai], color=["green", "blue"])
plt.ylabel("Mean NDVI Value")
plt.title("NDVI Comparison: Berambadi vs Chennai")
plt.show()
