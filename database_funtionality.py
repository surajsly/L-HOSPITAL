
# ====================================================== IMPORTING SQL TO PYTHON CONNECTOR  =======================================================#

import mysql.connector


# ====================================================== ADD DATA TO DATABASE =======================================================#

def user_data_adder(name,email,mobile,username,dbpassword,address):

    # ====================================================== ACCESSING DATABASE =======================================================#

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='user_authentication'
    )

    # ====================================================== CREATING CURSOR =======================================================#

    mycursor = mydb.cursor()

    inserting_formula = "INSERT INTO user_data (name,email,mobile,username,pass,address) VALUES (%s,%s,%s,%s,%s,%s)"
    inserting_values = ( name,email,mobile,username,dbpassword,address )
    print(inserting_values)
    mycursor.execute(inserting_formula,inserting_values)
    mydb.commit()


# ====================================================== CHECKING FOR VALID DATA =======================================================#

def user_data_checking(username,password):
    front = username[:3]
    if(front == "DEV" or front == "HOS" or front == "CLI"):
        if(front == 'CLI'):


            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='user_authentication'
            )

            mycursor = mydb.cursor(buffered=True)

            comd = "SELECT username From user_data WHERE username  = %s "
            mycursor.execute(comd,(username,))
            row_count = mycursor.fetchone()[0]
            print(row_count)
            if(row_count == 0):
                return 'e1'
            else:
                comd = "SELECT pass From user_data WHERE username  = %s "
                mycursor.execute(comd,(username,))
                dbpass = mycursor.fetchone()[0]
                print(dbpass)
                if(password == dbpass ):
                    return 'pu'
                else:
                    return 'e1'
    else:
        return 'e2'


# ====================================================== ADDING NEW HOSPITAL IGNORE IF ALREADY EXIST =======================================================#

def hospital_data_entry(name,username,password,lat,lng,gopd,pn,icu,a_icu,rateing,ambulance,bed,a_bed,pharmacy
                        ,a_n_unit,a_p_unit,b_n_unit,b_p_unit,ab_n_unit,ab_p_unit,o_n_unit,o_p_unit):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='user_authentication'
    )

    mycursor = mydb.cursor(buffered=True)
    comd = "SELECT username From hospital_data WHERE username  = %s "
    mycursor.execute(comd, (username,))
    row_count = mycursor.fetchall()
    if (len(row_count) ==  0): # code from here
        comd1 = "INSERT INTO hospital_data(name,username,password,lat,lng,GOPD_time,phoneno,icu,avilable_icu,rateing,ambulance,total_bed,avilable_bed,pharmacy," \
           "A_N_unit,A_p_unit,B_N_unit,B_p_unit,AB_N_unit,AB_p_unit,O_N_unit,O_p_unit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (name,username,password,lat,lng,gopd,pn,icu,a_icu,rateing,ambulance,bed,a_bed,pharmacy
                        ,a_n_unit,a_p_unit,b_n_unit,b_p_unit,ab_n_unit,ab_p_unit,o_n_unit,o_p_unit)
        mycursor.execute(comd1,val)
    else:
        pass
    mydb.commit()


# ====================================================== GETTING HOSPITAL DATA FROM DATABASE =======================================================#

def hospital_data_get(username):

    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='user_authentication'
    )

    mycursor = mydb.cursor(buffered=True)
    comd = "SELECT * From hospital_data WHERE username  = %s "
    mycursor.execute(comd, (username,))
    data = mycursor.fetchone()
    return data


#====================================================== FINDING USERNAME OF HOSPITAL FROM ITA NAME=================================================#

def username_finder(name='S'):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='user_authentication'
    )

    mycursor = mydb.cursor(buffered=True)
    comd = "SELECT username From hospital_data WHERE name  = %s "
    mycursor.execute(comd, (name,))
    username = mycursor.fetchall()
    if (len(username) == 0):
        return 'e'
    else:
        comd = "SELECT username From hospital_data WHERE name  = %s "
        mycursor.execute(comd, (name,))
        username = mycursor.fetchall()[0][0]
        return username


#====================================================== CHECKING VALID DATA FOR HOSPITAL ========================================================#

def hospital_data_checking(username,password):
    front = username[:3]
    if (front == "DEV" or front == "HOS" or front == "CLI"):
        if (front == 'HOS'):

            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='1234',
                database='user_authentication'
            )

            mycursor = mydb.cursor(buffered=True)

            comd = "SELECT username From hospital_data WHERE username  = %s "
            mycursor.execute(comd, (username,))
            row_count = mycursor.fetchone()
            #print(row_count)
            if (row_count == None):
                return 'e1'
            else:
                comd = "SELECT password From hospital_data WHERE username  = %s "
                mycursor.execute(comd, (username,))
                dbpass = mycursor.fetchone()[0]
                if (password == dbpass):

                    return 'pu'
                else:
                    return 'e1'
    else:
        return 'e2'


#====================================================== UPDATING HOSPITAL DATA ==================================================================#

def hospial_data_update(username,a_icu=0,a_bed=0,AP=0,AN=0,BP=0,BN=0,ABP=0,ABN=0,OP=0,ON=0):
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='user_authentication'
    )

    mycursor = mydb.cursor(buffered=True)
    input = ( a_icu,a_bed,AP,AN,BP,AN,ABP,ABN,OP,ON,username )
    query = 'UPDATE hospital_data SET avilable_ICU = %s , avilable_bed = %s , A_p_unit = %s , A_N_unit = %s , B_p_unit = %s , B_N_unit = %s ,' \
            ' AB_p_unit = %s , AB_N_unit = %s , O_p_unit = %s , O_N_unit = %s WHERE username = %s'
    mycursor.execute(query,input)
    mydb.commit()
    return 'p'
    print('yeh')

hospital_data_checking('HOS-SPH@28.678.77.224','PASS-HOS-SPH@28.678.77.224')
