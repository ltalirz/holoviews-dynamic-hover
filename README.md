# holoviews with dynamic bokeh overlay

**Problem**: You want to make a two-dimensional scatter plot of a data set but the data set
is too large (> 50k points) to be sensibly visualized with [`bokeh`](https://bokeh.org/).
At the same time, you would like to retain the ability to interact with individual points to find out more information about them (e.g. via the `hover` tool).

**Solution**: Use [`holoviews`](http://holoviews.org/), start with a full view of the plot rendered with [`datashader`](https://datashader.org/),
and overlay with a [`bokeh`](https://bokeh.org/) scatter plot only once the user has zoomed in far enough.

![Demo](https://i.ibb.co/mS7z89R/zoom.gif "Bokeh overlay appears upon zoom.")

## Prerequisites
With [`conda`](https://docs.conda.io/en/latest/):
```
conda install -c pyviz bokeh datashader fastparquet python-snappy
```

Tested with python 3.7, holoviews 1.12.7 and datashader 0.9.0

## Run
Run jupyter notebook via
```
jupyter notebook dynamic_overlay.ipynb
```

Serve as web page via bokeh
```
bokeh serve dynamic_overlay.py --show
```

Note: `bokeh_app.py` shows how to integrate this into an existing bokeh app
via manipulation of `curdoc()`.

## Credits

All credits due to @philippjfr for not only creating the great holoviews package but also providing [great support](https://discourse.holoviz.org/t/how-to-show-hide-overlay-depending-on-zoom-level/61/2).
