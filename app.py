from flask import Flask,request
import os
import numpy as np
import cv2
app=Flask(__name__)

INPUT=os.path.basename('input')
app.config['INPUT']=INPUT
OUTPUT=os.path.basename("output")
app.config['OUTPUT']=OUTPUT



@app.route("/upload",methods=['POST'])
def main():
    file=request.files['image']
    if file is None:
        print("NO image upload")
    f1=os.path.join(app.config['INPUT'],file.filename)
    file.save(f1)
    source = cv2.imread(f1, cv2.IMREAD_COLOR)
    greyimage = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(app.config['OUTPUT'],file.filename),greyimage)
    return "Converted"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5001',debug=True)
