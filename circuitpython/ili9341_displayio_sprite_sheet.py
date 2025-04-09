import time
import board
import displayio
import adafruit_imageload
from fourwire import FourWire
import adafruit_ili9341


# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_dc   = board.D10
tft_cs   = board.D9
tft_rst  = board.D8

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

# Load the sprite sheet (bitmap)
sprite_sheet, palette = adafruit_imageload.load("/cp_sprite_sheet.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

# Create a sprite (tilegrid)
sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette,
                            width = 1,
                            height = 1,
                            tile_width = 16,
                            tile_height = 16)

# Create a Group to hold the sprite
group = displayio.Group(scale=1)

# Add the sprite to the Group
group.append(sprite)

# Add the Group to the Display
display.root_group = group

# Set sprite location
group.x = 120
group.y = 80

# Loop through each sprite in the sprite sheet
source_index = 0
while True:
    sprite[0] = source_index % 6
    source_index += 1
    time.sleep(2)
