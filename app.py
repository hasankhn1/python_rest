from flask import Flask, jsonify, request


class NoStoreFound(ValueError):
  def __init__(self, msg):
      self.msg = msg

  def __str__(self):
      return self.msg


app = Flask(__name__)

stores = [{
    'name': 'My Wonderful store',
    'items': [
        {
            'name': 'chicken', 'price': '200'},
        {
            'name': 'salad', 'price': '100'
        }]
}]


@app.route('/store', methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
      'name': request_data['name'],
      'items': []
  }
  stores.append(new_store)
  return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store_by_name(name):
  for store in stores:
    if store['name'] == name:
      return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store')
def get_store():
  return jsonify({'stores': stores})


@app.route('/store/<string:name>/items', methods=['POST'])
def create_item(name):
  request_data = request.get_json()
  for store in stores:
    if(store['name'] == name):
      print(store)
      new_item = {
          'name': request_data['name'],
          'price': request_data['price']
      }
      store['items'].append(new_item)
      return jsonify({'stores':stores})
  return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/items')
def get_items_in_store(name):
  for store in stores:
    if store['name'] == name:
      return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


app.run(port=5000)
