# -*- coding: utf-8 -*-
"""
Created on Fri Apr 5 19:26:11 2024

@author: Debabrata Ghorai, Ph.D.

Flask Application - Manage Project.
"""

import os
import sys
sys.path.append('src')

from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')
CORS(app)

# add functions


# run
if __name__ == '__main__':
    app.run(debug=True)
