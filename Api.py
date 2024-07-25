
from flask import Blueprint, jsonify, request
from flask_mysqldb import MySQL
from DBConfig import DatabaseConfig

api = Blueprint('api', __name__)

mysql = MySQL()


@api.route('/test')
def test():
    return jsonify({"message": "Test Route working"}), 200


@api.route('/show')
def showadmin():
    cursor = None
    try:
        cursor = mysql.connection.cursor()
        selectQuery = 'SELECT * FROM admins'
        cursor.execute(selectQuery)
        result = cursor.fetchall()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()


@api.route('/show/<int:id>')
def showById(id):
    cursor = None
    try:
        cursor = mysql.connection.cursor()
        selectIdQuery = 'SELECT * FROM admins WHERE id = %s'
        cursor.execute(selectIdQuery, (id,))
        result = cursor.fetchone()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({"message": "Admin not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()


@api.route('/add', methods=['POST'])
def addData():
    cursor = None
    try:
        _json = request.json
        _name = _json['employee_name']
        _contact = _json['employee_contact']
        _age = _json['employee_age']
        if _name and _contact and _age and request.method == 'POST':
            insertQuery = 'INSERT INTO admins(employee_name, employee_contact, employee_age) VALUES(%s, %s, %s)'
            data = (_name, _contact, _age)
            cursor = mysql.connection.cursor()
            cursor.execute(insertQuery, data)
            mysql.connection.commit()
            return jsonify('User Added Successfully.'), 200
        else:
            return jsonify('Invalid input data'), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()


@api.route('/update/<int:id>',methods=['PUT'])
def UpdateData(id):
    cursor = None
    try:
        _json = request.json
        _name = _json['employee_name']
        _contact = _json['employee_contact']
        _age = _json['employee_age']
        if _name and _contact and _age and request.method == 'PUT':
            UpdateQuery = 'UPDATE admins SET employee_name = %s, employee_contact = %s, employee_age = %s WHERE id = %s'
            data = (_name, _contact, _age, id)
            cursor = mysql.connection.cursor()
            cursor.execute(UpdateQuery, data)
            mysql.connection.commit()
            return jsonify('User Information Updated Successfully.'), 200
        else:
            return jsonify('Invalid input data'), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()

@api.route('/delete/<int:id>',methods=['DELETE'])
def deleteData(id):
    cursor = None
    try:
            cursor = mysql.connection.cursor()
            DeleteQuery = 'DELETE FROM admins WHERE id = %s'
            cursor.execute(DeleteQuery, (id,))
            mysql.connection.commit()
            return jsonify('User Deleted Successfully.'), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor is not None:
            cursor.close()
