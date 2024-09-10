import sys
sys.path.append('.')
from flask import Flask, request, jsonify
from utilities import log_setup 
import traceback
from database import db_operations as db
import pandas as pd

logger = log_setup.getlogger()
# Fundamental line of code used to create a new Flask application instance
app = Flask(__name__)

@app.route('/categories', methods=['GET'])

def get_all_categories():
    try:
        conn = db.get_alias_connection('store_db')
        sql = "select * from categories"
        category_df = pd.read_sql(sql,conn)
        category_dict= category_df.to_dict()
        return category_dict
    except:
        logger.error(traceback.format_exc())

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

    
