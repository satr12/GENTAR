import tkinter as tk
from tkinter import *
import numpy as np


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        # border = tk.LabelFrame(self, text='Login', bg='ivory', bd = 10, font=("Arial", 20))
        # border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        border = tk.LabelFrame(self, bg='ivory', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes")

        T1 = tk.Label(self, text="GENTAR BALOK BESAR", font=("Arial Bold", 15), bg='ivory')
        T1.place(x=300, y=50)

        T2 = tk.Label(self, text="(GENERATOR MOMEN DAN LENDUTAN BALOK BESAR)", font=("Arial Bold", 10), bg='ivory')
        T2.place(x=250, y=100)



        B1 = tk.Button(border, text="Balok B10", font=("Arial",15),height=10,bg="gray",width=30, command=lambda: controller.show_frame(balokb10))
        B1.pack(side=LEFT,anchor=S,pady=50,padx=(20,0))
        B2 = tk.Button(border, text="Balok B14", font=("Arial",15),height=10,bg="gray",width=30, command=lambda: controller.show_frame(balokb14))
        B2.pack(side=RIGHT,pady=50,anchor=S,padx=(0,20))

 
        
class balokb10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        border = tk.LabelFrame(self, bg='ivory', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes")
        
        L1 = tk.Label(border, text="GENTAR : BALOK B10", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=300, y=20)
        

        
        #### Perhitungan perumusan Ql dan Qd
        bebanmati = 125
        bebanhidup = 479
        Qd = bebanmati*8
        Ql = bebanhidup*8
        L = 24
        selimut = 40

        
        
        def tumpuan():
            #Momen ditumpuan 

 
            D = 25
            b = 700
            x = L/4
            tulangantumpuan = 32
            As = round(0.25*np.pi*D**2*tulangantumpuan,2)
            at = round(((As*fy.get())/(0.85*fc.get()*b)),2)
            d = round(800-selimut-D/2,2)

            q = round(1.2*Qd+1.6*Ql,2)
            Mntumpuan = round(((q*L/4)/2*(L-(L/4))),2)
            Mn = round(0.9*As*fy.get()*(d-0.5*at)/10/1000,2)


            textbox.insert(
                END,
                'KAPASITAS MOMEN TUMPUAN'
                )           

            textbox.insert(
                END,
                '\nUntuk momen terjadi di tumpuan yang berada di 1/4 L ='+str(x)+' m'
                )            
            
            textbox.insert(
                END,
                '\nMomen diTumpuan yang tejadi pada balok\nMmaxs = ((q x x)/2) x(L-x)\n'
                +'= ('+str(q)+' x '+str(x)+')/2 x ('+str(L)+'-'+ str(x)+') ='+ str(Mntumpuan)+' kg.m'            
                )

            textbox.insert(
                END,
                '\nØMn = 0.9 x As x fy x(d - 0.5 a) \n=  0.9 x'+
                str(As)+" x "+str(fy.get())+' x ('+str(d)+' - 0.5 x '+str(at)+')'
                + ' = '+ str('{:0,.2f}'.format(Mn))+' kg.m\n'+'\nmaka : '
                )
            if Mn < Mntumpuan :
                    textbox.insert(
                        END,
                        'ØMn = '+str(Mn) 
                        + (' > ') #harus difungsikan 
                        +'Mmax = '+str(Mntumpuan)+' (OK)\n\n'
                        )
            else :
                    textbox.insert(
                        END,
                        'ØMn = '+str(Mn) 
                        + ('<') #harus difungsikan 
                        +'Mmax = '+str(Mntumpuan)+' (Tidak OK)\n\n'
                        )               

        def lapangan():
            #Momen ditumpuan 

            D = 25
            b = 700
            tulanganlapangan = 24
            As = round(0.25*np.pi*D**2*tulanganlapangan,2)
            a = round((As*fy.get())/(0.85*fc.get()*b),2)
            d = round(800-selimut-D/2,2)

            q = round(1.2*Qd+1.6*Ql,2)
            Mnlapangan = round(1/8*q*L**2,2)
            Mn = round(0.9*As*fy.get()*(d-0.5*a)/10/1000,2) 



            textbox.insert(
                END,
                'KAPASITAS MOMEN LAPANGAN'
                )            

            
            textbox.insert(
                END,
                '\nMomen diLapangan yang tejadi pada balok\nMmaxs = 1/8 x q x L ^ 2\n'
                +'= 1/8 x '+str(q)+' x '+str(L**2)+' = '+ str(Mnlapangan)+' kg.m'
                )

            textbox.insert(
                END,
                '\nØMn = 0.9 x As x fc x(d - 0.5 a) \n=  0.9 x'+
                str(As)+" x "+str(fc.get())+' x ('+str(d)+' - 0.5 x '+str(a)+')'
                + ' = '+ str('{:0,.2f}'.format(Mn))+' kg.m\n'+'\nmaka : '
                )

            ####TUGAS DI FUNGSIKAN 
            if Mn < Mnlapangan :
                    textbox.insert(
                        END,
                        'ØMn = '+str(Mn) 
                        + (' < ') #harus difungsikan 
                        +'Mmax = '+str(Mnlapangan)+' (OK)\n\n'
                        )
            else :
                    textbox.insert(
                        END,
                        'ØMn = '+str(Mn) 
                        + ('<') #harus difungsikan 
                        +'Mmax = '+str(Mnlapangan)+' (Tidak OK)\n\n'
                        )                    

        
        
        def lendutan():
            #Momen diLendutan


            b = 700
            h = 800
            Li = L*1000

            q = round((1.2*Qd+1.6*Ql)*10/1000,2)
            E = round(4700*np.sqrt(fc.get()),2)
            I = round(1/12*b*h**3,2)

            Δmaks = round((5*q*Li**4)/(384*E*I),2)

            Δijin = round(Li/240,2)

            textbox.insert(
                END,
                'KAPASITAS LENDUTAN'
                )           

            textbox.insert(
                END,
                '\nKombinasi pembebanan 1.2D + 1.6L (q)  =\n'
                +'= 1.2 x '+str(Qd)+'+ 1.6 x '+str(Ql)+' = '
                + str(q)+' N/mm'
                )
            textbox.insert(
                END,
                '\nE = 4700 x √fc \n'
                +'= 4700 x '+str(Qd)+' + 1.6 x √'+str(fc.get())+' = '
                + str(q)+' N/mm^2'
                )
            textbox.insert(
                END,
                '\nI = 1/12 x b x h^3 \n'
                +'= 1/12 x '+str(b)+' x '+str(h)+'^3 \n= '
                + str(q)+' mm^4'
                )
            
            textbox.insert(
                END,
                '\nΔ maks = (5 x q x L^4)/(384 x E x I) \n=  (5 x '+
                str(q)+" x "+str(Li)+'^4) /  (384 x '+str(E)+' x '+str(I)+')'
                + ' = '+ str(Δmaks)+' mm'
                )

            textbox.insert(
                END,
                '\nΔ ijin = L / 240 \n= '+
                str(L)+" / 240 "+ ' = '+ str('{:0,.2f}'.format(Δijin))+' mm\n'+'\nmaka : '
                )
            if Δmaks > Δijin :
                    textbox.insert(
                        END,
                        'Δ Maks = '+str(Δmaks) 
                        + (' > ') #harus difungsikan 
                        +'Mmax = '+str(Δijin)+' (OK)\n\n'
                        )
            else :
                    textbox.insert(
                        END,
                        'Δ Maks = '+str(Δmaks) 
                        + (' < ') #harus difungsikan 
                        +'Mmax = '+str(Δijin)+' (Tidak OK)\n\n'
                        )               

        fc = IntVar()
        fy = IntVar()      

        B1 = tk.Label(border, text="Fc = ", font=("Arial", 10))
        B1.place(x=30, y=70)
        T1 = tk.Entry(border, width = 30, bd = 5,textvariable=fc)
        T1.place(x=150, y=70)

        B1 = tk.Label(border, text="Fy = ", font=("Arial", 10))
        B1.place(x=400, y=70)
        T2 = tk.Entry(border, width = 30, bd = 5,textvariable=fy)
        T2.place(x=520, y=70)


        B1 = tk.Button(border, text="Kapasitas Momen Tumpuan", font=("Arial", 10), command=tumpuan)
        B1.place(x=30, y=120)
        B2 = tk.Button(border, text="Kapasitas Momen Lapangan", font=("Arial", 10), command=lapangan)
        B2.place(x=280, y=120)
        B3 = tk.Button(border, text="Lendutan Maksimum yang terjadi", font=("Arial", 10), command=lendutan)
        B3.place(x=530, y=120)

        B2 = tk.Button(self, text="Back", bg = "dark orange", font=("Arial",15), command=lambda: controller.show_frame(FirstPage))
        B2.place(x=50, y=20)

        textbox = tk.Text(border, width = 90,height=18)
        textbox.place(x=20, y=170)

        ##################Menambahkan Scroll bar ##################tugas 



     
class balokb14(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        border = tk.LabelFrame(self, bg='ivory', bd = 10, font=("Arial", 20))
        border.pack(fill="both", expand="yes")
        
        L1 = tk.Label(border, text="GENTAR : BALOK B14", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=300, y=20)
        

        
        #### Perhitungan perumusan Ql dan Qd
        bebanmati = 125
        bebanhidup = 479
        Qd = bebanmati*8
        Ql = bebanhidup*8
        L = 24
        selimut = 40

        
        
        def tumpuan():
            #Momen ditumpuan 


            D = 25 #mm 
            b = 1000 #mm
            x = round(L/4,2) #mm
            tulangantumpuan = 24
            As = round(0.25*np.pi*D**2*tulangantumpuan,2)
            a = round(((As*fy.get())/(0.85*fc.get()*b)),2)
            d = round(800-selimut-D/2,2)

            q = round(1.2*Qd+1.6*Ql,2)
            Mntumpuan = round(((q*L/4)/2*(L-(L/4))),2)
            Mn = round(0.9*As*fy.get()*(d-0.5*a)/10/1000,2)


            textbox.insert(
                END,
                'KAPASITAS MOMEN TUMPUAN'
                )           

            textbox.insert(
                END,
                '\nUntuk momen terjadi di tumpuan yang berada di 1/4 L = '+str(x)+' m'
                )            
            
            textbox.insert(
                END,
                '\nMomen diTumpuan yang tejadi pada balok\nMmaxs = ((q x x)/2) x(L-x)\n'
                +'= ('+str(q)+' x '+str(x)+')/2 x ('+str(L)+'-'+ str(x)+') ='+ str(Mntumpuan)+' kg.m'
                )

            textbox.insert(
                END,
                '\nØMn = 0.9 x As x fy x(d - 0.5 a) \n=  0.9 x '+
                str(As)+" x "+str(fy.get())+' x ('+str(d)+' - 0.5 x '+str(a)+')'
                + ' = '+ str('{:0,.2f}'.format(Mn))+' kg.m\n'+'\nmaka : '
                )
            if Mn < Mntumpuan :
                    textbox.insert(
                        END,
                        'ØMn = '+str(Mn) 
                        + (' > ') #harus difungsikan 
                        +'Mmax = '+str(Mntumpuan)+' (OK)\n\n'
                        )
            else :
                    textbox.insert(
                        END,
                        'ØMn = '+str(Mn) 
                        + ('<') #harus difungsikan 
                        +'Mmax = '+str(Mntumpuan)+' (Tidak OK)\n\n'
                        )               

        def lapangan():
            #Momen ditumpuan 

            D = 25
            b = 1000
            tulanganlapangan = 22
            As = round(0.25*np.pi*D**2*tulanganlapangan,2)
            a = round((As*fy.get())/(0.85*fc.get()*b),2)
            d = round(800-selimut-D/2,2)

            q = round(1.2*Qd+1.6*Ql,2)
            Mnlapangan = round(1/8*q*L**2,2)
            Mn = round(0.9*As*fy.get()*(d-0.5*a)/10/1000,2) 



            textbox.insert(
                END,
                'KAPASITAS MOMEN LAPANGAN'
                )            

            textbox.insert(
                END,
                '\nMomen diLapangan yang tejadi pada balok\nMmaxs = 1/8 x q x L ^ 2\n'
                +'= 1/8 x '+str(q)+' x '+str(L**2)+' = '+ str(Mnlapangan)+' kg.m'
                )

            textbox.insert(
                END,
                '\nØMn = 0.9 x As x fy x(d - 0.5 a) \n=  0.9 x'+
                str(As)+" x "+str(fy.get())+' x ('+str(d)+' - 0.5 x '+str(a)+')'
                + ' = '+ str('{:0,.2f}'.format(Mn))+' kg.m\n'+'\nmaka : '
                )

            ####TUGAS DI FUNGSIKAN 
            if Mn < Mnlapangan :
                    textbox.insert(
                        END,
                        'ØMn = '+str(Mn) 
                        + (' > ') #harus difungsikan 
                        +'Mmax = '+str(Mnlapangan)+' (OK)\n\n'
                        )
            else :
                    textbox.insert(
                        END,
                        'ØMn = '+str(Mn) 
                        + ('<') #harus difungsikan 
                        +'Mmax = '+str(Mnlapangan)+' (Tidak OK)\n\n'
                        )                    

        
        
        def lendutan():
            #Momen diLendutan

            b = 1000
            h = 800
            Li = L*1000

            q = round((1.2*Qd+1.6*Ql)*10/1000,2)
            E = round(4700*np.sqrt(fc.get()),2)
            I = round(1/12*b*h**3,2)

            Δmaks = round((5*q*Li**4)/(384*E*I),2)

            Δijin = round(Li/240,2)

            textbox.insert(
                END,
                'KAPASITAS LENDUTAN'
                )           

            textbox.insert(
                END,
                '\nKombinasi pembebanan 1.2D + 1.6L (q)  =\n'
                +'= 1.2 x '+str(Qd)+'+ 1.6 x '+str(Ql)+' = '
                + str(q)+' N/mm'
                )
            textbox.insert(
                END,
                '\nE = 4700 x √fc \n'
                +'= 4700 x '+str(Qd)+' + 1.6 x √'+str(fc.get())+' = '
                + str(q)+' N/mm^2'
                )
            textbox.insert(
                END,
                '\nI = 1/12 x b x h^3 \n'
                +'= 1/12 x '+str(b)+' x '+str(h)+'^3 \n= '
                + str(q)+' mm^4'
                )
            
            textbox.insert(
                END,
                '\nΔ maks = (5 x q x L^4)/(384 x E x I) \n=  (5 x '+
                str(q)+" x "+str(Li)+'^4) /  (384 x '+str(E)+' x '+str(I)+')'
                + ' = '+ str(Δmaks)+' mm'
                )

            textbox.insert(
                END,
                '\nΔ ijin = L / 240 \n= '+
                str(L)+" / 240 "+ ' = '+ str('{:0,.2f}'.format(Δijin))+' mm\n'+'\nmaka : '
                )
            if Δmaks > Δijin :
                    textbox.insert(
                        END,
                        'Δ Maks = '+str(Δmaks) 
                        + (' > ') #harus difungsikan 
                        +'Mmax = '+str(Δijin)+' (OK)\n\n'
                        )
            else :
                    textbox.insert(
                        END,
                        'Δ Maks = '+str(Δmaks) 
                        + (' < ') #harus difungsikan 
                        +'Mmax = '+str(Δijin)+' (Tidak OK)\n\n'
                        )               

        fc = IntVar()
        fy = IntVar()      


        B1 = tk.Label(border, text="Fc = ", font=("Arial", 10))
        B1.place(x=30, y=70)
        T1 = tk.Entry(border, width = 30, bd = 5,textvariable=fc)
        T1.place(x=150, y=70)

        B1 = tk.Label(border, text="Fy = ", font=("Arial", 10))
        B1.place(x=400, y=70)
        T2 = tk.Entry(border, width = 30, bd = 5,textvariable=fy)
        T2.place(x=520, y=70)
               

        B1 = tk.Button(border, text="Kapasitas Momen Tumpuan", font=("Arial", 10), command=tumpuan)
        B1.place(x=30, y=120)
        B2 = tk.Button(border, text="Kapasitas Momen Lapangan", font=("Arial", 10), command=lapangan)
        B2.place(x=280, y=120)
        B3 = tk.Button(border, text="Lendutan Maksimum yang terjadi", font=("Arial", 10), command=lendutan)
        B3.place(x=530, y=120)

        B2 = tk.Button(self, text="Back", bg = "dark orange", font=("Arial",15), command=lambda: controller.show_frame(FirstPage))
        B2.place(x=50, y=20)

        textbox = tk.Text(border, width = 90,height=18)
        textbox.place(x=20, y=170)


        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #creating a window
        window = tk.Frame(self)
        
        window.pack()
        
        window.grid_rowconfigure(0, minsize = 500)
        window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}
        for F in (FirstPage, balokb10,balokb14):
            frame = F(window, self)
            self.frames[F] = frame

            frame.grid(row = 0, column=0, sticky="nsew")
             
        self.show_frame(FirstPage)
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("GENTAR")
            
app = Application()
app.maxsize(800,500)
app.mainloop()