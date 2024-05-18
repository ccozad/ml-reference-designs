# Flask imports
from flask import Flask, request, Response
# Used to generate globally unique identifiers
from uuid import uuid4
# Used to serialize and deserialize Python objects
import json

from custom_pipelines import CustomPipelines

cp = CustomPipelines()

app = Flask(__name__)

# Our storage for this example will simply be an in memory dictionary
print("Initializing storage")
storage = {
    'references': {},
    'interactions': {}
}

@app.route("/references", methods=['GET', 'POST'])
def all_references():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is not None and 'url' in body and 'docType' in body:
            if body['docType'] == 'html':
                index_success = cp.index_html_pipeline(body['url'])
                if index_success:
                    id = uuid4()
                    body['id'] = str(id)
                    storage['references'][str(id)] = body
                    return Response(json.dumps(body, indent=4), status=200, mimetype='application/json')
                else:
                    return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
            else:
                return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
    elif request.method == 'GET':
        all_references = {
            'items': []
        }
        for k,v in storage['references'].items():
            all_references['items'].append(v)
        return Response(json.dumps(all_references, indent=4), status=200, mimetype='application/json')

@app.route("/interactions", methods=['GET', 'POST'])
def all_interactions():
    if request.method == 'POST':
        body = request.get_json(silent=True)
        if body is not None and 'query' in body:
            rag_success, answer = cp.rag_pipeline(body['query'])
            if rag_success:
                id = uuid4()
                body['id'] = str(id)
                body['answer'] = answer
                storage['interactions'][str(id)] = body
                return Response(json.dumps(body, indent=4), status=200, mimetype='application/json')
            else:
                return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
        else:
            return Response(json.dumps({'status': 'bad request'}, indent=4), status=400, mimetype='application/json')
    elif request.method == 'GET':
        all_interactions = {
            'items': []
        }
        for k,v in storage['interactions'].items():
            all_interactions['items'].append(v)
        return Response(json.dumps(all_interactions, indent=4), status=200, mimetype='application/json')