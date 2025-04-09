# color_setup.py Customise for your hardware config

from machine import Pin, SPI
import gc

# *** Choose your color display driver here ***
# ili9341 specific driver
from drivers.ili93xx.ili9341 import ILI9341 as SSD


pdc = Pin('D10', Pin.OUT, value=0)
prst = Pin('D8', Pin.OUT, value=1)
pcs = Pin('D9', Pin.OUT, value=1)

# Kept as ssd to maintain compatability
gc.collect()  # Precaution before instantiating framebuf
# See DRIVERS.md re overclocking the SPI bus
spi = SPI(0, baudrate=4_000_000)
ssd = SSD(spi, dc=pdc, cs=pcs, rst=prst)