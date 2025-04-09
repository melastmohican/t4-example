import board,busio, os
from time import sleep
from fourwire import FourWire
import adafruit_ili9341
import displayio
import time

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_dc   = board.D10
tft_cs   = board.D9
tft_rst  = board.D8

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

bitmap = displayio.OnDiskBitmap("/0.bmp")
bitmap1 = displayio.OnDiskBitmap("/1.bmp")
bitmap2 = displayio.OnDiskBitmap("/2.bmp")
group = displayio.Group()
display.root_group = group

while True:
    tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)
    group.append(tile_grid)
    sleep(8)
    tile_grid = displayio.TileGrid(bitmap1, pixel_shader=bitmap1.pixel_shader)
    group.append(tile_grid)
    sleep(8)
    tile_grid = displayio.TileGrid(bitmap2, pixel_shader=bitmap2.pixel_shader)
    group.pop()
    group.append(tile_grid)
    sleep(8)