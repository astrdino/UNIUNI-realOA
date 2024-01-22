#The file the framework FLASK used to deliver Web App content
from flask import Flask, request,render_template,send_file,send_from_directory

import pandas as pd
import os
import csv
from datetime import datetime


#https://realpython.com/python-web-applications/


#Create Flask instance "app"
app = Flask(__name__)

#Create directory for downloadable files
app.config['UPLOAD_FOLDER'] = 'tmp'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

celsius = "N/A"

# @app.route("/Convert.html?celsius=123")
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
       
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        
        print(str(fahrenheit)+"from function")
        return fahrenheit
        # return render_template('Convert.html', my_var = str(fahrenheit))  
    except ValueError:
        return "invalid input"

@app.route("/Convert.html", methods=['GET', 'POST'])
def Convert():
    fahrenheit = None
    if request.method == 'POST':
        print('hello')
        celsius = request.form.get("celsius", "")
        fahrenheit = fahrenheit_from(celsius)
        print(celsius)
        print(fahrenheit)
        return render_template('Convert.html', my_var = str(fahrenheit))

    return  render_template('Convert.html')


@app.route("/Uniuni-Concat.html", methods=['GET', 'POST'])
def Uniuni_Concat():

    current_time = datetime.now().strftime("%m-%d-%Y")

    if request.method == 'POST':

        batchNum = request.form.get('batchInput')
        driverIDs = request.form.getlist("driverInputs[]")

        #Remove syntax
        for ele in driverIDs:
            print(ele)
            ele.replace("'",'')

        
        return render_template('Uniuni-Concat.html', batchNum=batchNum, driverIDs=driverIDs, current_time = current_time)

    return render_template('Uniuni-Concat.html', current_time = current_time)



@app.route('/Auto_DailyReport.html', methods=['GET','POST'])
def upload_file():

    

    if 'file' not in request.files:
        return render_template('Auto_DailyReport.html',Sheet_Status = 'Sheet not foud')
    
    file = request.files['file']

    if file.filename == '':
        return 'No selected file'
    if file:
        return render_template('Auto_DailyReport.html',Sheet_Status = 'Sheet found',output_filename=process_csv(file))
        

def process_csv(file):

    if file.filename.endswith('.csv'):
        print()
    elif file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
        # Create a new CSV file to write processed data
        output_file = 'processed_data.xlsx'
        df.to_excel("./tmp/"+output_file,index=False)
        # return render_template('Auto_DailyReport.html',Sheet_Status = 'ALL DONE')

    else:
        "File Format Error"




    print(file.filename)
    return output_file



#Download
@app.route('/download/<filename>')
def download_file(filename):
    print("last step")
    print(filename)
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d")
    return render_template('index.html', current_time = current_time)


@app.route("/Test.html")
def PAGE_test():
    return render_template('Test.html')




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    