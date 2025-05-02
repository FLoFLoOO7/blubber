import os
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request
import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)
id_count = 3
franzset=[
    {"set_id":1,"vorderseite":"magasin","ruckseite":"laden","erledigt":False},
    {"set_id":1,"vorderseite":"magasin","ruckseite":"laden","erledigt":False},
    {"set_id":1,"vorderseite":"magasin","ruckseite":"laden","erledigt":False},
    {"set_id":1,"vorderseite":"magasin","ruckseite":"laden","erledigt":False},
    

]

app = Flask("Mein erster Server")
CORS(app)

@app.route("/api/add",methods=["PUT"])
def add_item():
    new_card=request.get_json()
    franzset.append(new_card)
    print(franzset)
#@app.route('/api/add', methods=['POST'])
#def create_item():
 #   global id_count # Die Variable id_count in der Methode definiert
  #  new_item = request.get_json() # Die Daten des neuen Items werden aus der Anfrage geladen
   # new_item['id'] = id_count # Das neue Item bekommt eine ID
    #id_count += 1 # Der ID-Zähler geht eins hoch, damit dass nächste Item eine neue ID bekommt
#    items.append(new_item) # Das neue Item wird der Liste der Items angehängt
 #   response = jsonify({"message": "Item created", "items": items})
  #  response.headers.add('Access-Control-Allow-Origin', '*')
   # return response, 201

#@app.route('/api/items/<int:item_id>', methods=['PUT'])
#def update_item(item_id):
#    print(item_id)
    # Wir überprüfen, ob die item_id gültig ist. Das wird hier sehr einfach gemacht und müsste in echt noch etwas ausführlicher geprüft werden.
#    if item_id >= len(items):
    # Falls nicht geben wir eine Fehlermeldung zurück
#        return jsonify({"error": "Item not found"}), 404
    # Wir holen das geupdatete Item aus dem JSON der Anfrage
 #   updated_item = request.get_json()
    # Und packen es in unserer Liste und überschreiben somit das bisherige item an dieser Stelle
  #  items[item_id] = updated_item
    # Zum schluss senden wir eine Erfolgsmeldung zurück sowie die aktualisierte Liste mit Items
   # response = jsonify({"message": "Item updated", "items": items})
#    response.headers.add('Access-Control-Allow-Origin', '*')
 #   return response

if __name__ == '__main__':
    app.run(debug=True)