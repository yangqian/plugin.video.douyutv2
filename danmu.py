#adopted from https://github.com/steeve/xbmctorrent/blob/master/resources/site-packages/xbmctorrent/player.py
import xbmc
import xbmcaddon
import xbmcgui
import os

WINDOW_FULLSCREEN_VIDEO = 12005
VIEWPORT_WIDTH = 1920.0
VIEWPORT_HEIGHT = 1080.0
class OverlayText(object):
    def __init__(self,  *args, **kwargs):
        self.window = xbmcgui.Window(WINDOW_FULLSCREEN_VIDEO)
        viewport_w, viewport_h = self._get_skin_resolution()
        # Adjust size based on viewport, we are using 1080p coordinates
        self._shown = False
        self._text = ""
        self._label = xbmcgui.ControlLabel(int(viewport_w*0.7), int(viewport_h*0.10), int(viewport_w*0.3), int(viewport_h*0.8),
            self._text,alignment=0)

    def show(self):
        if not self._shown:
            self.window.addControls([self._label])
            self._shown = True

    def hide(self):
        if self._shown:
            self._shown = False
            self.window.removeControls([ self._label])

    def close(self):
        self.hide()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        if self._shown:
            self._label.setLabel(self._text)

    # This is so hackish it hurts.
    def _get_skin_resolution(self):
        import xml.etree.ElementTree as ET
        skin_path = xbmc.translatePath("special://skin/")
        tree = ET.parse(os.path.join(skin_path, "addon.xml"))
        res = tree.findall("./extension/res")[0]
        return int(res.attrib["width"]), int(res.attrib["height"])
