from pygame.font import Font
import __main__
import os

ASSETS_DIR = os.path.dirname(__main__.__file__) + "\\assets\\"
GLOBAL_FONT_PATH = ASSETS_DIR + "winter-minie.ttf"

TITLE_TEXT_STYLE = Font(GLOBAL_FONT_PATH, 60)
BODY_TEXT_STYLE = Font(GLOBAL_FONT_PATH, 24)
INSTRUCTION_TEXT_STYLE = Font(GLOBAL_FONT_PATH, 26)
OPTION_TEXT_STYLE = Font(GLOBAL_FONT_PATH, 32)
SCORE_TEXT_STYLE = Font(GLOBAL_FONT_PATH, 34)