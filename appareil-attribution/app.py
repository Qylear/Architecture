from flask import Flask, request, redirect, url_for
from app.views import attribution_view

app = Flask(__name__)

@app.route('/attribution/form')
def allocation_form():
    return attribution_view.display_allocation_form()

@app.route('/attribution/status/<int:attribution_id>')
def allocation_status(allocation_id):
    return attribution_view.display_allocation_status(allocation_id)

@app.route('/')
def home():
    return "Bienvenue sur l'application d'attribution !"

@app.route('/allocation/submit', methods=['POST'])
def allocation_submit():
    return attribution_view.submit_allocation_form()

if __name__ == '__main__':
    app.run(debug=True)