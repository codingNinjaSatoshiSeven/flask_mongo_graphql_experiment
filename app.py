from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
import resolver as r
from database import init_db


app = Flask(__name__)

type_defs = load_schema_from_path('schema.graphql')

#query = QueryType()
query = ObjectType("Query")
vehicle = ObjectType("Vehicle")
booking = ObjectType("Booking")


#Set Query fields
query.set_field("vehicle", r.getVehicles)
query.set_field("booking", r.getBookings)


schema = make_executable_schema(type_defs, [query, booking, vehicle])

@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200
    
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
    schema,
    data,
    context_value=None,
    debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0')