from flask import Flask, request, render_template_string
app = Flask(__name__)

data_received = {}

@app.route('/', methods=['POST'])
def receive_data():
    global data_received
    #timestamp = request.json.get('timestamp')
    #unique_id = request.json.get('unique_id')
    integer = request.json.get('integer')

    # Check that unique_id is 32 characters long
    #if len(unique_id) != 32:
    #    return "Error: unique_id must be 32 characters long", 400

    data_received = {
    #    'timestamp': timestamp,
    #    'unique_id': unique_id,
        'integer': integer
    }

    return "Data received successfully", 200

@app.route('/lookie')
def display_data():
    return render_template_string('''
        <h1>Data received:</h1>
        <ul>
            <li>Integer: {{ integer }}</li>
        </ul>
        ''', **data_received)

if __name__ == '__main__':
    app.run(debug=True)
