# bulid my flask app for electron configuration of the peridoic table elements
from flask import Flask, render_template, request
from mendeleev import element

app = Flask(__name__)


# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        element_name = request.form['element_name'] 
        element_object = element(element_name)
        element_electrons = element_object.ec
        atomic_number= element_object.atomic_number
        # complete name of the element
        element_name = element_object.name
        # Symbol of the element
        element_symbol = element_object.symbol
        # period of the element
        element_period = element_object.period
        # group of the element
        element_group = element_object.group
        # atomic mass of the element
        element_atomic_mass = element_object.atomic_weight
        # element_atomic_mass two decimal places
        element_atomic_mass = round(element_atomic_mass, 3)
        #  number of electrons per shell type
        element_electrons_per_shell = element_object.ec.electrons_per_shell()
        # Pauling’s thermochemical scale of electronegativity
        element_pauling = element_object.electronegativity('pauling')
        return render_template('index.html', element_name=element_name, 
                               element_electrons=element_electrons, 
                               atomic_number=atomic_number,
                               element_period=element_period,
                               element_group=element_group,
                               element_atomic_mass=element_atomic_mass,
                               element_pauling=element_pauling,
                               element_electrons_per_shell=element_electrons_per_shell,
                               element_symbol = element_symbol)                           
    else:
        return render_template('index.html')
@app.route('/offline')
def offline():
    return app.send_static_file('offline.html')
@app.route('/manifest.json')
def manifest():
    return app.send_static_file('manifest.json')
@app.route('/sw01.js')
def service_worker():
    return app.send_static_file('sw01.js')
  
# run   the app
if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=8080)
    app.run(debug=True)
