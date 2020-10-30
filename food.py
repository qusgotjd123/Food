from flask import Flask, render_template, request
from check_mod import check_add, check_phone, payment_save
import mariadb
import sys

app = Flask(__name__)
reservation_info = []

@app.route("/")
def main():
    return render_template('main.html')

@app.route