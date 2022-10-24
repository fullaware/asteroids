from app_settings import *
from flask import Flask, request, jsonify, flash, url_for, redirect, render_template
import json
import requests

# creating an instance of the flask app
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def show_all():
    response = requests.get(api_endpoint)
    return render_template('show_all.html', asteroids=response.json())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['sizekg'] or not request.form['au']:
            flash('Please enter all the fields', 'error')
        else:
            r = request.form.to_dict()
            res = requests.post(api_endpoint, json=r)
            print(res.text)
            flash('Record was successfully added')

            return redirect(url_for('show_all'))
    return render_template('new.html')


# @app.route('/delete/<int:id>', methods=['POST'])
# def delete(id):
#     uri_id = api_endpoint+'/'+str(id)
#     print(uri_id)
#     requests.delete(uri_id)

#     flash('Asteroid was successfully deleted')

#     return redirect(url_for('show_all'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':

        response = request.form
        
        headers = {
            'content-type': 'application/json',
            'content-length': str(len(response))
        }
        str_args = {
            'name': response['name'],
            'owner': response['owner'],
            'sizekg': response['sizekg'],
            'minedsizekg': response['minedsizekg'],
            'hazard': response['hazard'],
            'diameterkm': response['diameterkm'],
            'spectralgroup': response['spectralgroup'],
            'rotationh': response['rotationh'],
            'au': response['au']
        }

        json_args = json.dumps(str_args)

        uri_api_endpoint = api_endpoint+'/'+str(response['id'])

        requests.put(uri_api_endpoint, data=json_args, headers=headers)
        flash('Record was successfully updated')
        flash(json_args)
        return redirect(url_for('show_all'))
    else:
        return redirect(url_for('show_all'))
    # return render_template('update.html', vehicle=car_id)

@app.route('/search', methods=['POST'])
def search():
    
    # print(jsonify(request.args()))
    response = request.form
        
    headers = {
            'content-type': 'application/json',
            'content-length': str(len(response))
        }
    str_args = {
            'search': response['search']
        }

    json_args = json.dumps(str_args)
    response = requests.post(api_endpoint+"/search", data=json_args, headers=headers)

    return render_template('show_all.html', asteroids=response.json())

@app.route('/scan', methods=['POST'])
def scan():
    
    # print(jsonify(request.args()))
    response = request.form
        
    headers = {
            'content-type': 'application/json',
            'content-length': str(len(response))
        }
    str_args = {
            'range': float(response['range']),
            'location': float(response['location'])
        }

    json_args = json.dumps(str_args)

    response = requests.post(api_endpoint+"/scan", data=json_args, headers=headers)

    return render_template('show_all.html', asteroids=response.json())

@app.route('/analytics')
def analytics():
    uri_endpoint = api_endpoint+'/analytics'
    response = requests.get(uri_endpoint)
    return render_template('analytics.html', analytics=response.json())

@app.route('/mining')
def mining():
    uri_endpoint = api_endpoint+'/analytics'
    response = requests.get(uri_endpoint)
    return render_template('analytics.html', analytics=response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)
