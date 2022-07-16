from tkinter import *
import random

counts = {'onion':50,'tomato': 50, 'potato': 50, 'carrot': 50,
        'capsicum': 50, 'cauliflower': 50, 'cabbage': 50,'apple': 50,
        'orange': 50, 'banana': 50, 'pear': 50, 'watermelon': 50,
        'greenGrapes': 50, 'blackGrapes': 50, 'milk': 50, 'ghee': 50,
        'cheese': 50, 'butter': 50, 'curd': 50, 'cream': 50,
        'slimMilk': 50, 'bread': 50, 'bun': 50,'salt': 50,
        'chocolate': 50, 'coke': 50, 'fanta': 50, 'chips': 50}

def showBill():
  class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1725,height = 900)
        self.root.minsize(width = 1725,height = 900)
        self.root.title("Fruits Billing System")
        
        #====================Variables========================#

        # TO DO: EDIT
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.Onions = IntVar()
        self.Tomato = IntVar()
        self.Potato = IntVar()
        self.Carrot = IntVar()
        self.Capsicum = IntVar()
        self.Cauliflower = IntVar()
        self.Cabbage = IntVar()
        self.Apple = IntVar()
        self.Banana = IntVar()
        self.Oranges = IntVar()
        self.Pear = IntVar()
        self.Watermelon = IntVar()
        self.Green_grapes = IntVar()
        self.Black_grapes = IntVar()
        self.Milk = IntVar()
        self.Ghee = IntVar()
        self.Cheese = IntVar()
        self.Butter = IntVar()
        self.Curd = IntVar()
        self.Cream = IntVar()
        self.Slim_milk = IntVar()
        self.Bread = IntVar()
        self.Bun = IntVar()
        self.Salt = IntVar()
        self.Chocolate = IntVar()
        self.Coke = IntVar()
        self.Fanta = IntVar()
        self.Chips = IntVar()
        self.total_Vegetables = StringVar()
        self.total_Fruits = StringVar()
        self.total_Dairy = StringVar()
        self.total_Others = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_Dairy = StringVar()
        self.tax_Others = StringVar()


        #===================================
        bg_color = "lightblue"
        fg_color = "black"
        lbl_color = 'black'
        #Title of App
        title = Label(self.root,text = "Fruits Billing System",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "red",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #==================Vegetables Frame=====================#
        F2 = LabelFrame(self.root,text = 'Vegetables',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 510)

        #===========Frame Content
        #========Onions
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Onions-1kg")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        if counts["onion"] > 0:
            bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Onions)
        else:
            bath_en = Label(F2,font = ("times new roman",15,"bold"),fg = "red",bg = bg_color,text = "Out of stock")
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Tomato
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Tomato-1kg")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        if counts["tomato"] > 0:
            face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Tomato)
        else:
            face_en = Label(F2,font = ("times new roman",15,"bold"),fg = "red",bg = bg_color,text = "Out of stock")
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)
        

        #========Potato
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Potato-1kg")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        if counts["potato"] > 0:
            wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Potato)
        else:
            wash_en = Label(F2,font = ("times new roman",15,"bold"),fg = "red",bg = bg_color,text = "Out of stock")
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Carrot
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Carrot-1kg")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        if counts["carrot"] > 0:
            hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Carrot)
        else:
            hair_en = Label(F2,font = ("times new roman",15,"bold"),fg = "red",bg = bg_color,text = "Out of stock")
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Capsicum
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Capsicum-1kg")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        if counts["capsicum"] > 0:
            lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Capsicum)
        else:
            lot_en = Label(F2,font = ("times new roman",15,"bold"),fg = "red",bg = bg_color,text = "Out of stock")
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #=======Cauliflower
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cauliflower-1")
        face_lbl.grid(row = 5,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Cauliflower)
        face_en.grid(row = 5,column = 1,ipady = 5,ipadx = 5)

        #=======Cabbage
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cabbage-1")
        face_lbl.grid(row = 6,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Cabbage)
        face_en.grid(row = 6,column = 1,ipady = 5,ipadx = 5)

        #==================Fruits Frame=====================#
        F2 = LabelFrame(self.root,text = 'Fruits',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 365,height = 510)

        #===========Frame Content
        Apple_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Apple-1kg")
        Apple_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        Apple_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Apple)
        Apple_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Oranges
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Oranges-1kg")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Oranges)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======Banana
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Banana-1D")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Banana)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Pear
        Pear_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Pear-1kg")
        Pear_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        Pear_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Pear)
        Pear_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #=========Watermelon
        Watermelon_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Watermelon-1")
        Watermelon_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        Watermelon_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Watermelon)
        Watermelon_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #========Green Grapes
        Pear_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Green Grapes-1kg")
        Pear_lbl.grid(row = 5,column = 0,padx = 10,pady = 20)
        Pear_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Green_grapes)
        Pear_en.grid(row = 5,column = 1,ipady = 5,ipadx = 5)

        #========Black Grapes
        Pear_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Black Grapes-1kg")
        Pear_lbl.grid(row = 6,column = 0,padx = 10,pady = 20)
        Pear_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Black_grapes)
        Pear_en.grid(row = 6,column = 1,ipady = 5,ipadx = 5)

        #==================Dairy Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Dairy',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F2.place(x = 695,y = 180,width = 370,height = 510)

        #===========Frame Content
        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Milk-500mL")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Milk)
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Ghee
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Ghee-1L")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Ghee)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======Cheese
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cheese-250g")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Cheese)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Butter
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Butter-500g")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Butter)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Curd
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Curd-500mL")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Curd)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #============Pure Cream
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Pure Cream-150mL")
        bis_lbl.grid(row = 5,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Cream)
        bis_en.grid(row = 5,column = 1,ipady = 5,ipadx = 5)

        #============Slim Milk
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Slim Milk-200mL")
        bis_lbl.grid(row = 6,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Slim_milk)
        bis_en.grid(row = 6,column = 1,ipady = 5,ipadx = 5)

        #==================Others =====================#
        F2 = LabelFrame(self.root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F2.place(x = 1065,y = 180,width = 325,height = 510)

        #=======Bread
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bread-1P")
        cock_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Bread)
        cock_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Bun
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bun-1P")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Bun)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======Salt
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Salt-250g")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Salt)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Chocolate
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Chocolate-1")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Chocolate)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Coke
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke-1")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Coke)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #============Fanta
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Fanta-1")
        bis_lbl.grid(row = 5,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Fanta)
        bis_en.grid(row = 5,column = 1,ipady = 5,ipadx = 5)

        #============Chips
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Chips-1")
        bis_lbl.grid(row = 6,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.Chips)
        bis_en.grid(row = 6,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 1390,y = 180,width = 325,height = 510)
        #===========
        bill_title = Label(F3,text = "Bill List",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 700,relwidth = 1,height = 195)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Vegetables")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_Vegetables)
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Fruits")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_Fruits)
        gro_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Dairy's Total")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_Dairy)
        oth_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Other's Total")
        oth_lbl.grid(row = 3,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_Others)
        oth_en.grid(row = 3,column = 1,ipady = 2,ipadx = 5)

        #================Vegetables Tax
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Vegetables Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================Fruits Tax
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Fruits Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================Dairy Tax
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Dairy Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_Dairy)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

         #==================Others Tax
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Tax")
        otht_lbl.grid(row = 3,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_Others)
        otht_en.grid(row = 3,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Inventory",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.inventory)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 8,ipadx = 20, padx = 30)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 1390,y = 180,width = 325,height = 510)
        #===========
        bill_title = Label(F3,text = "Bill List",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

#Function to get total pApples
    def total(self):
      error = "Items with value entered more than available stock: "
      if self.Onions.get() <= counts["onion"]:
        error += "Onions "
        print(error)
      elif self.Tomato.get() <= counts["tomato"]:
        error += "Tomato "
      elif self.Potato.get() <= counts["potato"]:
        error += "Potato "
      elif self.Carrot.get() <= counts["carrot"]:
        error += "Carrot "
      elif self.Capsicum.get() <= counts["onion"]:
        error += "Capsicum "
      if error == "Items with value entered more than available stock: ":
        #=================Total Vegetables 
        self.total_Vegetables_pApples = (
            (self.Onions.get() * 39)+
            (self.Tomato.get() * 45)+
            (self.Potato.get() * 28.8)+
            (self.Carrot.get() * 50)+
            (self.Capsicum.get() * 72)+
            (self.Cauliflower.get() * 45)+
            (self.Cabbage.get() * 25)
        )
        self.total_Vegetables.set("₹"+str(self.total_Vegetables_pApples))
        self.tax_cos.set("₹"+str(round(self.total_Vegetables_pApples*0.18)))
        #====================Total Fruits 
        self.total_Fruits_pApples = (
            (self.Pear.get()*185)+
            (self.Oranges.get() * 70)+
            (self.Banana.get() * 65)+
            (self.Apple.get() *220)+
            (self.Watermelon.get() * 35)+
            (self.Green_grapes.get() *80)+
            (self.Black_grapes.get() *80)
        )
        self.total_Fruits.set("₹"+str(self.total_Fruits_pApples))
        self.tax_groc.set("₹"+str(round(self.total_Fruits_pApples*0.18)))
        #======================Total Dairy 
        self.total_Dairy_pApples = (
            (self.Milk.get() * 56)+
            (self.Cheese.get() * 118)+
            (self.Ghee.get() * 490)+
            (self.Butter.get() * 50)+
            (self.Curd.get() * 20)+
            (self.Cream.get() * 63)+
            (self.Slim_milk.get() * 82)
        )
        self.total_Dairy.set("₹"+str(self.total_Dairy_pApples))
        self.tax_Dairy.set("₹"+str(round(self.total_Dairy_pApples*0.05)))

        #======================Total Extra 
        self.total_Others_pApples = (
            (self.Bread.get() * 50)+
            (self.Bun.get() * 15)+
            (self.Salt.get() * 22)+
            (self.Chocolate.get() * 30)+
            (self.Coke.get() * 35)+
            (self.Fanta.get() * 35)+
            (self.Chips.get() * 35)
        )
        self.total_Others.set("₹"+str(self.total_Others_pApples))
        self.tax_Others.set("₹"+str(round(self.total_Others_pApples*0.12)))
      else:
          print("Error")

#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Store's Retail\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty         Cost")
        self.txt.insert(END,"\n===================================")

#Function to clear the bill area
    def clear(self):
        self.root.destroy()
        showBill()

#Add Product name, qty and pApple to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.Onions.get() != 0:
            self.txt.insert(END,f"\nOnions             {self.Onions.get()}       {self.Onions.get() * 39}")
            counts["onion"] -= self.Onions.get()
        if self.Tomato.get() != 0:
            self.txt.insert(END,f"\nTomato             {self.Tomato.get()}       {self.Tomato.get() * 45}")
            counts["tomato"] -= self.Tomato.get()
        if self.Potato.get() != 0:
            self.txt.insert(END,f"\nPotato             {self.Potato.get()}       {self.Potato.get() * 28.8}")
            counts["potato"] -= self.Potato.get()
        if self.Carrot.get() != 0:
            self.txt.insert(END,f"\nCarrot             {self.Carrot.get()}       {self.Carrot.get() * 50}")
            counts["carrot"] -= self.Carrot.get()
        if self.Capsicum.get() != 0 :
            self.txt.insert(END,f"\nCapsicum           {self.Capsicum.get()}       {self.Capsicum.get() * 72}")
            counts["capsicum"] -= self.Capsicum.get()
        if self.Cauliflower.get() != 0 :
            self.txt.insert(END,f"\nCauliflower        {self.Cauliflower.get()}       {self.Cauliflower.get() * 45}")
            counts["cauliflower"] -= self.Cauliflower.get()
        if self.Cabbage.get() != 0 :
            self.txt.insert(END,f"\nCabbage            {self.Cabbage.get()}       {self.Cabbage.get() * 25}")
            counts["cabbage"] -= self.Cabbage.get()
        if self.Pear.get() != 0:
            self.txt.insert(END,f"\nPear               {self.Pear.get()}       {self.Pear.get() * 185}")
            counts["pear"] -= self.Pear.get()
        if self.Oranges.get() != 0:
            self.txt.insert(END,f"\nOranges            {self.Oranges.get()}       {self.Oranges.get() * 65}")
            counts["orange"] -= self.Oranges.get()
        if self.Banana.get() != 0:
            self.txt.insert(END,f"\nBanana             {self.Banana.get()}       {self.Banana.get() * 70}")
            counts["banana"] -= self.Banana.get()
        if self.Apple.get() != 0:
            self.txt.insert(END,f"\nApple              {self.Apple.get()}       {self.Apple.get() * 220}")
            counts["apple"] -= self.Apple.get()
        if self.Watermelon.get() != 0:
            self.txt.insert(END,f"\nWatermelon         {self.Watermelon.get()}       {self.Watermelon.get() * 35}")
            counts["watermelon"] -= self.Watermelon.get()
        if self.Green_grapes.get() != 0:
            self.txt.insert(END,f"\nGreen Grapes       {self.Green_grapes.get()}       {self.Green_grapes.get() * 80}")
            counts["greenGrapes"] -= self.Green_grapes.get()
        if self.Black_grapes.get() != 0:
            self.txt.insert(END,f"\nBlack Grapes       {self.Black_grapes.get()}       {self.Black_grapes.get() * 80}")    
            counts["blackGrapes"] -= self.Black_grapes.get()
        if self.Milk.get() != 0:
            self.txt.insert(END,f"\nMilk               {self.Milk.get()}       {self.Milk.get() * 56}")
            counts["milk"] -= self.Milk.get()
        if self.Cheese.get() != 0:
            self.txt.insert(END,f"\nCheese             {self.Cheese.get()}       {self.Cheese.get() * 118}")
            counts["cheese"] -= self.Cheese.get()
        if self.Ghee.get() != 0:
            self.txt.insert(END,f"\nGhee               {self.Ghee.get()}       {self.Ghee.get() * 490}")
            counts["ghee"] -= self.Ghee.get()
        if self.Butter.get() != 0:
            self.txt.insert(END,f"\nButter             {self.Butter.get()}       {self.Butter.get() * 50}")
            counts["butter"] -= self.Butter.get()
        if self.Curd.get() != 0:
            self.txt.insert(END,f"\nCurd               {self.Curd.get()}       {self.Curd.get() * 20}")
            counts["curd"] -= self.Curd.get()
        if self.Cream.get() != 0:
            self.txt.insert(END,f"\nPure Cream         {self.Cream.get()}       {self.Cream.get() * 63}")  
            counts["cream"] -= self.Cream.get()
        if self.Slim_milk.get() != 0:
            self.txt.insert(END,f"\nSlim Milk          {self.Slim_milk.get()}       {self.Slim_milk.get() * 82}")
            counts["slimMilk"] -= self.Slim_milk.get()
        if self.Bread.get() != 0:
            self.txt.insert(END,f"\nBread              {self.Bread.get()}       {self.Bread.get() * 50}")
            counts["bread"] -= self.Bread.get()
        if self.Bun.get() != 0:
            self.txt.insert(END,f"\nBun                {self.Bun.get()}       {self.Bun.get() * 15}")
            counts["bun"] -= self.Bun.get()
        if self.Salt.get() != 0:
            self.txt.insert(END,f"\nSalt               {self.Salt.get()}       {self.Salt.get() * 22}")
            counts["salt"] -= self.Salt.get()
        if self.Chocolate.get() != 0:
            self.txt.insert(END,f"\nChocolate          {self.Chocolate.get()}       {self.Chocolate.get() * 30}")
            counts["chocolate"] -= self.Chocolate.get()
        if self.Coke.get() != 0:
            self.txt.insert(END,f"\nCoco-Cola          {self.Coke.get()}       {self.Coke.get() * 35}")
            counts["coke"] -= self.Coke.get()
        if self.Fanta.get() != 0:
            self.txt.insert(END,f"\nFanta              {self.Fanta.get()}       {self.Fanta.get() * 35}")  
            counts["fanta"] -= self.Fanta.get()
        if self.Chips.get() != 0:
            self.txt.insert(END,f"\nChips              {self.Chips.get()}       {self.Chips.get() * 35}")           
            counts["chips"] -= self.Chips.get()
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                      Total : ₹{self.total_Vegetables_pApples+self.total_Fruits_pApples+self.total_Dairy_pApples+self.total_Vegetables_pApples * 0.05+self.total_Fruits_pApples * 0.05+self.total_Dairy_pApples * 0.05}")

    def inventory(self):
        self.root.destroy()
        from inventory import showInventory
        showInventory()
        

    def exit(self):
        exit()

  root = Tk()
  object = Bill_App(root)
  root.mainloop()
showBill()