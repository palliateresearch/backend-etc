from flask import *
from datetime import *


app = Flask(__name__)

data_received = {}
internal_data = {
    'wattsecond': 1,
    'totalEnergy': 1,}
energy = float(0.0)  # Total energy in Watt Hours
totalEnergy = float(0.0)



@app.route('/arduino', methods=['POST'])
def receive_data():
    global data_received, totalEnergy, internal_data
    integer = request.json.get('integer')
    parkName = "Apple Park"

    wattsecond = float(integer)
    energy = float(integer) / 3600.0
    totalEnergy += energy
    totalEnergy = round(totalEnergy, 2)

    # Check that unique_id is 32 characters long
    #if len(unique_id) != 32:
    #    return "Error: unique_id must be 32 characters long", 400

    data_received = {
        #'energy': energy,
        'totalEnergy': totalEnergy
    }
    internal_data = {
        'wattsecond': wattsecond,
        'totalEnergy': totalEnergy,
    }

    return "Data received successfully", 200

@app.route('/lookie')
def display_data():
    return render_template('lookie.html', **internal_data)


@app.route('/get', methods=['GET'])
def g28hgf30rghhsgf0h0h9g():
    global data_received
    JSONData = jsonify(data_received)





    # return render_template_string('''
    #         <h1>Device Debugger:</h1>
    #         <ul>
    #             <li>JSON: {{ wap }}</li>
    #         </ul>
    #         ''', **JSONData)
    return jsonify(data_received)

if __name__ == '__main__':
    app.run(debug=True)

# gunicorn -b 172.16.252.187:5000 app:app
#10.113.57.174
#gunicorn -b 172.16.91.144:5000 app:app
#169.254.204.64
#gunicorn -b 172.16.206.71:5000 app:app