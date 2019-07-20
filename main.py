
# ====================================================== IMPORTING LIBRARIES =======================================================#

from tkinter import *       # FOR G.U.I
from PIL import ImageTk     # FOR IMAGE HEANDLING
import backend_funtionality
from tkinter import messagebox
import database_funtionality

#======================================================= SHOW UPDATED HOSPITAL DETAILS TO HOSPITAL=================================================#
class show_details_to_hospital:
    def __init__(self,canvas,uid):
        self.canvas = canvas
        self.uid = uid

        def home_page_calling():
            self.home.pack_forget()
            self.canvas.pack_forget()
            a = maininterface(window)

        # ====================================================== GETTING DATA OF SELECTED HOSPITAL =======================================================#

        self.data = database_funtionality.hospital_data_get(self.uid)
        print(self.data)

        # ====================================================== NAME OF HOSPITAL WITH RATEING =======================================================#

        self.name_label = Label(self.canvas, text= self.data[0]+"     ( "+str(self.data[9])+" ★ )"
                                ,fg='green',bg='white',
                         font=("arial",20,'bold'))
        self.name_label.place(x=40, y=150)
        self.name_label.pack(padx=10,pady=10,anchor = NW)

        # ====================================================== SHOWING LOCATION =======================================================#

        self.location_label = Label(self.canvas, text="Location : latitude ( "+self.data[3]+") , longitude ("+self.data[4]+")", fg='blue', bg='white',
                                font=("arial", 10, 'bold'))
        self.location_label.place(x=40, y=160)
        self.location_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING MOBILE NO =======================================================#

        self.mobile_label = Label(self.canvas,
                                    text="Mobile no. : " + str(self.data[6]) , fg='blue', bg='white',
                                    font=("arial", 10, 'bold'))
        self.mobile_label.place(x=40, y=170)
        self.mobile_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING GOPD TIMEING =======================================================#

        self.gopd_label = Label(self.canvas,
                                  text="General OPD timing : " + str(self.data[5]), fg='blue', bg='white',
                                  font=("arial", 10, 'bold'))
        self.gopd_label.place(x=40, y=180)
        self.gopd_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING NO. OF AMBULANCE =======================================================#

        self.ambulance_label = Label(self.canvas,
                                text="Ambulance : " + str(self.data[10]), fg='coral', bg='white',
                                font=("arial", 10, 'bold'))
        self.ambulance_label.place(x=40, y=290)
        self.ambulance_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING PHARMACY AVAILABILITY =======================================================#

        self.c = ''
        if(self.data[13] == 0):
            self.c =  'NO'
        else:
            self.c='YES'

        self.pharm_label = Label(self.canvas,
                                     text="Pharmacy Availability : " + str(self.c), fg='coral', bg='white',
                                     font=("arial", 10, 'bold'))
        self.pharm_label.place(x=40, y=300)
        self.pharm_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING I.C.U.=======================================================#

        self.icu_label = Label(self.canvas,
                                 text="I.C.U Available : " + str(self.data[8]) + " / " + str(self.data[7]), fg='coral', bg='white',
                                 font=("arial", 10, 'bold'))
        self.icu_label.place(x=40, y=310)
        self.icu_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING BEDS =======================================================#

        self.bed_label = Label(self.canvas,
                               text="Bed Available : " + str(self.data[12]) + " / " + str(self.data[11]), fg='coral',
                               bg='white',
                               font=("arial", 10, 'bold'))
        self.bed_label.place(x=40, y=320)
        self.bed_label.pack(padx=10, pady=10, anchor=NW)

        #========================================================= BLOOD BANK==============================================================#

        self.name_label = Label(self.canvas, text="BLOOD BANK :", fg='red', bg='white',
                                font=("arial", 15, 'bold'))
        self.name_label.place(x=40, y=475)

        # ====================================================== SHOWING A + BLOOD GROUP =======================================================#

        self.AP_label = Label(self.canvas,text=" A+ : " + str(self.data[15]) + '  UNIT', fg='brown4', bg='white',
                                 font=("arial", 10, 'bold'))
        self.AP_label.place(x=100, y=530)

        # ====================================================== SHOWING A - BLOOD GROUP =======================================================#

        self.AN_label = Label(self.canvas, text=" A- : " + str(self.data[14]) + '  UNIT', fg='brown4', bg='white',
                        font=("arial", 10, 'bold'))
        self.AN_label.place(x=100, y=580)

        # ====================================================== SHOWING B + BLOOD GROUP =======================================================#

        self.BP_label = Label(self.canvas, text=" B+ : " + str(self.data[17]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.BP_label.place(x=225, y=530)

        # ====================================================== SHOWING B - BLOOD GROUP =======================================================#

        self.BN_label = Label(self.canvas, text=" B- : " + str(self.data[16]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.BN_label.place(x=225, y=580)

        # ====================================================== SHOWING AB + BLOOD GROUP =======================================================#

        self.ABP_label = Label(self.canvas, text=" AB+ : " + str(self.data[19]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.ABP_label.place(x=350, y=530)

        # ====================================================== SHOWING AB - BLOOD GROUP =======================================================#

        self.ABN_label = Label(self.canvas, text=" AB- : " + str(self.data[18]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.ABN_label.place(x=350, y=580)

        # ====================================================== SHOWING O + BLOOD GROUP =======================================================#

        self.OP_label = Label(self.canvas, text=" O+ : " + str(self.data[21]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.OP_label.place(x=475, y=530)

        # ====================================================== SHOWING O - BLOOD GROUP =======================================================#

        self.ON_label = Label(self.canvas, text=" O- : " + str(self.data[20]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.ON_label.place(x=475, y=580)

        self.home = Button(text = "<< HOME >>", fg="pink", bg="orange", relief="flat", font=("Comic Sans MS", 10, "bold"),
                           width=10, anchor=W, command= home_page_calling )
        self.home.pack()


# ====================================================== SHOW DETAIL OF SELECTED HOSPITAL FOR SEARCH HOSPITAL near me =======================================================#

class show_details:
    def __init__(self,canvas,uid):
        self.canvas = canvas
        self.uid = uid

        def home_page_calling():
            self.home.pack_forget()
            self.canvas.pack_forget()
            a = maininterface(window)

        # ====================================================== GETTING DATA OF SELECTED HOSPITAL =======================================================#

        self.data = database_funtionality.hospital_data_get(self.uid)
        print(self.data)

        # ====================================================== NAME OF HOSPITAL WITH RATEING BETWEEN TWO LINES =======================================================#

        self.line = canvas.create_line(0, 100, 1920, 100, dash=(4, 2))

        self.name_label = Label(self.canvas, text= self.data[0]+"     ( "+str(self.data[9])+" ★ )"
                                ,fg='green',bg='white',
                         font=("arial",20,'bold'))
        self.name_label.place(x=40, y=150)
        self.name_label.pack(padx=10,pady=10,anchor = NW)

        self.line1 = canvas.create_line(0, 155, 1920, 155, dash=(4, 2))

        # ====================================================== SHOWING LOCATION =======================================================#

        self.location_label = Label(self.canvas, text="Location : latitude ( "+self.data[3]+") , longitude ("+self.data[4]+")", fg='blue', bg='white',
                                font=("arial", 10, 'bold'))
        self.location_label.place(x=40, y=160)
        self.location_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING MOBILE NO =======================================================#

        self.mobile_label = Label(self.canvas,
                                    text="Mobile no. : " + str(self.data[6]) , fg='blue', bg='white',
                                    font=("arial", 10, 'bold'))
        self.mobile_label.place(x=40, y=170)
        self.mobile_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING GOPD TIMEING =======================================================#

        self.gopd_label = Label(self.canvas,
                                  text="General OPD timing : " + str(self.data[5]), fg='blue', bg='white',
                                  font=("arial", 10, 'bold'))
        self.gopd_label.place(x=40, y=180)
        self.gopd_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== CREATING LINE =======================================================#

        self.line2 = canvas.create_line(0, 285, 1920, 285, dash=(4, 2))

        # ====================================================== SHOWING NO. OF AMBULANCE =======================================================#

        self.ambulance_label = Label(self.canvas,
                                text="Ambulance : " + str(self.data[10]), fg='coral', bg='white',
                                font=("arial", 10, 'bold'))
        self.ambulance_label.place(x=40, y=290)
        self.ambulance_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING PHARMACY AVAILABILITY =======================================================#

        self.c = ''
        if(self.data[13] == 0):
            self.c =  'NO'
        else:
            self.c='YES'

        self.pharm_label = Label(self.canvas,
                                     text="Pharmacy Availability : " + str(self.c), fg='coral', bg='white',
                                     font=("arial", 10, 'bold'))
        self.pharm_label.place(x=40, y=300)
        self.pharm_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING I.C.U.=======================================================#

        self.icu_label = Label(self.canvas,
                                 text="I.C.U Available : " + str(self.data[8]) + " / " + str(self.data[7]), fg='coral', bg='white',
                                 font=("arial", 10, 'bold'))
        self.icu_label.place(x=40, y=310)
        self.icu_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== SHOWING BEDS =======================================================#

        self.bed_label = Label(self.canvas,
                               text="Bed Available : " + str(self.data[12]) + " / " + str(self.data[11]), fg='coral',
                               bg='white',
                               font=("arial", 10, 'bold'))
        self.bed_label.place(x=40, y=320)
        self.bed_label.pack(padx=10, pady=10, anchor=NW)

        # ====================================================== CREATING LINE =======================================================#

        self.line3 = canvas.create_line(0, 470, 1920, 470, dash=(4, 2))


        #========================================================= BLOOD BANK==============================================================#

        self.name_label = Label(self.canvas, text="BLOOD BANK :", fg='red', bg='white',
                                font=("arial", 15, 'bold'))
        self.name_label.place(x=40, y=475)

        # ====================================================== CREATING LINE =======================================================#

        self.line4 = canvas.create_line(0, 510, 1920, 510, dash=(4, 2))

        # ====================================================== SHOWING A + BLOOD GROUP =======================================================#

        self.AP_label = Label(self.canvas,text=" A+ : " + str(self.data[15]) + '  UNIT', fg='brown4', bg='white',
                                 font=("arial", 10, 'bold'))
        self.AP_label.place(x=100, y=530)

        # ====================================================== SHOWING A - BLOOD GROUP =======================================================#

        self.AN_label = Label(self.canvas, text=" A- : " + str(self.data[14]) + '  UNIT', fg='brown4', bg='white',
                        font=("arial", 10, 'bold'))
        self.AN_label.place(x=100, y=580)

        # ====================================================== SHOWING B + BLOOD GROUP =======================================================#

        self.BP_label = Label(self.canvas, text=" B+ : " + str(self.data[17]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.BP_label.place(x=225, y=530)

        # ====================================================== SHOWING B - BLOOD GROUP =======================================================#

        self.BN_label = Label(self.canvas, text=" B- : " + str(self.data[16]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.BN_label.place(x=225, y=580)

        # ====================================================== SHOWING AB + BLOOD GROUP =======================================================#

        self.ABP_label = Label(self.canvas, text=" AB+ : " + str(self.data[19]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.ABP_label.place(x=350, y=530)

        # ====================================================== SHOWING AB - BLOOD GROUP =======================================================#

        self.ABN_label = Label(self.canvas, text=" AB- : " + str(self.data[18]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.ABN_label.place(x=350, y=580)

        # ====================================================== SHOWING O + BLOOD GROUP =======================================================#

        self.OP_label = Label(self.canvas, text=" O+ : " + str(self.data[21]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.OP_label.place(x=475, y=530)

        # ====================================================== SHOWING O - BLOOD GROUP =======================================================#

        self.ON_label = Label(self.canvas, text=" O- : " + str(self.data[20]) + '  UNIT', fg='brown4', bg='white',
                              font=("arial", 10, 'bold'))
        self.ON_label.place(x=475, y=580)

        self.home = Button(text="<< HOME >>", fg="pink", bg="orange", relief="flat", font=("Comic Sans MS", 10, "bold"),
                           width=10, anchor=W, command=home_page_calling)
        self.home.pack()


# ====================================================== SHOWING LIST OF HOSPITAL NEAR ME PAGE =======================================================#

class hospital_search_result:
    def __init__(self,canvas):
        self.canvas = canvas

        # ====================================================== GETTING NAME AND UID OF ALL THE HOSPITAL NEAR ME =======================================================#

        self.name_list,self.uid_list = backend_funtionality.hosfinder()

        # ====================================================== TO GO TO SHOW DETAILS OF SELECTED HOSPITAL =======================================================#

        def func(uid):
            self.tip.place_forget()
            self.tip.pack_forget()
            for i in range(0,len(self.name_list)):
                self.button[i].pack_forget()
            page6 = show_details(self.canvas,uid)

        # ====================================================== SHOWING MEASSAGE =======================================================#

        self.tip = Label(self.canvas,text = "CLICK ON HOSPITAL FOR ITS DETAILS : ",fg='red',bg='white', font =("arial",24,"bold"))
        self.tip.place(x=40,y=100)
        self.tip.pack(padx = 10,pady =10)

        # ====================================================== CREATING LIST OF ALL THE HOSPITAL NEAR ME IN FORM OF BUTTON ================================================#

        self.button = list()
        i = 0
        for item in self.name_list:
            self.button.append( Button(self.canvas, text=item, command=lambda x=self.uid_list[i]: func(x)) )
            self.button[i].pack(padx = 10,pady =10,anchor = NW)
            i+=1


# ====================================================== AFTER SIGNUP PAGE =======================================================#

class aftersignup:
    def __init__(self,canvas,name,email,mobile,password):
        self.canvas = canvas
        self.name=name
        self.email=email
        self.mobile=mobile
        self.password=password

        # ====================================================== CREATING USERNAME =======================================================#

        self.username = backend_funtionality.creating_user_username(self.email)
        self.canvas.pack(expand=YES, fill=BOTH)

        # ====================================================== SHOWING USERNAME =======================================================#

        self.aftersignup_username = Label(self.canvas, text="YOUR USER NAME IS :", width=50, height=2, bg="peach puff", relief="solid"
                                   , font=("Times", 10, "bold"))
        self.aftersignup_username.pack(padx=10, pady=10, anchor=CENTER)
        self.aftersignup_username_show = Label(self.canvas, text=self.username, width=30, height=2, bg="white", relief="solid"
                                   , font=("Times", 10, "bold"))
        self.aftersignup_username_show.pack(padx=10, pady=10, anchor=CENTER)

        # ====================================================== SHOWING PASSWORD =======================================================#

        self.aftersignup_password = Label(self.canvas, text="YOUR PASSWORD IS :", width=50, height=2, bg="peach puff", relief="solid"
                                   , font=("Times", 10, "bold"))
        self.aftersignup_password.pack(padx=10, pady=10, anchor=CENTER)
        self.aftersignup_password_show = Label(self.canvas, text=self.password, width=30, height=2, bg="white", relief="solid"
                                   , font=("Times", 10, "bold"))
        self.aftersignup_password_show.pack(padx=10, pady=10, anchor=CENTER)

        # ====================================================== SHOWING SOME TEXT =======================================================#

        self.T = Text(self.canvas, height=2, width=70)
        self.T.pack(padx=10, pady=10, anchor=CENTER)
        self.T.insert(INSERT, "WELCOME , NOW YOU ARE A MEMBER OF L HOSPITAL COMMUNITY :)")

        self.T2 = Text(self.canvas, height=2, width=70)
        self.T2.pack(padx=10, pady=10, anchor=CENTER)
        self.T2.insert(INSERT, "CLICK ON HOME BOTTON :)")

        # ====================================================== TO GO TO HOME PAGE =======================================================#

        def home_page_calling():   # FOR GOING BACK TO THE MAIN INTERFACE
            self.T.pack_forget()
            self.T2.pack_forget()
            self.home.pack_forget()
            self.canvas.pack_forget()
            a = maininterface(window)

        # ====================================================== HOME BUTTON =======================================================#

        self.home = Button(text="<< HOME >> ", fg="pink", bg="orange", relief="flat", font=("Comic Sans MS", 10, "bold"),
                           width=15, anchor=CENTER, command=home_page_calling)
        self.home.pack(padx=10, pady=10)


# ====================================================== SEARCH HOSPITAL BY NAME =======================================================#

class search_hospital_by_name:
    def __init__(self,canvas):
        self.canvas = canvas

        # ====================================================== TO GET DATA FROM DATABASE =======================================================#

        def queary_result():
            self.name = self.search.get()
            self.result = database_funtionality.username_finder(self.name)
            if(self.result=='e'):
                messagebox.showinfo("sorry!!!", "No Such Hospital ")
            else:
                self.search.place_forget()
                self.search_but.place_forget()
                page7 = show_details(self.canvas,self.result)


        self.search = Entry(width = 70,font =('arial',20,'bold'),fg = "plum4", bg = "lavender")
        self.search.place(x= 200 , y = 140 )
        self.search_but = Button(text = 'S E A R C H', width = 10, relief = 'solid',font =('arial',30,'bold'),fg = "plum4", bg = "lavender",command = queary_result)
        self.search_but.place(x=525,y=350)


#======================================================after hospital login =========================================================#
class after_login_hospital:
    def __init__(self,canvas,username,password):
        self.canvas = canvas
        self.username = username
        self.password = password


        #================================== FOR THROWING ERROR =================================================#

        def check():
            if(self.icu_entry.get() == '' or self.icu_entry.get().isnumeric() == FALSE ):
                messagebox.showinfo("WRONG INPUT", "Please enter a valid I.C.U. number")

            elif (self.bed_entry.get() == '' or self.bed_entry.get().isnumeric() == FALSE):
                messagebox.showinfo("WRONG INPUT", "Please enter a valid Bed  number")

            elif (self.AP_entry.get() == '' or self.AP_entry.get().isnumeric() == FALSE):
                messagebox.showinfo("WRONG INPUT", "INVALID ENTRY AT A + BLOOD GROUP FIELD")

            elif (self.AN_entry.get() == '' or self.AN_entry.get().isnumeric() == FALSE):
                messagebox.showinfo("WRONG INPUT", "INVALID ENTRY AT A - BLOOD GROUP FIELD")

            elif (self.BP_entry.get() == '' or self.BP_entry.get().isnumeric() == FALSE):
                messagebox.showinfo("WRONG INPUT", "INVALID ENTRY AT B + BLOOD GROUP FIELD")

            elif (self.BN_entry.get() == '' or self.BN_entry.get().isnumeric() == FALSE):
                messagebox.showinfo("WRONG INPUT", "INVALID ENTRY AT B - BLOOD GROUP FIELD")

            elif (self.ABP_entry.get() == '' or self.ABP_entry.get().isnumeric() == FALSE):
                messagebox.showinfo("WRONG INPUT", "INVALID ENTRY AT AB + BLOOD GROUP FIELD")

            elif (self.ABN_entry.get() == '' or self.ABN_entry.get().isnumeric() == FALSE):
                messagebox.showinfo("WRONG INPUT", "INVALID ENTRY AT AB - BLOOD GROUP FIELD")

            elif (self.OP_entry.get() == '' or self.OP_entry.get().isnumeric() == FALSE):
                messagebox.showinfo("WRONG INPUT", "INVALID ENTRY AT O + BLOOD GROUP FIELD")

            elif (self.ON_entry.get() == '' or self.ON_entry.get().isnumeric() == FALSE):
                messagebox.showinfo("WRONG INPUT", "INVALID ENTRY AT O - BLOOD GROUP FIELD")

            elif(self.ON_entry.get() != ''):
                self.result = database_funtionality.hospial_data_update(self.username , self.icu_entry.get() , self.bed_entry.get() , self.AP_entry.get(),
                                                                        self.AN_entry.get() , self.BP_entry.get() , self.BN_entry.get() , self.ABP_entry.get(),
                                                                        self.ABN_entry.get() , self.OP_entry.get() , self.ON_entry.get())
                if(self.result == 'p'):
                    messagebox.showinfo("UPDATED", "DATA ADDED SUCCESFULLY")
                    self.icu.place_forget()
                    self.icu_entry.place_forget()
                    self.bed.place_forget()
                    self.bed_entry.place_forget()
                    self.AP.place_forget()
                    self.AN.place_forget()
                    self.BP.place_forget()
                    self.BN.place_forget()
                    self.ABP.place_forget()
                    self.ABN.place_forget()
                    self.OP.place_forget()
                    self.ON.place_forget()
                    self.AP_entry.place_forget()
                    self.AN_entry.place_forget()
                    self.BP_entry.place_forget()
                    self.BN_entry.place_forget()
                    self.ABP_entry.place_forget()
                    self.ABN_entry.place_forget()
                    self.OP_entry.place_forget()
                    self.ON_entry.place_forget()
                    self.gen_info.pack_forget()
                    self.name_label.place_forget()
                    self.update.place_forget()
                    page8 = show_details_to_hospital(self.canvas,self.username)
                else:
                    messagebox.showinfo("ERROR", "UNKNOWN ERROR OCCOR")



        #================================================================BUTTONS AND LABEL AND ENTRY BOX FORMATION ==============================#

        data = database_funtionality.hospital_data_get(self.username)


        self.gen_info =Label(self.canvas,text = "NAME     : " + data[0] + "\n"
                                    "UID      : " + data[1] + "\n"
                                    "GEN. OPD : " + data[5]
                             ,relief = "solid", bg = "lavender" ,fg = "forest green", font = ("arial",15,"bold"),width = 50
                             )
        self.gen_info.place(x=850,y=20)
        self.gen_info.pack(padx=10,pady=10)

        self.icu = Label(self.canvas, text="ICU AVAILABLE :", width=20,bg="peach puff", relief="solid")
        self.icu.place(x=5,y=100)
        self.icu_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.icu_entry.place(x=200,y=100)

        self.bed = Label(self.canvas, text="BED AVAILABLE :", width=20, bg="peach puff", relief="solid")
        self.bed.place(x=5, y=130)
        self.bed_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.bed_entry.place(x=200, y=130)


        self.name_label = Label(self.canvas, text="BLOOD BANK :", fg='red', bg='white',
                                font=("arial", 15, 'bold'))
        self.name_label.place(x=5, y=160)


        self.AP = Label(self.canvas, text="A + AVAILABLE :", width=20, bg="peach puff", relief="solid")
        self.AP.place(x=5, y=200)
        self.AP_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.AP_entry.place(x=200, y=200)

        self.AN = Label(self.canvas, text="A - AVAILABLE :", width=20, bg="peach puff", relief="solid")
        self.AN.place(x=5, y=230)
        self.AN_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.AN_entry.place(x=200, y=230)

        self.BP = Label(self.canvas, text="B + AVAILABLE :", width=20, bg="peach puff", relief="solid")
        self.BP.place(x=5, y=260)
        self.BP_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.BP_entry.place(x=200, y=260)

        self.BN = Label(self.canvas, text="B - AVAILABLE :", width=20, bg="peach puff", relief="solid")
        self.BN.place(x=5, y=290)
        self.BN_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.BN_entry.place(x=200, y=290)

        self.ABP = Label(self.canvas, text="AB + AVAILABLE :", width=20, bg="peach puff", relief="solid")
        self.ABP.place(x=5, y=320)
        self.ABP_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.ABP_entry.place(x=200, y=320)

        self.ABN = Label(self.canvas, text="AB - AVAILABLE :", width=20, bg="peach puff", relief="solid")
        self.ABN.place(x=5, y=350)
        self.ABN_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.ABN_entry.place(x=200, y=350)

        self.OP = Label(self.canvas, text="O + AVAILABLE :", width=20, bg="peach puff", relief="solid")
        self.OP.place(x=5, y=380)
        self.OP_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.OP_entry.place(x=200, y=380)

        self.ON = Label(self.canvas, text="O - AVAILABLE :", width=20, bg="peach puff", relief="solid")
        self.ON.place(x=5, y=410)
        self.ON_entry = Entry(self.canvas, width=25, bg="LightBlue3", relief="solid")
        self.ON_entry.place(x=200, y=410)

        self.update = Button(self.canvas, text="UPDATE", width=20,height = 5,bg="peach puff",relief="solid", font=("Times", 10, "bold"),command = check)
        self.update.place(x=600,y=500)





#====================================================== AFTER USER LOGIN PAGE =======================================================#

class after_login_user:
    def __init__(self,canvas,user,password):
        self.canvas = canvas

        # ====================================================== TO GO TO HOSPITAL NEAR ME =======================================================#

        def hospital_search_result_calling():
            self.search_hospital.pack_forget()
            self.search_hospital.place_forget()
            self.hospital_near_me.pack_forget()
            self.hospital_near_me.place_forget()
            page5 = hospital_search_result(self.canvas)

        # ====================================================== TO GO TO SEARCH HOSPITAL =======================================================#

        def search_hospital_calling():
            self.search_hospital.pack_forget()
            self.search_hospital.place_forget()
            self.hospital_near_me.pack_forget()
            self.hospital_near_me.place_forget()
            page6 = search_hospital_by_name(self.canvas)

        # ====================================================== HOSPITAL NEAR ME BUTTON =======================================================#

        self.hospital_near_me = Button(self.canvas, text="HOSPITAL NEAR ME", width=20, height=10, bg="peach puff", relief="solid"
                              , font=("Times", 10, "bold"),command = hospital_search_result_calling)
        self.hospital_near_me.pack(padx=10,pady=10)
        self.hospital_near_me.place(x=500,y=300)

        # ====================================================== SEARCH HOSPITAL BUTTON =======================================================#

        self.search_hospital = Button(self.canvas, text="SEARCH HOSPITAL \n BY NAME", width=20, height=10, bg="peach puff",
                                       relief="solid"
                                       , font=("Times", 10, "bold"), command = search_hospital_calling)
        self.search_hospital.pack(padx=10,pady=10)
        self.search_hospital.place(x=700, y=300)


# ====================================================== LOGIN PAGE =======================================================#

class loginpage:            # LOGIN PAGE LAYOUT
    def __init__(self, canvas):
        self.canvas = canvas
        # ====================================================== USERNAME LABEL AND ENTRY =======================================================#
        self.username = Label(self.canvas, text="Username:", width=100, height=3, bg="peach puff", relief="solid"
                              , font=("Times", 10, "bold"))
        self.username.pack(padx=10, pady=10)
        self.username_entry = Entry(self.canvas, width=50, bg="LightBlue3", relief="solid")
        self.username_entry.pack(padx=10, pady=10)

        # ====================================================== PASSWORD LABEL AND ENTRY =======================================================#

        self.password = Label(self.canvas, text="Password", width=100, height=3, bg="peach puff", relief="solid"
                              , font=("Times", 10, "bold"))
        self.password.pack(padx=10, pady=10)
        self.password_entry = Entry(self.canvas, width=50, bg="LightBlue3", relief="solid",show = '*')
        self.password_entry.pack(padx=10, pady=10)

        # ====================================================== TO GO BACK TO HOME PAGE =======================================================#

        def back_page_calling():   # FOR GOING BACK TO THE MAIN INTERFACE
            self.login.pack_forget()
            self.back.pack_forget()
            self.canvas.pack_forget()
            a = maininterface(window)

        # ====================================================== BACK BUTTON =======================================================#

        self.back = Button(text="<<-- BACK ", fg="pink", bg="orange", relief="flat", font=("Comic Sans MS", 10, "bold"),
                           width=10, anchor=W, command=back_page_calling)
        self.back.pack(padx=10, pady=10)

        # ====================================================== TO CHECK NAME AND PASSWORD IF WRONG SHOW ERROR =======================================================#

        def check_calling():
            result = database_funtionality.user_data_checking(self.username_entry.get(),self.password_entry.get())
            if(result=='pu'):
                self.username.pack_forget()
                self.username_entry.pack_forget()
                self.password.pack_forget()
                self.password_entry.pack_forget()
                self.back.pack_forget()
                self.login.pack_forget()
                messagebox.showinfo("(ツ)", " (ツ) sucessful login")
                if(self.username_entry.get()[:3]=='CLI'):
                    page5 =  after_login_user(self.canvas,self.username_entry.get(),self.password_entry.get())
                else:
                    messagebox.showinfo("WRONG INPUT", "Please enter a valid Userame or Password")
            else:
                messagebox.showinfo("WRONG INPUT", "Please enter a valid Userame or Password")

        # ====================================================== LOGIN BUTTON =======================================================#

        self.login = Button(text="Log in", fg="pink", bg="orange", relief="flat", font=("Comic Sans MS", 20, "bold"),
                            width=30, anchor=N,command = check_calling)
        self.login.pack(padx=10, pady=10)


#====================================================== login PAGE hospital =======================================================#

class loginpagehospital:
    def __init__(self,canvas):
        self.canvas = canvas
        # ====================================================== USERNAME LABEL AND ENTRY =======================================================#
        self.username = Label(self.canvas, text="Username:", width=100, height=3, bg="peach puff", relief="solid"
                              , font=("Times", 10, "bold"))
        self.username.pack(padx=10, pady=10)
        self.username_entry = Entry(self.canvas, width=50, bg="LightBlue3", relief="solid")
        self.username_entry.pack(padx=10, pady=10)

        # ====================================================== PASSWORD LABEL AND ENTRY =======================================================#

        self.password = Label(self.canvas, text="Password", width=100, height=3, bg="peach puff", relief="solid"
                              , font=("Times", 10, "bold"))
        self.password.pack(padx=10, pady=10)
        self.password_entry = Entry(self.canvas, width=50, bg="LightBlue3", relief="solid", show='*')
        self.password_entry.pack(padx=10, pady=10)

        # ====================================================== TO GO BACK TO HOME PAGE =======================================================#

        def back_page_calling():  # FOR GOING BACK TO THE MAIN INTERFACE
            self.login.pack_forget()
            self.back.pack_forget()
            self.canvas.pack_forget()
            a = maininterface(window)

        # ====================================================== BACK BUTTON =======================================================#

        self.back = Button(text="<<-- BACK ", fg="pink", bg="orange", relief="flat", font=("Comic Sans MS", 10, "bold"),
                           width=10, anchor=W, command=back_page_calling)
        self.back.pack(padx=10, pady=10)

        # ====================================================== TO CHECK NAME AND PASSWORD IF WRONG SHOW ERROR =======================================================#

        def check_calling():
            result = database_funtionality.hospital_data_checking(self.username_entry.get(), self.password_entry.get())
            if (result == 'pu'):
                self.username.pack_forget()
                self.username_entry.pack_forget()
                self.password.pack_forget()
                self.password_entry.pack_forget()
                self.back.pack_forget()
                self.login.pack_forget()
                messagebox.showinfo("(ツ)", " (ツ) sucessful login")
                if (self.username_entry.get()[:3] == 'HOS'):
                    page5 = after_login_hospital(self.canvas, self.username_entry.get(), self.password_entry.get())
                    pass
                else:
                    messagebox.showinfo("WRONG INPUT", "Please enter a valid Userame or Password")
            else:
                messagebox.showinfo("WRONG INPUT", "Please enter a valid Userame or Password")

        # ====================================================== LOGIN BUTTON =======================================================#

        self.login = Button(text="Log in", fg="pink", bg="orange", relief="flat", font=("Comic Sans MS", 20, "bold"),
                            width=30, anchor=N, command=check_calling)
        self.login.pack(padx=10, pady=10)


#====================================================== SIGNUP PAGE =======================================================#

class signuppage:   # SIGNUP PAGE LAYOUT
    def __init__(self, canvas):
        self.canvas = canvas

        # ====================================================== FULL NAME LABEL AND ENTRY =======================================================#

        self.signup_fullname = Label(self.canvas, text="FULL NAME:", width=15, height=2, bg="peach puff", relief="solid"
                                     , font=("Times", 10, "bold"))
        self.signup_fullname.pack(padx=10, pady=10, anchor=W)
        self.signup_fullname_entry = Entry(self.canvas, width=50, bg="LightBlue3", relief="solid")
        self.signup_fullname_entry.pack(padx=10, pady=10, anchor=W)

        # ====================================================== FOR GOING BACK TO HOME PAGE =======================================================#

        def back_page_calling():     # FOR GOING BACK TO THE MAIN INTERFACE
            self.signin.pack_forget()
            self.back.pack_forget()
            self.canvas.pack_forget()
            a = maininterface(window)

        # ====================================================== BACK BUTTON TO GO BACK TO HOME PAGE =======================================================#

        self.back = Button(text="<<-- BACK ", fg="pink", bg="orange", relief="flat", font=("Comic Sans MS", 10, "bold"),
                           width=10, anchor=W, command=back_page_calling)
        self.back.pack(padx=10, pady=10)

        # ====================================================== EMAIL LABEL AND ENTRY =======================================================#

        self.signup_email = Label(self.canvas, text="EMAIL :", width=15, height=2, bg="peach puff", relief="solid"
                                  , font=("Times", 10, "bold"))
        self.signup_email.pack(padx=10, pady=10, anchor=SW)
        self.signup_email_entry = Entry(self.canvas, width=50, bg="LightBlue3", relief="solid")
        self.signup_email_entry.pack(padx=10, pady=10, anchor=SW)

        # ====================================================== MOBILE NO. LABEL AND ENTRY =======================================================#

        self.signup_mobile = Label(self.canvas, text="MOBILE :", width=15, height=2, bg="peach puff", relief="solid"
                                   , font=("Times", 10, "bold"))
        self.signup_mobile.pack(padx=10, pady=10, anchor=SW)
        self.signup_mobile_entry = Entry(self.canvas, width=50, bg="LightBlue3", relief="solid")
        self.signup_mobile_entry.pack(padx=10, pady=10, anchor=SW)

        # ====================================================== PASSWORD LABEL AND ENTRY =======================================================#

        self.signup_password = Label(self.canvas, text="PASSWORD :", width=15, height=2, bg="peach puff", relief="solid"
                                     , font=("Times", 10, "bold"))
        self.signup_password.pack(padx=10, pady=10, anchor=SW)
        self.signup_password_entry = Entry(self.canvas, width=50, bg="LightBlue3", relief="solid")
        self.signup_password_entry.pack(padx=10, pady=10, anchor=SW)

        # ====================================================== ADDRESS LABEL AND ENTRY =======================================================#

        self.signup_address = Label(self.canvas, text=" ADDRESS :", width=30, height=2,
                                 bg="peach puff", relief="solid"
                                 , font=("Times", 10, "bold"))
        self.signup_address.pack(padx=10, pady=10, anchor=SW)
        self.signup_address_entry = Entry(self.canvas, width=50, bg="LightBlue3", relief="solid")
        self.signup_address_entry.pack(padx=10, pady=10, anchor=SW)

        # ====================================================== TO GO TO NEXT PAGE OR SHOW POP UP ERRORS =======================================================#

        def aftersignup_calling():
            result = backend_funtionality.cheacking_data(self.signup_fullname_entry.get(),
                                                         self.signup_email_entry.get(),self.signup_mobile_entry.get(),self.signup_password_entry.get())
            self.name = self.signup_fullname_entry.get()
            self.email = self.signup_email_entry.get()
            self.mobile = self.signup_mobile_entry.get()
            self.password = self.signup_password_entry.get()
            self.username = backend_funtionality.creating_user_username(self.email)
            self.address = self.signup_address_entry.get()

            if(result =='e1'):  # INVALID NAME
                messagebox.showinfo("WRONG INPUT", "Please enter a valid Name")
            if (result == 'e2'): #INVALID EMAIL
                messagebox.showinfo("WRONG INPUT", " Please enter a valid Email.")
            if (result == 'e3'): #INVALID PHONE NO.
                messagebox.showinfo("WRONG INPUT", "Please enter a valid Phone Number.")
            elif(result=='p'):
                database_funtionality.user_data_adder(self.name,self.email,self.mobile,self.username,self.password,self.address)
                self.signup_fullname.pack_forget()
                self.signup_fullname_entry.pack_forget()
                self.signup_email.pack_forget()
                self.signup_email_entry.pack_forget()
                self.signup_mobile.pack_forget()
                self.signup_mobile_entry.pack_forget()
                self.signup_password.pack_forget()
                self.signup_password_entry.pack_forget()
                self.signup_address.pack_forget()
                self.signup_address_entry.pack_forget()
                self.back.pack_forget()
                self.signin.pack_forget()
                page4 = aftersignup(self.canvas,self.name,self.email,self.mobile,self.password)

        # ====================================================== SIGNUP BUTTON =======================================================#

        self.signin = Button(text="SIGN IN ", fg="pink", bg="orange", relief="flat", font=("Comic Sans MS", 20, "bold"),
                             width=30, anchor=N,command = aftersignup_calling)
        self.signin.pack(padx=10, pady=10)


#====================================================== HOME PAGE =======================================================#

class maininterface:   # MAIN INTERFACE LAYOUT
    def __init__(self, mainbox): # CONSTRUCTOR HERE MAINBOX = WINDOW
        self.mainbox = mainbox
        # ====================================================== CANVAS MAKING =======================================================#

        self.canvas = Canvas(self.mainbox, width=200, height=200, bg='white')  # MAKING A CANVAS IN MAINBOX
        self.canvas.pack(expand=YES, fill=BOTH)   # PACKING THE CANVAS

        # ====================================================== ADDING HEADING =======================================================#

        self.heading = Label(self.canvas, text="L hospital", fg="pink", bg="white", relief="flat",
                             font=("Comic Sans MS", 50, "bold"),
                             width=100)    # CREATEING HEADING ON CANVAS
        self.heading.pack()  # PACKING HEADING

        # ====================================================== ADDING IMAGE TO THE CANVAS =======================================================#

        self.image = ImageTk.PhotoImage(file="back.jpg")  # MAKING IMAGE OBJECT
        self.canvas.create_image(0, 0, image=self.image, anchor=NW)  # ADING THE IMAGE IN BACKGROUND OF CANVAS

        # ====================================================== TO GO TO LOGIN PAGE USER =======================================================#

        def login_page_calling():   # FOR MOVING INTO LOGIN PAGE
            self.hospital_but.pack_forget()
            self.client_but.pack_forget()
            #self.developer_but.pack_forget()
            self.signup_but.pack_forget()
            page2 = loginpage(self.canvas)

        # ====================================================== TO GO TO LOGIN PAGE HOSPITAL=======================================================#

        def login_page_hospital_calling():  # FOR MOVING INTO LOGIN PAGE
            self.hospital_but.pack_forget()
            self.client_but.pack_forget()
            #self.developer_but.pack_forget()
            self.signup_but.pack_forget()
            self.heading.pack_forget()
            self.canvas.delete("all")
            page2 = loginpagehospital(self.canvas)


        # ====================================================== TO GO TO SIGNUP PAGE PAGE =======================================================#

        def signup_page_calling():  # FOR MOVING TO THE SIGN UP PAGE
            self.hospital_but.pack_forget()
            self.client_but.pack_forget()
            #self.developer_but.pack_forget()
            self.signup_but.pack_forget()
            page3 = signuppage(self.canvas)

        # ====================================================== HOSPITAL LOGIN BUTTON =======================================================#

        self.hospital_but = Button(self.canvas, text="HOSPITAL LOGIN", width=20, height=5, padx=20, pady=20, bg="white",
                                   activebackground='pink', relief="solid", command=login_page_hospital_calling)  # HOSPITAL LOGIN BUTTON
        self.hospital_but.pack(anchor=E, expand=True)

        # ====================================================== CLIENT LOGIN BUTTON =======================================================#

        self.client_but = Button(self.canvas, text="CLIENT LOGIN", width=20, height=5, padx=20, pady=20, bg="white",
                                 activebackground='pink', relief="solid", command=login_page_calling) #CLIENT LOGIN BUTTON
        self.client_but.pack(anchor=E, expand=True)

        # ====================================================== DEVELOPER LOGIN BUTTON =======================================================#

        # self.developer_but = Button(self.canvas, text="DEVELOPER LOGIN", width=20, height=5, padx=20, pady=20,
        #                             bg="white",
        #                             activebackground='pink', relief="solid", command=login_page_calling)
        # self.developer_but.pack(anchor=E, expand=True)  # DEV LOGIN BUTTON

        # ====================================================== SIGNUP BUTTON =======================================================#

        self.signup_but = Button(self.canvas, text="SIGN UP", width=20, height=5, padx=20, pady=20, bg="white",
                                 activebackground='pink', relief="solid", command=signup_page_calling)
        self.signup_but.pack(anchor=E, expand=True)  # SIGNUP BUTTON


#====================================================== MAKING MAIN WINDOW =======================================================#

window = Tk()  # MAKING A WINDOW
window.title("Hospital")  # SETTING THE TITLE OF THE WINDOW
window.geometry("1920x1800+0+0") # SETTING GEOMETRY OF THE WINDOW
a = maininterface(window)  # PASSING THE WINDOW TO MAININTERFACE CLASS

mainloop()
