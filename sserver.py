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
print(response)


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

if __name__ == '__main__':
    app.run(debug=True)