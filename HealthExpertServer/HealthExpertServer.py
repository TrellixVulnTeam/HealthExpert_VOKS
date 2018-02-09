from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import json, os
import hashlib

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hedb'
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
mysql = MySQL(app)


# JSONResponses
# Register Status


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/auth/register/doctor', methods=['POST', 'GET'])
def user_register():
    if request.method == 'POST':
        data = request.data
        dataD = json.loads(data)
        name = dataD['name'].encode('utf-8')
        emailid = dataD['emailid'].encode('utf-8')
        accesstoken = hashlib.sha256(emailid).hexdigest()
        regid = dataD['regid'].encode('utf-8')
        speciality = dataD['speciality'].encode('utf-8')
        city = dataD['city'].encode('utf-8')
        gender = dataD['gender'].encode('utf-8')
        pincode = dataD['pincode'].encode('utf-8')
        experience = dataD['experience'].encode('utf-8')
        phoneno = dataD['phoneno'].encode('utf-8')
        password = hashlib.sha256(dataD['password'].encode('utf-8')).hexdigest()
        file = request.files['image']
        photo = accesstoken + file.filename
        f = os.path.join(app.config['UPLOAD_FOLDER'], photo)
        f.save(f)
        status = 0
        r_id = 2
        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO doctor(d_name,d_phoneno,d_regid,d_gender,d_speciality,d_experience,d_city,d_pincode,d_accesstoken,d_photo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
            (name, phoneno, regid, gender, speciality, experience, city, pincode, accesstoken, photo))
        cur.execute('''INSERT into users(u_accesstoken,u_emailid,u_password,u_status,r_id) values(%s,%s,%s,%s,%s)''',
                    (accesstoken, emailid, password, status, r_id))
        mysql.connection.commit()
        return jsonify(status=True,
                       message="Registered Successfully")


@app.route('/auth/register/patient/icon', methods=['POST', 'GET'])
def patient_register_icon():
    if request.method == 'POST':
        data = request.data
        dataD = json.loads(data)
        name = dataD['name'].encode('utf-8')
        dob = dataD['dob'].encode('utf-8')
        height = dataD['height'].encode('utf-8')
        weight = dataD['weight'].encode('utf-8')
        emailid = dataD['emailid'].encode('utf-8')
        occupation = dataD['occupation'].encode('utf-8')
        symptoms = dataD['symptoms'].encode('utf-8')
        bloodgroup = dataD['bloodgroup'].encode('utf-8')
        history = dataD['history'].encode('utf-8')
        investigations = dataD['investigations'].encode('utf-8')
        mothersname = dataD['mothersname'].encode('utf-8')
        mothersymptom = dataD['mothersymptom'].encode('utf-8')
        fathername = dataD['fathername'].encode('utf-8')
        fathersymptom = dataD['fathersymptom'].encode('utf-8')
        accesstoken = hashlib.sha256(emailid).hexdigest()
        city = dataD['city'].encode('utf-8')
        gender = dataD['gender'].encode('utf-8')
        pincode = dataD['pincode'].encode('utf-8')
        phoneno = dataD['phoneno'].encode('utf-8')
        password = hashlib.sha256(dataD['password'].encode('utf-8')).hexdigest()
        file = request.files['image']
        photo = accesstoken + file.filename
        f = os.path.join(app.config['UPLOAD_FOLDER'], photo)
        f.save(f)
        status = 1
        r_id = 3
        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO patient(p_name,p_dob,p_gender,p_height,p_weight,p_accesstoken,p_phoneno,p_occupation,p_symptoms,p_bloodgroup,p_history,p_investigations,p_city,p_pincode,p_mothername,p_mothersymptoms,p_fathername,p_fathersymptoms,p_photo) 
              values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
            (name, dob, gender, height, weight, accesstoken, phoneno, occupation, symptoms, bloodgroup, history,
             investigations, city, pincode, mothersname, mothersymptom, fathername, fathersymptom, photo))
        cur.execute('''INSERT into users(u_accesstoken,u_emailid,u_password,u_status,r_id) values(%s,%s,%s,%s,%s)''',
                    (accesstoken, emailid, password, status, r_id))
        mysql.connection.commit()
        return jsonify(status=True,
                       message="Registered Successfully")


@app.route('/auth/register/patient/noicon', methods=['POST', 'GET'])
def patient_register_noicon():
    if request.method == 'POST':
        data = request.data
        dataD = json.loads(data)
        name = dataD['name'].encode('utf-8')
        dob = dataD['dob'].encode('utf-8')
        height = dataD['height'].encode('utf-8')
        weight = dataD['weight'].encode('utf-8')
        emailid = dataD['emailid'].encode('utf-8')
        occupation = dataD['occupation'].encode('utf-8')
        symptoms = dataD['symptoms'].encode('utf-8')
        bloodgroup = dataD['bloodgroup'].encode('utf-8')
        history = dataD['history'].encode('utf-8')
        investigations = dataD['investigations'].encode('utf-8')
        mothersname = dataD['mothername'].encode('utf-8')
        mothersymptom = dataD['mothersymptoms'].encode('utf-8')
        fathername = dataD['fathername'].encode('utf-8')
        fathersymptom = dataD['fathersymptoms'].encode('utf-8')
        accesstoken = hashlib.sha256(emailid).hexdigest()
        city = dataD['city'].encode('utf-8')
        gender = dataD['gender'].encode('utf-8')
        pincode = dataD['pincode'].encode('utf-8')
        phoneno = dataD['phoneno'].encode('utf-8')
        password = hashlib.sha256(dataD['password'].encode('utf-8')).hexdigest()
        status = 1
        r_id = 3
        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO patient(p_name,p_dob,p_gender,p_height,p_weight,p_accesstoken,p_phoneno,p_occupation,p_symptoms,p_bloodgroup,p_history,p_investigations,p_city,p_pincode,p_mothername,p_mothersymptoms,p_fathername,p_fathersymptoms) 
              values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
            (name, dob, gender, height, weight, accesstoken, phoneno, occupation, symptoms, bloodgroup, history,
             investigations, city, pincode, mothersname, mothersymptom, fathername, fathersymptom))
        cur.execute('''INSERT into users(u_accesstoken,u_emailid,u_password,u_status,r_id) values(%s,%s,%s,%s,%s)''',
                    (accesstoken, emailid, password, status, r_id))
        mysql.connection.commit()
        return jsonify(status=True,
                       message="Registered Successfully")


@app.route('/auth/login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        data = request.data
        dataD = json.loads(data)
        emailid = dataD['emailid'].encode('utf-8')
        password = hashlib.sha256(dataD['password'].encode('utf-8')).hexdigest()
        cur = mysql.connection.cursor()
        cur.execute(
            '''SELECT u_status,u_accesstoken,r_id FROM users where u_emailid = %s AND u_password= %s LIMIT 1''',
            (emailid, password))
        if cur.rowcount == 0:
            return jsonify(status=False,
                           message="Invalid EmailId / Password")
        else:
            for row in cur:
                if row[0] == 0:
                    return jsonify(status=False,
                                   message="Registration hasn't verified!")
                else:
                    return jsonify(status=True,
                                   message="Login Successful",
                                   accessToken=row[1],
                                   role=row[2])


@app.route('/doctor/patient/symptoms', methods=['GET', 'POST'])
def get_symptoms():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('SELECT s_id,s_name FROM symptom ORDER BY s_name ASC')
        list_data = []
        for row in cur:
            dataDict = {'id': row[0], 'sname': row[1]}
            list_data.append(dataDict)
        return jsonify(data=list_data)


@app.route('/doctor/mypatients', methods=['GET', 'POST'])
def get_mypatients():
    if request.method == 'POST':
        data = request.data
        dataD = json.loads(data)
        accesstoken = dataD['accessToken'].encode('utf-8')
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM patient where d_accesstoken=%s''', (accesstoken))
        list_data = []
        for row in cur:
            dataDict = {'pid': row[0],
                        'name': row[1],
                        'dob': row[2],
                        'gender': row[3],
                        'height': row[4],
                        'weight': row[5],
                        'emailid': row[6],
                        'phoneno': row[7],
                        'occupation': row[8],
                        'symptoms': row[9],
                        'history': row[10],
                        'investigations': row[11],
                        'city': row[12],
                        'pincode': row[13],
                        'mothername': row[14],
                        'mothersymptoms': row[15],
                        'fathername': row[16],
                        'fathersymptoms': row[17],
                        'photo': row[18]
                        }
            list_data.append(dataDict)

        return jsonify(data=list_data)


# TODO Patient + PatientDetails
@app.route('/doctor/patients', methods=['GET', 'POST'])
def get_patients():
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM patient ORDER BY p_name ''')
        list_data = []
        for row in cur:
            dataDict = {'pid': row[0],
                        'name': row[1],
                        'dob': row[2],
                        'gender': row[3],
                        'height': row[4],
                        'weight': row[5],
                        'emailid': row[6],
                        'phoneno': row[7],
                        'occupation': row[8],
                        'symptoms': row[9],
                        'history': row[10],
                        'investigations': row[11],
                        'city': row[12],
                        'pincode': row[13],
                        'mothername': row[14],
                        'mothersymptoms': row[15],
                        'fathername': row[16],
                        'fathersymptoms': row[17],
                        'photo': row[18]
                        }
            list_data.append(dataDict)

        return jsonify(data=list_data)


@app.route('/admin/doctors', methods=['GET', 'POST'])
def get_doctors():
    if request.method == 'POST':

        cur = mysql.connection.cursor()
        cur.execute(
            '''SELECT d_name,d_emailid,d_phoneno,d_pincode,d_city,d_speciality,d_gender,d_experience,d_regid,d_accesstoken FROM doctor INNER JOIN users on doctor.d_accesstoken = users.u_accesstoken  AND r_id=2 ''')
        list_data = []
        for row in cur:
            dataDict = {'name': row[0],
                        'emailid': row[1],
                        'phoneno': row[2],
                        'pincode': row[3],
                        'city': row[4],
                        'speciality': row[5],
                        'gender': row[6],
                        'experience': row[7],
                        'regid': row[8],
                        'accesstoken': row[9]}
            list_data.append(dataDict)

        return jsonify(data=list_data)


@app.route('/admin/doctors/status', methods=['GET', 'POST'])
def status_doctor():
    if request.method == 'POST':
        data = request.data
        dataD = json.loads(data)
        accesstoken = dataD['accesstoken'].encode('utf-8')
        status = dataD['status'].encode('utf-8')
        cur = mysql.connection.cursor()
        cur.execute(
            '''UPDATE users SET u_status = %s where u_accesstoken = %s''',
            (status, accesstoken))
        mysql.connection.commit()
        if status != 99:
            return jsonify(status=True,
                           message="Doctor Verified")
        else:
            return jsonify(status=True,
                           message="Doctor Rejected")


if __name__ == '__main__':
    app.run(host='192.168.0.103', port=5000)
