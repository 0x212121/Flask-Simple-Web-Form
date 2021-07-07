from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from waitress import serve
from filtering import filter_badge, filter_hostname, filter_type
from get_username import get_username
import calculate
import re

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'assessment'
app.secret_key = "super secret key"

mysql = MySQL(app)

@app.route('/')
def index():
    ip_address = request.remote_addr
    return render_template("index.html", ipa = ip_address)

@app.route('/assessment', methods=["GET", "POST"])
def assessment():
    if request.method == "POST":
        errors = False
        try:
            name = request.form["name"]
            # re_name = re.match("^[a-zA-Z0-9]*$", name)
            # if re_name is not None:
            form_name = get_username(name)
            cur = mysql.connection.cursor()
            is_duplicate = cur.execute(f"SELECT * FROM results WHERE fullname = '{form_name}'")
            if (is_duplicate > 0):
                flash('Username sudah digunakan untuk menginput data!')
                errors = True
        except:
            flash('Logon username salah, silahkan periksa kembali :)')
            errors = True
            
        badge = request.form["badge"].upper()
        form_host = request.form["hostname"].upper()
        filter_host = filter_hostname(form_host)
        check_badge = filter_badge(badge)
        if check_badge is None:
            flash('Format badge number salah!')
            errors = True
        if filter_host is None:
            flash('Format computer name salah!')
            errors = True
            
        pc_model = filter_type(form_host)
        cur = mysql.connection.cursor()
        is_duplicate = cur.execute(f"SELECT * FROM results WHERE hostname = '{form_host}'")
        if (is_duplicate):
            flash('Computer name sudah ada di database!')
            errors = True
        if (errors):
            return redirect(url_for('index'))
        
        return render_template("assessment.html", hostname=form_host, name=form_name, badge=badge, type_pc=pc_model)
    elif request.method == "GET":
        return redirect(url_for('index'))
        # return render_template("assessment.html")

@app.route('/result', methods=["GET", "POST"])
def result():
    if request.method == "POST":
        name = request.form['name']
        hostname = request.form['hostname']
        badge = request.form['badge']
        type_pc = request.form['type-pc']

        use_mobile = request.form['use_mobile']
        sharing = request.form['sharing_file']
        use_cloud = request.form['use_cloud']
        onlineform = request.form['onlineform']
        registered = request.form['registered']
        use_powerbi = request.form['use_powerbi']
        use_macro = request.form['use_macro']
        kpc_mail = request.form['kpc_mail']
        vpn_user = request.form['vpn_user']
        paham_o365 = request.form['paham_o365']

        grouped = [use_mobile, sharing, use_cloud, onlineform, registered,
        use_powerbi, use_macro, kpc_mail, vpn_user, paham_o365, type_pc]

        results = calculate.calc(grouped)
        cur = mysql.connection.cursor()
        is_duplicate = cur.execute(f"SELECT * FROM results WHERE fullname = '{name}'")
        if not is_duplicate:
            cur.execute(""" INSERT INTO results
            (fullname, hostname, badge, use_mobile, sharing_file, use_cloud, onlineform, registered,
            use_powerbi, use_macro, kpc_mail, vpn_user, paham_o365, result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s)""", (name, hostname, badge, use_mobile, sharing, use_cloud,
            onlineform, registered, use_powerbi, use_macro, kpc_mail, vpn_user, paham_o365, results))
            mysql.connection.commit()

        return render_template('result.html', use_officex = results)
    elif request.method == "GET":
        return redirect(url_for('index'))

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/data')
def data():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM results")
    data = cur.fetchall()
    return render_template('data.html', data=data)

if __name__== '__main__':
    app.run(debug=True)
    # serve(app, host='0.0.0.0', port=5000, threads=4)
