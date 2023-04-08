from flask import Blueprint, request, jsonify
from ..Controllers import \
    form_register, form_update, form_delete, form_by_name, all_data
import json

api_form = Blueprint('form', __name__)

@api_form.get("/teste")
def test():
    return 'oi'

@api_form.post("/form/register")
def register(): 
    data = json.loads(request.data)
    return form_register(data)

@api_form.put("/form/update/<id>") 
def update(id):
    data = json.loads(request.data)
    return form_update(id,data)

@api_form.delete("/form/delete/<id>") 
def delete(id):
    
    return form_delete(id)
@api_form.get("/form/get") 
def get_name():
    data = json.loads(request.data)
    type_key = list(data.keys())[0]
    print(type_key)
    
    if not type_key in ["name", "form"]:
        return jsonify({"menssage":"type not exist"}),400

    return form_by_name(type_key,data[type_key])
@api_form.get("/form/all")
def get_all():
    
    return all_data()