from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template
app = Flask(__name__)

from temp_logger import TempLogger

sample_period = 60 # sample period for sensor 60 seconds
# relay_pin = 1 # figure out what this is

# Have the logger log temps in the background
logger = TempLogger(sample_period)
logger.log_temperature()

@app.route("/")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)