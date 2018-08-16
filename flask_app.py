from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)

# from temp_logger import TempLogger

sample_period = 60 # sample period for sensor 60 seconds
# relay_pin = 1 # figure out what this is

# Have the logger log temps in the background
# logger = TempLogger(sample_period)
# logger.log_temperature()

pump_on_time = 1
pump_off_time = 19

@app.route("/")
def root():
    basic_info = ("<ul>" + 
                    "<li><b>Pump On Time:</b> " + str(pump_on_time) + " minutes</li>" +
                     "<li><b>Pump Off Time:</b> " + str(pump_off_time) + " minutes</li>" +
                 "</ul>")

    return basic_info

@app.route("/charts")
def charts():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)