from flask import jsonify, make_response

def custom_response(status=200, data=[], msg=None, meta=None):
    data = jsonify({

        "message" : msg,
        "data" : data,
        "meta" : meta
    })
    return make_response(data, status)
