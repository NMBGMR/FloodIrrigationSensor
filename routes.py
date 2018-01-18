# ===============================================================================
# Copyright 2018 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
from datetime import datetime

from bokeh.embed import components
from bokeh.plotting import figure
from flask import render_template
from numpy.ma import array

from application import app
from sensor import get_sensor_data


def create_figure(x, y, title):
    tools = "crosshair,pan,reset,save,wheel_zoom"
    plot = figure(plot_height=400, plot_width=400,
                  title=title,
                  tools=tools)

    plot.line(x, y, line_width=3, line_alpha=0.6)

    # plot.xaxis.axis_label = 'Demo X'
    # Set the y axis label
    #
    # plot.yaxis.axis_label = 'Demo Y'
    return plot


def make_demo_plot():
    x = array([1, 2, 3, 4])
    a, b, c = 1, 2, 3
    y = a * x * x + b * x + c
    # Create the plot
    plot = create_figure(x, y, 'Demo Plot')

    return components(plot)


@app.route('/')
def index():
    script, div = make_demo_plot()
    ctx = {'timestamp': datetime.now(),
           'sensor1': get_sensor_data(1),
           'sensor2': get_sensor_data(2),
           'temp_script': script,
           'temp_div': div}

    return render_template('index.html', **ctx)
# ============= EOF =============================================
