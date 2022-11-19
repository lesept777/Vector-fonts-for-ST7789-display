import st7789
import tft_config

import Fonts.Calibri as calibri
import Fonts.Arial as arial
import Fonts.ariali as ariali
import Fonts.cour as courrier
import Fonts.courbi as courrierBI
import Fonts.times as times

# Init display
tft = tft_config.config(1)
tft.init()
size = 0.9
blue = st7789.BLUE
bg   = st7789.WHITE
tft.fill(bg)
tft.rotation(0) 
tft.draw(arial, 'Arial', 0, 40, blue, size*2)
tft.draw(ariali, 'Arial i', 0, 80, blue, size)
tft.draw(calibri, 'Calibri', 0, 120, blue, size)
tft.draw(courrier, 'Courrier', 0, 160, blue, size)
tft.draw(courrierBI, 'Courrier BI', 0, 190, blue, size/2)
tft.draw(times, 'Times', 0, 230, blue, size*2)
