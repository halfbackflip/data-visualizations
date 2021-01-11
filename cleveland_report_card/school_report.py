from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, Label, LabelSet, Range1d
from bokeh.palettes import inferno, viridis, plasma
import pandas

output_file("school_report.html")

df = pandas.read_csv("school_report_card.csv").sort_values(by=['Performance'])

dist = list(df.District)
results = list(df.Performance)
plasma_p = plasma(31)

p = figure(x_range=dist,
        plot_width=1200, 
        plot_height=800)

p.vbar(x=dist,
        width=0.5, 
        bottom=0,
        top=results, 
        color = plasma_p,
        fill_alpha=.75)

p.xaxis.major_label_orientation = .9

show(p)