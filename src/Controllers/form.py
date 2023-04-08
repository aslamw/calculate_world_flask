from flask import request, jsonify
from ..Models import form_schema, db, Form, forms_schema
import json

def form_register(data):
    
    try:
        form = Form(data["name"],data["form"])
        
        db.session.add_all([form])
        db.session.commit()
        
        result = form_schema.dump(form)
        return jsonify({"date":result}),201
    except:
        return jsonify({"menssage":"internal error"}),500
def form_update(id,data):
    
    try:
        form = Form.query.get(id)
        
        if not form :
            return jsonify({"menssage":"form not exist"}),400
        
        form.name = data["name"]
        form.form = data["form"]
        
        db.session.commit()
        result = form_schema.dump(form)
        return jsonify({"date":result}),200
    except:
        return jsonify({"menssage":"internal error"}),304

def form_delete(id):
    try:
        
        form = Form.query.get(id)
        
        if not form :
            return jsonify({"menssage":"form not exist"}),400
        
        db.session.delete(form)
        db.session.commit()
        result = form_schema.dump(form)
        return jsonify({"date":result}),200
    except:
        return jsonify({"menssage":"internal error"}),500

def form_by_name(key,name):
    try:
        form = False
        match key:
            case "name":
                form = Form.query.filter(Form.name == name).one()
            case "form":
                form = Form.query.filter(Form.form == name).one()
        db.session.commit()
        
        if not form :
            return jsonify({"menssage":"name not exist"}),400

        result = form_schema.dump(form)
        return jsonify({"date":result}),200
    except:
        return jsonify({"menssage":"internal error"}),500
    
def all_data():
    
    #try:
    form = Form.query.all()
    
    result = forms_schema.dump(form)
    
    return jsonify({"date":result}),200
        
    """ except:
        return jsonify({"menssage":"internal error"}),500 """
    