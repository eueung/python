from simplexml import dumps
from flask import make_response, Flask
from flask_restful import Api, Resource
#------------------------------------------
def output_xml(data, code, headers=None):
    resp = make_response(dumps({'response' :data}), code)
    resp.headers.extend(headers or {})
    return resp
#------------------------------------------
app = Flask(__name__)
api = Api(app, default_mediatype='application/xml')
api.representations['application/xml'] = output_xml
#------------------------------------------
class Hello(Resource):
    def get(self, entry):
        return {'hello': entry}
#------------------------------------------
api.add_resource(Hello, '/<string:entry>')
#------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)