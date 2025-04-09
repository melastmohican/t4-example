"""
ILI9341 demo (colored squares).
"""
from time import sleep
from ili9341 import Display
from machine import Pin, SPI
from sys import modules
import mySetup

RED = const(0XF800)  # (255, 0, 0)
GREEN = const(0X07E0)  # (0, 255, 0)
BLUE = const(0X001F)  # (0, 0, 255)
YELLOW = const(0XFFE0)  # (255, 255, 0)
FUCHSIA = const(0XF81F)  # (255, 0, 255)
AQUA = const(0X07FF)  # (0, 255, 255)
MAROON = const(0X8000)  # (128, 0, 0)
DARKGREEN = const(0X0400)  # (0, 128, 0)
NAVY = const(0X0010)  # (0, 0, 128)
TEAL = const(0X0410)  # (0, 128, 128)
PURPLE = const(0X8010)  # (128, 0, 128)
OLIVE = const(0X8400)  # (128, 128, 0)
ORANGE = const(0XFC00)  # (255, 128, 0)
DEEP_PINK = const(0XF810)  # (255, 0, 128)
CHARTREUSE = const(0X87E0)  # (128, 255, 0)
SPRING_GREEN = const(0X07F0)  # (0, 255, 128)
INDIGO = const(0X801F)  # (128, 0, 255)
DODGER_BLUE = const(0X041F)  # (0, 128, 255)
CYAN = const(0X87FF)  # (128, 255, 255)
PINK = const(0XFC1F)  # (255, 128, 255)
LIGHT_YELLOW = const(0XFFF0)  # (255, 255, 128)
LIGHT_CORAL = const(0XFC10)  # (255, 128, 128)
LIGHT_GREEN = const(0X87F0)  # (128, 255, 128)
LIGHT_SLATE_BLUE = const(0X841F)  # (128, 128, 255)
WHITE = const(0XFFF)  # (255, 255, 255)

colors = [RED,
          GREEN,
          BLUE,
          YELLOW,
          FUCHSIA,
          AQUA,
          MAROON,
          DARKGREEN,
          NAVY,
          TEAL,
          PURPLE,
          OLIVE,
          ORANGE,
          DEEP_PINK,
          CHARTREUSE,
          SPRING_GREEN,
          INDIGO,
          DODGER_BLUE,
          CYAN,
          PINK,
          LIGHT_YELLOW,
          LIGHT_CORAL,
          LIGHT_GREEN,
          LIGHT_SLATE_BLUE,
          WHITE ]

def test():
    display = mySetup.createMyDisplay()

    colors.sort()
    c = 0
    for x in range(0, 240, 48):
        for y in range(0, 320, 64):
            display.fill_rectangle(x, y, 47, 63, colors[c])
            c += 1
    sleep(9)
    display.cleanup()


test()
