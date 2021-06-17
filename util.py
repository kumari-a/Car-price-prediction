import pickle
import json
import numpy as np

_data_columns = None
_model = None

def read_artifacts():   
    global _data_columns
    global _model
    print('Accessing Artifacts...')

    with open('./columns.json','r') as f:
        _data_columns = json.load(f)['data_columns']

    with open('./car_price.pickle','rb') as f:
        _model = pickle.load(f)
    
    print('Loading Artifacts Done...')

def predict_price(year,kms,mig,eng,pwr,seats,fuel_type,transmission,owner,city,name):
    input = np.zeros(len(_data_columns))

    input[0] = year
    input[1] = kms
    input[2] = mig
    input[3] = eng
    input[4] = pwr
    input[5] = seats

    
    idf = _data_columns.index(fuel_type.lower())
    idt = _data_columns.index(transmission.lower())
    ido = _data_columns.index(owner.lower())
    idc = _data_columns.index(city.lower())
    idd = _data_columns.index(name.lower())

    input[idf] = 1
    input[idt] = 1
    input[ido] = 1
    input[idc] = 1
    input[idd] = 1

    return _model.predict([input])[0][0]
    
#def show_data_columns():
#    print(len(_data_columns))


read_artifacts()
print(predict_price(1,60000,14,120,89,5,'Diesel','Automatic','First','Delhi','audi a4'))
