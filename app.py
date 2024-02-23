from flask import Flask, render_template, request, redirect, url_for
from stat_1 import stat
from flask import session
from flask import jsonify
from getdata import get
from datetime import datetime
from moisture import moist
m=moist()
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

s=stat()
# Placeholder variable for moisture level (in %)
#moisture_level =m.get_moisture_data()
moisture_level =75
@app.route('/')
def index():
    return render_template('index.html', moisture_level=moisture_level)

import csv

@app.route('/irrigation', methods=['GET', 'POST'])
def irrigation():
    if request.method == 'POST':
        irrigation_hour = request.form['irrigation_hour']
        irrigation_minute = request.form['irrigation_minute']
        water_flow_time = int(request.form['water_flow_time'])
        
        # Create irrigation_time string
        irrigation_time = f"{irrigation_hour}:{irrigation_minute}"
        
        # Print irrigation_time and water_flow_time
        print(irrigation_time)
        print(water_flow_time)
        
        # Write data to CSV file
        with open('irrigation_data.csv', 'w', newline='') as csvfile:
            fieldnames = ['irrigation_hour', 'irrigation_minute', 'water_flow_time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data to CSV file
            writer.writerow({'irrigation_hour': irrigation_hour, 'irrigation_minute': irrigation_minute, 'water_flow_time': water_flow_time})
        
        return redirect(url_for('index'))
    else:
        return render_template('irrigation.html')

@app.route('/stop_irrigation', methods=['POST'])
def stop_irrigation():
    s.poststat(0)
    return redirect(url_for('index'))
@app.route('/get_session_data', methods=['GET'])
def get_session_data():
    return jsonify({
        'irrigation_hour': session.get('irrigation_hour'),
        'irrigation_minute': session.get('irrigation_minute'),
        'water_flow_time': session.get('water_flow_time')
    })

if __name__ == '__main__':
    app.run(debug=True)
