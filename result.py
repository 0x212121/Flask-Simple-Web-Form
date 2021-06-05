def result():

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