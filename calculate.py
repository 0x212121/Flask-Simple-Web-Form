def calc(grouped):
    point = 0

    #check type PC
    if grouped[9] == "HP Compaq Elite 8300 USDT" or grouped[8] == "HP Compaq Elite 8200 USDT":
        return "Tipe PC tidak support"

    #use_office
    if grouped[0] == 'Ya':
        point += 1
    
    #use_smartphone
    if grouped[1] == 'Ya':
        return "Direkomendasikan"

    #use_cloud
    if grouped[2] == 'Ya':
        return "Direkomendasikan"

    #sharing
    if grouped[3] == 'Ya':
        return  "Direkomendasikan"

    #review_docs
    if grouped[4] == 'Ya':
        point += 1
    
    #outside
    if grouped[5] == 'Ya':
        point += 1
    
    #track changes
    if grouped[6] == 'Ya':
        point += 1

    #use_powerapps
    if grouped[7] == 'Ya':
        point += 1

    if point >= 3:
        return "Direkomendasikan"
    elif point < 3:
        return "Tidak direkomendasikan"