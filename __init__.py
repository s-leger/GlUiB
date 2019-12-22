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

bl_info = {
    "name": "GlUiB exemple",
    "description": "Simple example of how to use GlUiB module",
    "author": "Legigan Jeremy AKA Pistiwique",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object"
    }


import bpy

from bpy.types import Operator, Panel

from . import GlUiApplication


class GLUIB_OT_open_window(Operator):
    '''  '''
    bl_idname = 'gluib.open_window'
    bl_label = "Open window"
    bl_options = {'REGISTER'}

    _running = False

    @classmethod
    def poll(cls, context):
        return not cls._running

    @classmethod
    def set_status(cls):
        cls._running = not cls._running

    def invoke(self, context, event):
        self.window = GlUiApplication.GlWindow(context, "VIEW_3D")
        self.window.setGeometry(10, 10, 400, 200)
        self.set_status()
        context.window_manager.modal_handler_add(self)

        self._handle = bpy.types.SpaceView3D.draw_handler_add(
                self.window.draw,
                (),
                'WINDOW',
                'POST_PIXEL')
        return {'RUNNING_MODAL'}

    def modal(self, context, event):
        context.area.tag_redraw()
        self.window.event(event)
        if event.type == 'ESC':
            self.set_status()
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        if self.window.is_hover:
            if event.type == "RIGHTMOUSE":
                self.set_status()
                bpy.types.SpaceView3D.draw_handler_remove(self._handle,
                                                          'WINDOW')
                return {'CANCELLED'}

            return {'RUNNING_MODAL'}

        return {'PASS_THROUGH'}


class GLUIBI_PT_tools_panel(Panel):
    bl_label = "GlUiB Interface"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "GlUiB"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        row.operator("gluib.open_window")


CLASSES = [
    GLUIB_OT_open_window,
    GLUIBI_PT_tools_panel
    ]

def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

def unregister():
    for cls in CLASSES:
        bpy.utils.unregister_class(cls)