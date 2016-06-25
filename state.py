from bokeh.plotting import *
from bokeh.sampledata.us_states import data as states
from bokeh.models import HoverTool, Slider
import math
from readData import *

data = createJsonObject("crimeData.json")

year = 2010

del states["HI"]
del states["AK"]

state_xs = [states[code]["lons"] for code in states]
state_ys = [states[code]["lats"] for code in states]

colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043", "#490303", "#000000"]


state_names = [state['name'] for state in states.values()]


state_colors = []
state_rates = []

for state_id in states:
    try:
        rate = getDataForYear(data, year, state_id)
        state_rates.append(rate)
        rate = math.log(rate) 
        idx = int(rate/2)
        state_colors.append(colors[idx])
    except KeyError:
        state_colors.append("black")
        
    
source = ColumnDataSource(data=dict(
    x = state_xs,
    y = state_ys,
    color = state_colors,
    name = state_names,
    rate = state_rates,
))

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(title="US Crime 2010", toolbar_location="left",
           plot_width=1100, plot_height=700, tools=TOOLS)

p.patches('x', 'y', source = source,
          fill_color='color', fill_alpha=0.7,
          line_color="white", line_width=0.5)


hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Name", "@name"),
    ("Violent Crimes", "@rate"),
]


def update():
    year = slider.value

slider = Slider(start=1990, end=2010, value=1, step=1,
                    title="Year")
slider.on_change('value', lambda attr, old, new: update())

output_file("crime.html", title="crime.py example")

show(vplot(p, slider))