from werkzeug.exceptions import RequestEntityTooLarge
from templates.get_username import get_username
from check_hostname import checkhostname
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from waitress import serve
import calculate

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
            form_name = get_username(name)
            cur = mysql.connection.cursor()
            is_duplicate = cur.execute(f"SELECT * FROM results WHERE fullname = '{form_name}'")
            if (is_duplicate):
                flash('Username sudah digunakan untuk menginput data')
                errors = True
                # return redirect(url_for('index'))
            form_host = request.form["hostname"].upper()
            badge = request.form["badge"]
            # print(f"nama: {form_name}")
            pc_model = checkhostname(form_host)
        except:
            # no_logon_name = True
            flash('Logon username salah, silahkan periksa kembali :)')
            errors = True
            # return redirect(url_for('index'))
    elif request.method == "GET":
        return redirect(url_for('index'))

    # Check duplicate hostname saat input
    cur = mysql.connection.cursor()
    is_duplicate = cur.execute(f"SELECT * FROM results WHERE hostname = '{form_host}'")
    # print(f"is_duplicate: {is_duplicate}")
    if (is_duplicate):
        flash('Hostname sudah ada di database')
        errors = True
        # return redirect(url_for('index'))
    if (errors):
        return redirect(url_for('index'))
    
    return render_template("assessment.html", hostname=form_host, name=form_name, badge=badge, type_pc=pc_model)

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
        use_powerapps = request.form['use_powerapps']
        use_powerbi = request.form['use_powerbi']
        use_macro = request.form['use_macro']
        kpc_mail = request.form['kpc_mail']
        vpn_user = request.form['vpn_user']
        paham_o365 = request.form['paham_o365']

        grouped = [use_mobile, sharing, use_cloud, use_powerapps,
        use_powerbi, use_macro, kpc_mail, vpn_user, paham_o365, type_pc]

        results = calculate.calc(grouped)
        cur = mysql.connection.cursor()
        cur.execute(""" INSERT INTO results
        (fullname, hostname, badge, use_mobile, sharing_file, use_cloud, use_powerapps,
        use_powerbi, use_macro, kpc_mail, vpn_user, paham_o365, result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 
        %s, %s, %s, %s)""", (name, hostname, badge, use_mobile, sharing, use_cloud,
        use_powerapps, use_powerbi, use_macro, kpc_mail, vpn_user, paham_o365, results))
        mysql.connection.commit()

        return render_template('result.html', use_officex = results)
    elif request.method == "GET":
        return redirect(url_for('index'))

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
    # app.run(debug=True)
    serve(app, host='0.0.0.0', port=5000)
