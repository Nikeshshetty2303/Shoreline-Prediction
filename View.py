from osgeo import gdal
import matplotlib.pyplot as plt

# Open the TIFF image
image_path = "hyperspectral_image/2022.tif"
ds = gdal.Open(image_path)

# Check if the file is successfully opened
if ds is None:
    print("Failed to open the TIFF file.")
else:
    # Specify the bands you want to display
    bands_to_display = [1, 3, 5]

    # Loop through each specified band and display it
    for band_num in bands_to_display:
        if 1 <= band_num <= ds.RasterCount:
            band = ds.GetRasterBand(band_num)
            band_data = band.ReadAsArray()

            # Display the band
            plt.imshow(band_data)  # You can choose a colormap based on your image type
            plt.title(f"Band {band_num}")
            plt.show()

    # Close the dataset
    ds = None
