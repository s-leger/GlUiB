# -*- coding:utf-8 -*-

# GlUiD module for Blender
# Copyright (C) 2018 Legigan Jeremy AKA Pistiwique
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# <pep8 compliant>


import bpy

from . import GlUiWidgets

from .GlUiGl import GPU_Quad
from . import GlUiCore


class GlWindow(GlUiWidgets.GlWidget, GlUiCore.GlArea):
    def __init__(self, context, area):
        GlUiWidgets.GlWidget.__init__(self)
        GlUiCore.GlArea.__init__(self)

        self._childrens = []
        self._context = context
        self._area_type = area
        self._close = False

        self._header = GPU_Quad(self)
        self._header_height = 30
        self._frame = GPU_Quad(self)

    @property
    def context(self):
        return self._context

    @property
    def areaType(self):
        return self._area_type

    @property
    def globalX(self):
        return self.min_x + self.x

    @property
    def globalY(self):
        return self.min_y - self.y

    def addWidget(self, widget):
        self._childrens.append(widget)

    def event(self, event):
        if event.type == "MOUSEMOVE":
            self.setIsHover(event, self.globalX, self.globalY, self.width, self.height)

    def draw(self):
        theme = bpy.context.preferences.themes['Default']
        panel_color = theme.view_3d.space.panelcolors
        self.getSize(self.context, self.areaType)

        self._header.setVertices(
                ((self.globalX, self.globalY),
                 (self.globalX + self.width, self.globalY),
                 (self.globalX, self.globalY - self._header_height),
                 (self.globalX + self.width, self.globalY - self._header_height))
                )
        if self.is_hover:
            self._header.setColor(theme.user_interface.wcol_radio.inner_sel)
        else:
            self._header.setColor(panel_color.header)

        self._frame.setVertices(
                ((self.globalX, self.globalY - self._header_height),
                 (self.globalX + self.width, self.globalY - self._header_height),
                 (self.globalX, self.globalY - self.height),
                 (self.globalX + self.width, self.globalY - self.height))
                )
        self._frame.setColor(panel_color.back)

        self._header.draw()
        self._frame.draw()

    @property
    def is_closed(self):
        return self._close

    def close(self):
        self._close = True