import sqlite3
from flask import Flask, session, render_template, request, g, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"
app.config["SESSION_COOKIE_NAME"] = "myCOOKIE_monSTER528"

@app.route("/", methods=["POST", "GET"])
def index():
    db = getattr(g, '_database', None)
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clients'")
    table_exists = cur.fetchone() is not None
    if table_exists:
        print("טבלה קיימת במסד הנתונים")
    else:
        print("טבלה לא קיימת במסד הנתונים")
        cur.execute("CREATE TABLE clients (cID INTEGER PRIMARY KEY,customerlastname TEXT,customerfirstname TEXT,city TEXT,street TEXT,phone INTEGER,cellphone INTEGER,dob DATE,streetnumber INTEGER, picture TEXT)")
        print("טבלה נוצרה בהצלחה")
        cur.execute('''CREATE TABLE corona_vaccination (
            id INTEGER PRIMARY KEY,
            vaccination_date_1 DATE,
            manufacturer_1 TEXT,
            vaccination_date_2 DATE,
            manufacturer_2 TEXT,
            vaccination_date_3 DATE,
            manufacturer_3 TEXT,
            vaccination_date_4 DATE,
            manufacturer_4 TEXT,
            positive_result_date DATE,
            recovery_date DATE
            )''')
    if db is None:
        db = g._database = sqlite3.connect('example.db')
        cursor_names = db.cursor()
        cursor_names.execute("SELECT customerfirstname, customerlastname FROM clients")
        all_name_data = cursor_names.fetchall()
        names_data = []
        for row in all_name_data:
            formatted_row = ' '.join(map(str, row))
            names_data.append(formatted_row)
        print(names_data)

        cursor_address = db.cursor()
        cursor_address.execute("SELECT city, street, streetnumber FROM clients")
        all_address_data = cursor_address.fetchall()
        address_data = []
        for row in all_address_data:
            formatted_address = ' '.join(map(str, row))
            address_data.append(formatted_address)
        print(address_data)

        cursor_id = db.cursor()
        cursor_id.execute("SELECT cID FROM clients")
        all_id_data = cursor_id.fetchall()
        id_data = [str(val[0]) for val in all_id_data]
        print(id_data)

        cursor_pic = db.cursor()
        cursor_pic.execute("SELECT picture FROM clients")
        all_pic_data = cursor_pic.fetchall()
        pic_data = [str(val[0]) for val in all_pic_data]
        print(pic_data)
    else:
        db = g._database = sqlite3.connect('example.db')
        cursor_names = db.cursor()
        cursor_names.execute("SELECT customerfirstname, customerlastname FROM clients")
        all_name_data = cursor_names.fetchall()
        names_data = []
        for row in all_name_data:
            formatted_row = ' '.join(map(str, row))
            names_data.append(formatted_row)
        print(names_data)

        cursor_address = db.cursor()
        cursor_address.execute("SELECT city, street, streetnumber FROM clients")
        all_address_data = cursor_address.fetchall()
        address_data = []
        for row in all_address_data:
            formatted_address = ' '.join(map(str, row))
            address_data.append(formatted_address)
        print(address_data)

        cursor_id = db.cursor()
        cursor_id.execute("SELECT cID FROM clients")
        all_id_data = cursor_id.fetchall()
        id_data = [str(val[0]) for val in all_id_data]
        print(id_data)
    return render_template("Home_page.html", names = names_data, address = address_data, ids = id_data, pics = pic_data)

#@app.route("/add_clientfile", methods=["GET"])
#def add_clientfile():
#    return render_template("AddClient_page.html")

@app.route("/add_client", methods=["POST","GET"])
def add_client():
    if request.method == 'POST':
        print("hygtrf")
        customerfirstname = request.form['customerfirstname']
        dob = request.form['dob']
        customerlastname = request.form['customerlastname']
        streetnumber = request.form['streetnumber']
        cellphone = request.form['cellphone']
        cID = request.form['ID']
        city = request.form['city']
        street = request.form['street']
        phone = request.form['phone']
        picture = request.form['picture']
        print("2")
        conn = sqlite3.connect('example.db')
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clients'")
        table_exists = cur.fetchone() is not None
        if table_exists:
            print("טבלה קיימת במסד הנתונים")
        else:
            print("טבלה לא קיימת במסד הנתונים")
            cur.execute("CREATE TABLE clients (cID INTEGER PRIMARY KEY,customerlastname TEXT,customerfirstname TEXT,city TEXT,street TEXT,phone INTEGER,cellphone INTEGER,dob DATE,streetnumber INTEGER, picture TEXT)")
            print("טבלה נוצרה בהצלחה")
            cur.execute('''CREATE TABLE corona_vaccination (
                id INTEGER PRIMARY KEY,
                vaccination_date_1 DATE,
                manufacturer_1 TEXT,
                vaccination_date_2 DATE,
                manufacturer_2 TEXT,
                vaccination_date_3 DATE,
                manufacturer_3 TEXT,
                vaccination_date_4 DATE,
                manufacturer_4 TEXT,
                positive_result_date DATE,
                recovery_date DATE
                )''')

        cur.execute("INSERT INTO clients (cID, customerlastname, customerfirstname, city, street, phone, cellphone, dob, streetnumber, picture) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                (cID, customerlastname, customerfirstname, city, street, phone, cellphone, dob, streetnumber, picture))


        conn.commit()
        conn.close()
        response = 'Clients registered successfully'
        return redirect("/")
    return render_template("AddClient_page.html")

@app.route("/view_client", methods=["GET", "POST"])
def viewclientprofile():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    if request.method == "GET":
        client_id = request.args.get('id')
        cursor.execute("SELECT * FROM clients WHERE cID=?", (client_id,))
        client_data = cursor.fetchone()
        cursor.execute("SELECT * FROM corona_vaccination WHERE id=?", (client_id,))
        corona_data = cursor.fetchone()
        conn.close()
        print(corona_data)
        return render_template("ViewClient_page.html", client_data=client_data,corona_data = corona_data)
    if request.method == "POST":
        client_id = request.form['ID']
        customerfirstname = request.form['customerfirstname']
        dob = request.form['dob']
        customerlastname = request.form['customerlastname']
        streetnumber = request.form['streetnumber']
        cellphone = request.form['cellphone']
        city = request.form['city']
        street = request.form['street']
        phone = request.form['phone']
        vac1 = request.form['vaccination_date_1']
        vac2 = request.form['vaccination_date_2']
        vac3 = request.form['vaccination_date_3']
        vac4 = request.form['vaccination_date_4']
        manu1 = request.form['manufacturer_1']
        manu2 = request.form['manufacturer_2']
        manu3 = request.form['manufacturer_3']
        manu4 = request.form['manufacturer_4']
        prdate = request.form['positive_result_date']
        recdate = request.form['recovery_date']
        cursor.execute("UPDATE clients SET customerlastname=?, customerfirstname=?, city=?, street=?, phone=?, cellphone=?, dob=?, streetnumber=? WHERE cID=?", (customerlastname, customerfirstname,city,street,phone,cellphone,dob ,streetnumber, client_id))
        cursor.execute("INSERT INTO corona_vaccination (id, vaccination_date_1, manufacturer_1, vaccination_date_2, manufacturer_2, vaccination_date_3, manufacturer_3, vaccination_date_4, manufacturer_4, positive_result_date, recovery_date)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" ,
                        (client_id, vac1,manu1,vac2,manu2,vac3,manu3 ,vac4, manu4, prdate, recdate))
        conn.commit() 
        conn.close()
        return redirect("/") 



    """client_id = request.args.get('id')
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE cID=?", (client_id,))
    client_data = cursor.fetchone()
    conn.close()
    return render_template("ViewClient_page.html", client_data = client_data)"""

@app.route("/del_client", methods=["post", "GET"])
def delete_client():
    print("hiidktgh i am so tired")
    client_id = request.args.get('id')
    
    print(client_id)
    #checked = request.form["remove_b"]
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM clients WHERE cID=?", (client_id,))
    conn.commit()
    conn.close()

    return redirect("/")


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()