from flask import Flask, redirect, Markup, Flask, render_template
from config import ConfigClass
from forms import PumpConfigForm
from temp_logger import TempLogger

# Globals
app = Flask(__name__)
pump_on_time = 1
pump_off_time = 19
sample_period = 60 # sample period for temp sensor 60 seconds
# relay_pin = 1 # figure out what this is

# Have the logger log temps in the background
logger = TempLogger(sample_period)
logger.log_temperature()

print(ConfigClass)
app.config.from_object(ConfigClass)

@app.route("/")
def root():
    print("root on time: " + str(pump_on_time))

    basic_info = ("<ul>" + 
                    "<li><b>Pump On Time:</b> " + str(pump_on_time) + " minutes</li>" +
                     "<li><b>Pump Off Time:</b> " + str(pump_off_time) + " minutes</li>" +
                     "<li><b>Probe Temperature:</b> " + str(logger.current_reading['probe']) + " F</li>" +
                     "<li><b>Ambient Temperature:</b> " + str(logger.current_reading['ambient']) + " F</li>" +
                 "</ul>")

    return basic_info


@app.route("/charts")
def charts():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)
 

@app.route('/pump', methods=['GET', 'POST'])
def pump_config():
    global pump_on_time
    global pump_off_time

    form = PumpConfigForm()

    if (form.validate_on_submit()):
        pump_on_time = form.pump_on_time.data
        pump_off_time = form.pump_off_time.data

        print("\n\n: on time: " + str(pump_on_time))
    else:
        return render_template('pump_config.html', title='Add Charge', form=form)

    return redirect('/', code=302)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)