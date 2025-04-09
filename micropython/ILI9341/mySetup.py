from ili9341 import Display
from machine import Pin, SPI, SoftSPI

TFT_CLK_PIN = const('D13')
TFT_MOSI_PIN = const('D11')
TFT_MISO_PIN = const('D12')

TFT_CS_PIN = const('D9')
TFT_RST_PIN = const('D8')
TFT_DC_PIN = const('D10')

def createMyDisplay():
    #spiTFT = SoftSPI(baudrate=40000000, sck=Pin(TFT_CLK_PIN), mosi=Pin(TFT_MOSI_PIN), miso=Pin(TFT_MISO_PIN))
    spiTFT = SPI(0, baudrate=4_000_000)
    display = Display(spiTFT, dc=Pin(TFT_DC_PIN), cs=Pin(TFT_CS_PIN), rst=Pin(TFT_RST_PIN))
    return display