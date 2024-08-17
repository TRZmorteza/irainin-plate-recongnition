from hezar.models import Model
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from PIL import Image

# Creating an SQLAlchemy instance
# db = SQLAlchemy(app)


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
@app.route('/',methods=["GET"])
def imga():
  path="D:/projects/up/img.png"
  print(path)
  model = Model.load("hezarai/crnn-fa-license-plate-recognition")
  plate_text = model.predict(path)
  sli=slice(11,-3)
  numberOfPlate=str(plate_text)[sli]
  sli2,sli3=slice(0,-2),slice(-2,len(numberOfPlate))

  numberOfPlate=str(numberOfPlate[sli2]+"-"+numberOfPlate[sli3])
  
  return numberOfPlate#returns string
if __name__=='__main__':
    app.run(debug=True)s