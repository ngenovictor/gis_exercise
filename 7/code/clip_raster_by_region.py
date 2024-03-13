import fiona
import rasterio
import rasterio.mask


def clip_raster_by_extents(input_raster_file_path, region_file_path, output_file_path):
    with rasterio.open(input_raster_file_path) as ds, fiona.open(region_file_path, "r") as region:
        shape = region[0]["geometry"]
        out_image, _ = rasterio.mask.mask(ds, [shape], crop=True)
        out_meta = ds.meta

    out_meta.update({"region": "test roi"})

    with rasterio.open(output_file_path, "w", **out_meta) as dest:
        dest.write(out_image)


if __name__ == "__main__":
    clip_raster_by_extents(
        "/app/data/S2B_MSIL2A_20221127T075159_N0400_R135_T36NXF_20221127T100500.SAFE/GRANULE/L2A_T36NXF_A029905_20221127T080452/IMG_DATA/R10m/T36NXF_20221127T075159_AOT_10m.jp2",
        "/app/data/region_of_interest.geojson",
        "clipped.jp2",
    )
