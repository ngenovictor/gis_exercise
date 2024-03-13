import subprocess

import rasterio


def compute_ndvi(NIR_path, R_path, output_path):
    command = f'gdal_calc.py -A {NIR_path} -B {R_path} --outfile {output_path} --calc "(A-B)/(A+B)"'
    subprocess.check_call(command, shell=True)
    return output_path


def read_image_stats(file_path):
    with rasterio.open(file_path) as ds:
        data = ds.read(1)
        return (data.min(), data.max(), data.mean(), data.median(), data.std())


if __name__ == "__main__":
    ndvi_path = compute_ndvi(
        "/app/data/S2B_MSIL2A_20221127T075159_N0400_R135_T36NXF_20221127T100500.SAFE/GRANULE/L2A_T36NXF_A029905_20221127T080452/IMG_DATA/R10m/T36NXF_20221127T075159_B08_10m.jp2",
        "/app/data/S2B_MSIL2A_20221127T075159_N0400_R135_T36NXF_20221127T100500.SAFE/GRANULE/L2A_T36NXF_A029905_20221127T080452/IMG_DATA/R10m/T36NXF_20221127T075159_B04_10m.jp2",
        "ndvi.tiff",
    )
    print(read_image_stats(ndvi_path))
