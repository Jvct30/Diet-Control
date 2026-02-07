from flask import Flask, request, jsonify  
from models.snack import Snack # modelo de snack
from models.database import db # banco de dados


app = Flask(__name__) # incia o programa
app.config["SECRET_KEY"] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://admindiet:admindiet@127.0.0.1:3306/Diet-control" #config do banco de dados
db.init_app(app)

@app.route("/snack", methods=["POST"]) # pega os dados no postman, separa e adiciona no banco de dados
def create_snack():
    data = request.json 
    name = data.get("name")
    description = data.get("description")
    date = data.get("date")
    time = data.get("time")
    in_diet = data.get("in_diet")

    if data and name and description and date and time and in_diet:
        snack=Snack(name=name, description=description, date=date, time=time, in_diet=in_diet)
        db.session.add(snack)
        db.session.commit()
        return jsonify({"message":"Snack adicionado com sucesso!"}), 201
    return jsonify({"message":"informações faltando"}), 400

@app.route("/snack", methods=["GET"]) # le todos os snacks no banco
def read_snacks():
    # Passa por todos os snacks na lista
    snacks = Snack.query.all()

    # cria uma lista temporaria
    result = []

    #para cada snack no banco ele adiciona na lista
    for snack in snacks:
        result.append({
            "id": snack.id,
            "name": snack.name,
            "description": snack.description,
            "date": snack.date,
            "time": snack.time,
            "in_diet": snack.in_diet  
        })
    return jsonify(result), 200
    
@app.route("/snack/<int:id>", methods=["GET"])
def read_snack(id):
    # procura no banco o id
    snack = Snack.query.get(id)
    # se tiver executa 
    if snack:
        return jsonify({
            "id": snack.id,
            "name": snack.name,
            "description": snack.description,
            "date": snack.date,
            "time": snack.time,
            "in_diet": snack.in_diet
        })
    return jsonify({"message":"snack não encontrado"}), 404
    
@app.route("/snack/<int:id>", methods=["PUT"])
def update_snack(id):
    # procura no banco o id
    snack = Snack.query.get(id)
    # se tiver executa 
    if snack:
        data = request.json
        snack.name = data.get("name")
        snack.description = data.get("description")
        snack.date = data.get("date")
        snack.time = data.get("time")
        snack.in_diet = data.get("in_diet")
        db.session.commit()
        return jsonify({"message":"snack atualizado com sucesso!"})
    return jsonify({"message":"snack não encontrado"}), 404

@app.route("/snack/<int:id>", methods=["DELETE"])
def delete_snack(id):
    # procura no banco o id
    snack = Snack.query.get(id)
    # se tiver executa: 
    if snack:
        db.session.delete(snack)
        db.session.commit()
        return jsonify({"message":f"snack {id} deletado com sucesso!"})
    return jsonify({"message":"snack não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)