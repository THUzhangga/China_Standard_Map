# coding=utf-8
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.ticker as mticker
import cartopy.io.shapereader as shpreader
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

crs = ccrs.AlbersEqualArea(central_longitude=110,
                           central_latitude=30,
                           standard_parallels=(25, 47))
ax = plt.axes(projection=crs)
extent = (65, 155, -5, 50)

# 矩形框四个顶点经纬度，分别是左上、右下、左下、右上，并将经纬度转换为Albers坐标系下坐标
coord1 = crs.transform_point(64.2268, 47.4315, ccrs.PlateCarree())
coord2 = crs.transform_point(130.8653846, -3.230294, ccrs.PlateCarree())
coord3 = crs.transform_point(84.3670886, -4.7107438, ccrs.PlateCarree())
coord4 = crs.transform_point(148.033707865, 49.6830986, ccrs.PlateCarree())

# 读入标准地图
fname = 'china_crop.png'
img = plt.imread(fname)
img_extent = (
    coord1[0], coord4[0], coord3[1], coord1[1]
)  # extent=[longitude_top_left,longitude_top_right,latitude_bottom_left,latitude_top_left]

ax.set_extent(extent)
shp_path = "shp/loess_plateau.shp"
bound = shpreader.Reader(shp_path).geometries()
ax.add_geometries(bound,
                  ccrs.PlateCarree(),
                  edgecolor='red',
                  facecolor='none',
                  linewidth=2,
                  zorder=10)  # 添加黄土高原边界
ax.imshow(img, origin='upper', extent=img_extent)  # 载入标准地图

# 以下代码可添加海岸线、经纬网等
ax.coastlines(linestyle='-')
gl = ax.gridlines(draw_labels=True)
gl.xlocator = mticker.FixedLocator(range(65, 150, 5))
gl.ylocator = mticker.FixedLocator(range(-5, 50, 5))
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
plt.show()