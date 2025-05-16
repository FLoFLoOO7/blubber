import os
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request
import os
from supabase import create_client, Client


url: str = "https://adndzfjcagmnkeyozqcc.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFkbmR6ZmpjYWdtbmtleW96cWNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU1NzA0NTQsImV4cCI6MjA2MTE0NjQ1NH0.U0li70uT1cU-tu1J81J9CTL-9PxM_5P_HAPPFR47hdQ"
supabase: Client = create_client(url, key)
id_count = 3
response = (
    supabase.table("Karteikarten")
    .select("*")
    .execute()
    
)



app = Flask("Mein erster Server")
CORS(app)
#Florian
@app.route("/api/add_card",methods=["POST"])
def add_item():
    new_card=request.get_json()
    response_add = (
        supabase.table("Karteikarten")
        .insert(new_card)
        .execute()
    )
    
    response = (
    supabase.table("Karteikarten")
    .select("*")
    .execute()
    
    )
    response=jsonify({"message": "Item created"})
    response.headers.add("Access-Control-Allow-Origin","*")
    return response, 201
@app.route("/api/add_set",methods=["POST"])
def add_set():
    new_card=request.get_json()
    response_add = (
        supabase.table("Sets")
        .insert(new_card)
        .execute()
    )
    
    response = (
    supabase.table("Karteikarten")
    .select("*")
    .execute()
    
    )
    response=jsonify({"message": "Item created"})
    response.headers.add("Access-Control-Allow-Origin","*")
    return response, 201

@app.route("/api/cards/<int:set_id>", methods=["GET"])
def loadSet(set_id):
    response = (
        supabase.table("Karteikarten")
        .select("*")
        .eq("SET_ID", set_id)
        .execute()
    )
    cards = response.data
    return jsonify(cards)



@app.route("/api/sets", methods=["GET"])
def get_sets():
    response = supabase.table("Sets").select("*").execute()
    sets = response.data
    return jsonify(sets)




@app.route("/api/erledigt", methods=["PUT"])
def markAsErledigt():
    try:
        data = request.get_json()
        card_id = data.get("id")
        if not card_id:
            response = jsonify({"error": "No card ID provided"})
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response, 400

        supabase.table("Karteikarten").update({"erledigt": True}).eq("id", card_id).execute()
        
        response = jsonify({"message": "Card marked as erledigt"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 200
    except Exception as e:
        # <-- WICHTIG: Fehler sichtbar machen
        print("Fehler in /api/erledigt:", str(e))
        response = jsonify({"error": str(e)})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response, 500


    
@app.route("/api/set_reset", methods=["PUT"])
def reset_set_cards():
    data = request.get_json()
    set_id = data.get("SET_ID")
#ChatGPT: fragte Chat, warum es manchmal error gab
    if not set_id:
        return jsonify({"error": "No SET_ID provided"}), 400
#Bis hier
    supabase.table("Karteikarten").update({"erledigt": False}).eq("SET_ID", set_id).execute()
    #ChatGPT
    response = jsonify({"message": "Card marked as erledigt"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    
#ChatGPT
    return jsonify({"message": "Cards reset"}), 200




if __name__ == '__main__':
    app.run(debug=True)