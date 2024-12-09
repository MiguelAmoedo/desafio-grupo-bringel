from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pandas as pd
from reportlab.pdfgen import canvas
from flask import send_file
import os
import io
# Inicializando a aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Definindo o modelo de dados para os usuários
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

# Modelo de dados para materiais
class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    material_type = db.Column(db.String(50), nullable=False)
    validity_date = db.Column(db.Date, nullable=False)
    serial = db.Column(db.String(100), nullable=False, unique=True)

# Modelo de dados para etapas do processo
class ProcessStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'), nullable=False)
    step_name = db.Column(db.String(50), nullable=False)
    failure = db.Column(db.Boolean, default=False)

# Rota para criar um usuário
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], role=data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Usuário criado com sucesso!'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = [{'id': user.id, 'name': user.name, 'role': user.role} for user in users]
    return jsonify(result)

# Rota para atualizar um usuário
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    user.role = data.get('role', user.role)
    db.session.commit()
    return jsonify({'message': 'Usuário atualizado com sucesso!'}), 200

# Rota para deletar um usuário
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Usuário deletado com sucesso!'}), 200

# Rota para cadastrar um material
@app.route('/materials', methods=['POST'])
def create_material():
    data = request.get_json()
    serial = f"{data['name'][:3].upper()}-{str(db.session.query(Material).count() + 1)}"
    material = Material(
        name=data['name'],
        material_type=data['material_type'],
        validity_date=data['validity_date'],
        serial=serial
    )
    db.session.add(material)
    db.session.commit()
    return jsonify({'message': 'Material cadastrado com sucesso!', 'serial': material.serial}), 201

@app.route('/materials', methods=['GET'])
def get_materials():
    materials = Material.query.all()
    result = [{'id': material.id, 'name': material.name, 'material_type': material.material_type, 'validity_date': material.validity_date, 'serial': material.serial} for material in materials]
    return jsonify(result)

# Rota para atualizar um material
@app.route('/materials/<int:id>', methods=['PUT'])
def update_material(id):
    material = Material.query.get_or_404(id)
    data = request.get_json()
    material.name = data.get('name', material.name)
    material.material_type = data.get('material_type', material.material_type)
    material.validity_date = data.get('validity_date', material.validity_date)
    db.session.commit()
    return jsonify({'message': 'Material atualizado com sucesso!'}), 200

# Rota para deletar um material
@app.route('/materials/<int:id>', methods=['DELETE'])
def delete_material(id):
    material = Material.query.get_or_404(id)
    db.session.delete(material)
    db.session.commit()
    return jsonify({'message': 'Material deletado com sucesso!'}), 200

# Rota para rastrear um serial
@app.route('/track/<serial>', methods=['GET'])
def track_material(serial):
    material = Material.query.filter_by(serial=serial).first()
    if not material:
        return jsonify({'message': 'Material não encontrado'}), 404
    steps = ProcessStep.query.filter_by(material_id=material.id).all()
    result = [{
        'step_name': step.step_name,
        'failure': step.failure
    } for step in steps]
    return jsonify(result)

# Rota para registrar uma etapa no processo
@app.route('/process_step', methods=['POST'])
def create_process_step():
    data = request.get_json()
    material = Material.query.get_or_404(data['material_id'])
    
    step = ProcessStep(
        material_id=material.id,
        step_name=data['step_name'],
        failure=data.get('failure', False)
    )
    db.session.add(step)
    db.session.commit()
    
    return jsonify({'message': 'Etapa do processo registrada com sucesso!'}), 201

# Geração de relatório em PDF
@app.route('/report/pdf', methods=['GET'])
def generate_pdf_report():
    materials = Material.query.all()
    filename = "report.pdf"
    c = canvas.Canvas(filename)
    c.drawString(100, 800, "Relatório de Materiais Esterilizados")
    y = 780
    for material in materials:
        c.drawString(100, y, f"Serial: {material.serial} - Nome: {material.name}")
        y -= 20
    c.save()
    
    return send_file(filename, as_attachment=True)

# Geração de relatório em Excel
@app.route('/report/xlsx', methods=['GET'])
def generate_xlsx_report():
    materials = Material.query.all()
    data = []
    for material in materials:
        data.append([material.serial, material.name, material.material_type, material.validity_date])
    
    # Criando o DataFrame
    df = pd.DataFrame(data, columns=["Serial", "Nome", "Tipo", "Data de Validade"])

    # Salvando o DataFrame em um arquivo Excel na memória (em vez de salvar no disco)
    output = io.BytesIO()
    df.to_excel(output, index=False, engine='openpyxl')
    output.seek(0)

    # Retornando o arquivo Excel como resposta
    return send_file(output, as_attachment=True, download_name="report.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)
