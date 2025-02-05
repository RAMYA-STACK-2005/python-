from flask import Flask, request, jsonify
app = Flask(__name__)
menu_items = []

@app.route('/')
def home():
    return "menu items"
@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        data = request.get_json()
        menu_items.append(data)
        return jsonify({"message": "Menu item added", "menu": menu_items})
    return jsonify({"menu": menu_items})
@app.route('/menu', methods=['DELETE'])
def delete_menu():
    menu_items.clear()
    return jsonify({"message": "Menu items deleted"})
if __name__ == '__main__':
    app.run(debug=True)