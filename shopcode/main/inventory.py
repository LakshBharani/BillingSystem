from tkinter import *
import random
from bill import counts

def showInventory():
  class Show_Inventory:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1635,height = 900)
        self.root.minsize(width = 1635,height = 900)
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

        #===================================
        bg_color = "lightblue"
        fg_color = "black"
        lbl_color = 'black'
        title = Label(self.root,text = "Inventory",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)
        
        #==================Vegetables Frame=====================#
        F2 = LabelFrame(self.root,text = 'Vegetables',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 510)

        #===========Frame Content
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Onions")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["onion"])
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Tomato
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Tomato")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["tomato"])
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)
        

        #========Potato
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Potato")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["potato"])
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Carrot
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Carrot")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["carrot"])
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Capsicum
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Capsicum")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["capsicum"])
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #=======Cauliflower
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cauliflower")
        face_lbl.grid(row = 5,column = 0,padx = 10,pady = 20)
        face_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["cauliflower"])
        face_en.grid(row = 5,column = 1,ipady = 5,ipadx = 5)

        #=======Cabbage
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cabbage")
        face_lbl.grid(row = 6,column = 0,padx = 10,pady = 20)
        face_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["cabbage"])
        face_en.grid(row = 6,column = 1,ipady = 5,ipadx = 5)

        #==================Fruits Frame=====================#
        F2 = LabelFrame(self.root,text = 'Fruits',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 510)

        #===========Frame Content
        Apple_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Apple")
        Apple_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        Apple_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["apple"])
        Apple_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Oranges
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Oranges")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["orange"])
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======Banana
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Banana")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["banana"])
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Pear
        Pear_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Pear")
        Pear_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        Pear_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["pear"])
        Pear_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #=========Watermelon
        Watermelon_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Watermelon")
        Watermelon_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        Watermelon_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["watermelon"])
        Watermelon_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #========Green Grapes
        Pear_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Green Grapes")
        Pear_lbl.grid(row = 5,column = 0,padx = 10,pady = 20)
        Pear_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["greenGrapes"])
        Pear_en.grid(row = 5,column = 1,ipady = 5,ipadx = 5)

        #========Black Grapes
        Pear_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Black Grapes")
        Pear_lbl.grid(row = 6,column = 0,padx = 10,pady = 20)
        Pear_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["blackGrapes"])
        Pear_en.grid(row = 6,column = 1,ipady = 5,ipadx = 5)

        #==================Dairy Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Dairy',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 510)

        #===========Frame Content
        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Milk")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["milk"])
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Ghee
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Ghee")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["ghee"])
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======Cheese
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Cheese")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["cheese"])
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Butter
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Butter")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["butter"])
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Curd
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Curd")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["curd"])
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #============Pure Cream
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Pure Cream")
        bis_lbl.grid(row = 5,column = 0,padx = 10,pady = 20)
        bis_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["cream"])
        bis_en.grid(row = 5,column = 1,ipady = 5,ipadx = 5)

        #============Slim Milk
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Slim Milk")
        bis_lbl.grid(row = 6,column = 0,padx = 10,pady = 20)
        bis_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["slimMilk"])
        bis_en.grid(row = 6,column = 1,ipady = 5,ipadx = 5)

        #==================Others =====================#
        F2 = LabelFrame(self.root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "red",font = ("times new roman",13,"bold"))
        F2.place(x = 980,y = 180,width = 325,height = 510)

        #=======Bread
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bread")
        cock_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        cock_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["bread"])
        cock_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Bun
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bun")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["bun"])
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======Salt
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Salt")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["salt"])
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Chocolate
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Chocolate")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["chocolate"])
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Coke
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["coke"])
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #============Fanta
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Fanta")
        bis_lbl.grid(row = 5,column = 0,padx = 10,pady = 20)
        bis_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["fanta"])
        bis_en.grid(row = 5,column = 1,ipady = 5,ipadx = 5)

        #============Chips
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Chips")
        bis_lbl.grid(row = 6,column = 0,padx = 10,pady = 20)
        bis_en = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = counts["chips"])
        bis_en.grid(row = 6,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 1305,y = 180,width = 325,height = 510)
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
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 8,ipadx = 20, padx = 30)

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 1305,y = 180,width = 325,height = 510)
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
        self.txt.delete('1.0',END)

#Add Product name , qty and pApple to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.Onions.get() != 0:
            self.txt.insert(END,f"\nOnions             {self.Onions.get()}       {self.Onions.get() * 39}")
        if self.Tomato.get() != 0:
            self.txt.insert(END,f"\nTomato             {self.Tomato.get()}       {self.Tomato.get() * 45}")
        if self.Potato.get() != 0:
            self.txt.insert(END,f"\nPotato             {self.Potato.get()}       {self.Potato.get() * 28.8}")
        if self.Carrot.get() != 0:
            self.txt.insert(END,f"\nCarrot             {self.Carrot.get()}       {self.Carrot.get() * 50}")
        if self.Capsicum.get() != 0 :
            self.txt.insert(END,f"\nCapsicum           {self.Capsicum.get()}       {self.Capsicum.get() * 72}")
        if self.Cauliflower.get() != 0 :
            self.txt.insert(END,f"\nCauliflower        {self.Cauliflower.get()}       {self.Cauliflower.get() * 45}")
        if self.Cabbage.get() != 0 :
            self.txt.insert(END,f"\nCabbage            {self.Cabbage.get()}       {self.Cabbage.get() * 25}")
        if self.Pear.get() != 0:
            self.txt.insert(END,f"\nPear               {self.Pear.get()}       {self.Pear.get() * 185}")
        if self.Oranges.get() != 0:
            self.txt.insert(END,f"\nOranges            {self.Oranges.get()}       {self.Oranges.get() * 65}")
        if self.Banana.get() != 0:
            self.txt.insert(END,f"\nBanana             {self.Banana.get()}       {self.Banana.get() * 70}")
        if self.Apple.get() != 0:
            self.txt.insert(END,f"\nApple              {self.Apple.get()}       {self.Apple.get() * 220}")
        if self.Watermelon.get() != 0:
            self.txt.insert(END,f"\nWatermelon         {self.Watermelon.get()}       {self.Watermelon.get() * 35}")
        if self.Green_grapes.get() != 0:
            self.txt.insert(END,f"\nGreen Grapes       {self.Green_grapes.get()}       {self.Green_grapes.get() * 80}")
        if self.Black_grapes.get() != 0:
            self.txt.insert(END,f"\nBlack Grapes       {self.Black_grapes.get()}       {self.Black_grapes.get() * 80}")    
        if self.Milk.get() != 0:
            self.txt.insert(END,f"\nMilk               {self.Milk.get()}       {self.Milk.get() * 56}")
        if self.Cheese.get() != 0:
            self.txt.insert(END,f"\nCheese             {self.Cheese.get()}       {self.Cheese.get() * 118}")
        if self.Ghee.get() != 0:
            self.txt.insert(END,f"\nGhee               {self.Ghee.get()}       {self.Ghee.get() * 490}")
        if self.Butter.get() != 0:
            self.txt.insert(END,f"\nButter             {self.Butter.get()}       {self.Butter.get() * 50}")
        if self.Curd.get() != 0:
            self.txt.insert(END,f"\nCurd               {self.Curd.get()}       {self.Curd.get() * 20}")
        if self.Cream.get() != 0:
            self.txt.insert(END,f"\nPure Cream         {self.Cream.get()}       {self.Cream.get() * 63}")  
        if self.Slim_milk.get() != 0:
            self.txt.insert(END,f"\nSlim Milk          {self.Slim_milk.get()}       {self.Slim_milk.get() * 82}")
        if self.Bread.get() != 0:
            self.txt.insert(END,f"\nBread              {self.Bread.get()}       {self.Bread.get() * 50}")
        if self.Bun.get() != 0:
            self.txt.insert(END,f"\nBun                {self.Bun.get()}       {self.Bun.get() * 15}")
        if self.Salt.get() != 0:
            self.txt.insert(END,f"\nSalt               {self.Salt.get()}       {self.Salt.get() * 22}")
        if self.Chocolate.get() != 0:
            self.txt.insert(END,f"\nChocolate          {self.Chocolate.get()}       {self.Chocolate.get() * 30}")
        if self.Coke.get() != 0:
            self.txt.insert(END,f"\nCoco-Cola          {self.Coke.get()}       {self.Coke.get() * 35}")
        if self.Fanta.get() != 0:
            self.txt.insert(END,f"\nFanta              {self.Fanta.get()}       {self.Fanta.get() * 35}")  
        if self.Chips.get() != 0:
            self.txt.insert(END,f"\nChips              {self.Chips.get()}       {self.Chips.get() * 35}")           
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                      Total : ₹{self.total_Vegetables_pApples+self.total_Fruits_pApples+self.total_Dairy_pApples+self.total_Vegetables_pApples * 0.05+self.total_Fruits_pApples * 0.05+self.total_Dairy_pApples * 0.05}")

    def bill(self):
        self.root.destroy()
        from bill import showBill
        showBill()

    def exit(self):
        exit()


  root = Tk()
  object = Show_Inventory(root)
  root.mainloop()