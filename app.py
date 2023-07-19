from flask import *
app = Flask(__name__)

data_received = {}
energy = float(0.0)  # Total energy in Watt Hours
totalEnergy = float(0.0)


@app.route('/arduino', methods=['POST'])
def receive_data():
    global data_received, totalEnergy
    integer = request.json.get('integer')
    parkName = "Apple Park"


    energy = int(integer) / 3600.0
    totalEnergy += energy

    # Check that unique_id is 32 characters long
    #if len(unique_id) != 32:
    #    return "Error: unique_id must be 32 characters long", 400

    data_received = {
        #'energy': energy,
        'totalEnergy': totalEnergy,
    }

    return "Data received successfully", 200

@app.route('/lookie')
def display_data():

    return render_template_string('''
        <h1>Device Debugger:</h1>
        <ul>
            <li>Device: {{ unique_id }}</li>
            <li>Timestamp: {{ timestamp }}</li>
            <li>Integer: {{ integer }}</li>
            <li>Energy: {{ energy }}</li>
            <li>Energy (Total wH): {{ totalEnergy }}</li>
            
        </ul>
        ''', **data_received)


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
    return jsonify(JSONData)

if __name__ == '__main__':
    app.run(debug=True)

# gunicorn -b 172.16.252.187:5000 app:app
#10.113.57.174
#gunicorn -b 172.16.91.144:5000 app:app