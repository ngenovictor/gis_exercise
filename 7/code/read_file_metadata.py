from osgeo import gdal


def get_metadata(file_path):
    ds = gdal.Open(file_path)
    metadata = ds.GetMetadata()
    print(metadata)


if __name__ == "__main__":
    get_metadata(
        "/app/data/S2B_MSIL2A_20221127T075159_N0400_R135_T36NXF_20221127T100500.SAFE/GRANULE/L2A_T36NXF_A029905_20221127T080452/IMG_DATA/R10m/T36NXF_20221127T075159_AOT_10m.jp2"
    )
