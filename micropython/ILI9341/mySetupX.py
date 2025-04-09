from ili9341 import Display
from machine import Pin, SPI
from xpt2046 import Touch

TFT_CLK_PIN = const('D13')
TFT_MOSI_PIN = const('D11')
TFT_MISO_PIN = const('D12')

TFT_CS_PIN = const('D9')
TFT_RST_PIN = const('D8')
TFT_DC_PIN = const('D10')

XPT_CLK_PIN = const('D13')
XPT_MOSI_PIN = const('D11')
XPT_MISO_PIN = const('D12')

XPT_CS_PIN = const('D4')
XPT_INT = const('D3')

def createMyDisplay():
    spiTFT = SPI(0, baudrate=40000000)
    display = Display(spiTFT, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN))
    return display

def createXPT(touch_handler):
    spiXPT = SPI(0, baudrate=1000000)

    xpt = Touch(spiXPT, cs=Pin(XPT_CS_PIN), int_pin=Pin(XPT_INT),int_handler=touch_handler)

    return xpt