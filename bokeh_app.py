import holoviews as hv
from holoviews.operation.datashader import datashade
import numpy as np
from bokeh.layouts import layout
from bokeh.io import curdoc

npt = 200000
threshold = 2000

hv.extension('bokeh')
points = hv.Points(np.random.multivariate_normal((0,0), [[0.1, 0.1], [0.1, 1.0]], (npt,)))

def filter_points(points, x_range, y_range):
    """Filter points by x/y range.
    
    To be used with RangeXY stream.
    """
    if x_range is None or y_range is None:
        return points
    return points[x_range, y_range]

def hover_points(points, threshold=threshold):
    """Filter points by threshold.
    
    Returns empty list if number of input points exceeds threshold.
    """
    if len(points) > threshold:
        return points.iloc[:0]
    return points

filtered = points.apply(filter_points, streams=[hv.streams.RangeXY(source=points)])
shaded = datashade(filtered, width=400, height=400)
hover = filtered.apply(hover_points)

hv_layout = (shaded * hover).opts(
    hv.opts.Points(tools=['hover'], active_tools=['wheel_zoom'],
                   alpha=0.1, hover_alpha=0.2, size=10, width=600, height=600))

renderer = hv.renderer('bokeh').instance(mode='server')
doc = curdoc()
hv_plot = renderer.get_plot(hv_layout, doc)
l = layout(hv_plot.state)
doc.add_root(l)
