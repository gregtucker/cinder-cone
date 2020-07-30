#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:20:41 2020

@author: gtucker
"""

from landlab.grid.raster_funcs import line_to_grid_coords

def nodes_along_line_segment(grid, x0, y0, x1, y1):
    """Return an array of node IDs that are intersected by the line segment
    (x0, y0) -> (x1, y1).

    Parameters
    ----------
    grid : RasterModelGrid
        Landlab grid object
    x0, y0 : float
        x and y coordinates of starting point
    x1, y1 : float
        x and y coordinates of ending point

    Examples
    --------
    >>> from landlab import RasterModelGrid
    >>> grid = RasterModelGrid((5, 7), xy_spacing=10.0)
    >>> nodes_along_line_segment(grid, 0, 0, 53, 32)
    array([  0,  8,  10, 17, 18, 26])
    """

    # Calculate starting and ending row and column indices
    r0 = int(round(x0 / grid.dx))
    c0 = int(round(y0 / grid.dy))
    r1 = int(round(x1 / grid.dx))
    c1 = int(round(y1 / grid.dy))

    # Find the nodes by row and column
    grid_coords = line_to_grid_coords(c0, r0, c1, r1)

    # Find and return the corresponding node IDs
    return grid.grid_coords_to_node_id(grid_coords[1], grid_coords[0])