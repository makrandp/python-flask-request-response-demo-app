from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]

@app.route('/')
def index():
    return jsonify({"success" : True , "result" : "Use /store route"})

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def createStore():
    request_data = request.get_json()
    app.logger.info(request_data)

    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


#get /store
@app.route('/stores')
def get_stores():
  return jsonify({'stores': stores})


#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'success' : False, 'message': 'store not found'})



#post /store/<name> data: {name : , price: }
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()

  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})


#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})



app.run(port=5000)