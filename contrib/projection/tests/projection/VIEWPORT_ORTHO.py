#!/usr/bin/env python
"""
"""

__docformat__ = 'restructuredtext'
__version__ = '$Id: WINDOW_OPEN.py 750 2007-03-17 01:16:12Z Alex.Holkner $'

import unittest

from pyglet.gl import *
from pyglet.ext import projection
from pyglet import window

from . import base_projection


class VIEWPORT_ORTHO(unittest.TestCase):

    def test_viewport_ortho(self):
        width, height = 200, 200
        w = window.Window(width, height)
        w.viewport = projection.WindowViewport(w)
        w.projection = projection.OrthographicProjection(w.viewport)
        self.views = views = [
            projection.OrthographicViewport(w.projection,
                                            0, 0, width / 2, height / 2),
            projection.OrthographicViewport(w.projection,
                                            width / 2, 0, width / 2,
                                            height / 2),
            projection.OrthographicViewport(w.projection,
                                            width / 2, height / 2, width / 2,
                                            height / 2),
            projection.OrthographicViewport(w.projection,
                                            0, height / 2, width / 2,
                                            height / 2),
        ]
        projections = [projection.OrthographicProjection(v) for v in views]
        colors = [
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 0)
        ]
        while not w.has_exit:
            w.dispatch_events()

            for color, p in zip(colors, projections):
                p.apply()
                glColor3f(*color)
                base_projection.fillrect(0, 0, width / 2, width / 2)

            w.flip()

        w.close()

    unittest.main()
