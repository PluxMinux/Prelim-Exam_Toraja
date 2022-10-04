#Prelim_Exam: Toraja-Q27
from flask import Flask, jsonify, request

app = Flask(__name__)

temperature_record = [
    {
        "temp_id" : "0001",
        "date" : "09-04-2022",
        "temperature" : "41 degree celsius"
    },

    {
        "temp_id" : "0002",
        "date" : "09-05-2022",
        "temperature" : "55 degree celsius"
    }
]

@app.route('/temperature_record',methods=['GET'])
def displayTempRecord():
    return jsonify(temperature_record)

@app.route('/temperature_record',methods=['POST'])
def addTemperature():
    new_temperature = request.get_json()
    temperature_record.append(new_temperature)
    return{'id': len(temperature_record)},200

@app.route('/temperature_record/<int:index>', methods=['DELETE'])
def deleteTemperature(index):
    temperature_record.pop(index)
    return "Temperature record was successfully deleted",200

if __name__ =='__main__':
    app.run()
