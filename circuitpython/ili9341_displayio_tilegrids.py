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
sprite_sheet, palette = adafruit_imageload.load("/castle_sprite_sheet.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

# Create the sprite TileGrid
sprite = displayio.TileGrid(sprite_sheet, pixel_shader=palette,
                            width = 1,
                            height = 1,
                            tile_width = 16,
                            tile_height = 16,
                            default_tile = 0)

# Create the castle TileGrid
castle = displayio.TileGrid(sprite_sheet, pixel_shader=palette,
                            width = 6,
                            height = 5,
                            tile_width = 16,
                            tile_height = 16)

# Create a Group to hold the sprite and add it
sprite_group = displayio.Group()
sprite_group.append(sprite)

# Create a Group to hold the castle and add it
castle_group = displayio.Group(scale=3)
castle_group.append(castle)

# Create a Group to hold the sprite and castle
group = displayio.Group()

# Add the sprite and castle to the group
group.append(castle_group)
group.append(sprite_group)

# Castle tile assignments
# corners
castle[0, 0] = 3  # upper left
castle[5, 0] = 5  # upper right
castle[0, 4] = 9  # lower left
castle[5, 4] = 11 # lower right
# top / bottom walls
for x in range(1, 5):
    castle[x, 0] = 4  # top
    castle[x, 4] = 10 # bottom
# left/ right walls
for y in range(1, 4):
    castle[0, y] = 6 # left
    castle[5, y] = 8 # right
# floor
for x in range(1, 5):
    for y in range(1, 4):
        castle[x, y] = 7 # floor

# put the sprite somewhere in the castle
sprite.x = 110
sprite.y = 70

# Add the Group to the Display
display.root_group = group

# Loop forever so you can enjoy your image
while True:
    pass
