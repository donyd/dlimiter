from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '\x14\tH\xf3\xb9\r\x8e\xaa9S\r\xa5\xfc\x98+\xc6\x93\xce\x06\xaa\xbfLR:'

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}.".format(self.firstname[0], self.lastname[0])

def convertCSV(input):
    convertedCSV = ''
    temp = input.split('\n')
    temp = list(map(lambda x: x.rstrip('\r'), temp))
    for i in range(len(temp)):
        convertedCSV += temp[i] + ', '

    convertedCSV = convertedCSV.rstrip('\n')
    convertedCSV = convertedCSV.rstrip(' ,')  
    return convertedCSV

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # if request.method == "POST":
    #     formData = request.form['columnData']
    #     result = convertCSV(formData)  
    #     flash(result)
    #     return redirect(url_for('index'))
    return render_template('index.html')    
    

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/change')
def change():
    return render_template('change.html')

if __name__ == '__main__':
    app.run(debug=True)