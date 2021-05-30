# -*- coding: utf-8 -*-
import json

import dicttoxml
from flask import Flask, Response, request

from geocode_function import cal_geocode

app = Flask(__name__)


@app.post("/getAddressDetails")
def cal_lat_long():
    """This API return latitude and longitude of any given address in XML or JSON format."""
    err_msg = ""
    status = 200

    try:
        # Read the request data.
        req_data = json.loads(request.data)
        if "address" not in req_data or "output_format" not in req_data:
            err_msg = "Wrong parameters"
            status = 400
        elif len(req_data["address"]) == 0:
            err_msg = "Invalid address"
            status = 400
        else:
            # pass the address value to cal_geocode function.
            (ret, output) = cal_geocode(req_data["address"])
            if not ret:
                err_msg = output
                status = 500
            elif req_data["output_format"] == "json":
                return output
            elif req_data["output_format"] == "xml":
                return Response(
                    dicttoxml.dicttoxml(output, attr_type=False),
                    mimetype="application/xml",
                )
            else:
                err_msg = "Wrong output format"
                status = 400
    except json.JSONDecodeError:
        err_msg = "Invalid JSON Parameters"
        status = 400

    except Exception as exp:
        print(exp)
        err_msg = "some server error"
        status = 500
    return Response(err_msg, status=status)


if __name__ == "__main__":
    app.run(debug=True)
