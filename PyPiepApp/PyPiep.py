"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van GUI
Creatie d.d. 15 maart 2019
"""
from tkinter import filedialog, Scrollbar, Y, END, StringVar, RIGHT, LEFT, RIDGE, TOP,X,Y,Frame,Label,Entry,Button
import tkinter
import mysql.connector

hostname="hannl-hlo-bioinformatica-mysqlsrv.mysql.database.azure.com"
dummyuser = "@hannl-hlo-bioinformatica-mysqlsrv"


class PyPiepGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title("PyPiep Release Candidate")
        self.frame0 = tkinter.Frame(self.main_window,height=100)
        self.frame0.pack()

        self.frame1 = tkinter.Frame(self.main_window, height=100,bg="green")
        self.frame1.pack()
        self.frame2 = tkinter.Frame(self.main_window, height=500,width=500)
        self.frame2.pack()
        self.user_var = StringVar()
        self.passw_var = StringVar()
        self.ulabel = tkinter.Label(self.frame0,text="Username")
        self.ulabel.pack(padx=5, pady=10, side=LEFT)
        self.user = tkinter.Entry(self.frame0,textvariable=self.user_var)
        self.user.pack(padx=5, pady=10, side=LEFT)
        self.plabel = tkinter.Label(self.frame0,text="Password")
        self.plabel.pack(padx=5, pady=10, side=LEFT)

        self.passw = tkinter.Entry(self.frame0, textvariable=self.passw_var,show="*")
        self.passw.pack(padx=5, pady=10, side=LEFT)

        self.my_button = tkinter.Button(self.frame1, text='Ververs',
                                        fg = "#c0c0c0", bg = "green",
                                        command=self.lees_berichten)
        self.label = tkinter.Label(self.frame1,text="Filter:")
        self.label.pack(padx=5, pady=10, side=LEFT)
        self.my_button.pack(padx=5, pady=10, side=RIGHT)
        self.filter_var = StringVar()
        self.filter = tkinter.Entry(self.frame1, textvariable=self.filter_var)
        self.filter.pack(padx=5, pady=10, side=LEFT)

        self.scrollbar = Scrollbar(self.frame2)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text = tkinter.Text(self.frame2, height=20, width=60,
                                 bg="white",
                                 yscrollcommand = self.scrollbar.set)
        self.text.pack()
        self.scrollbar.config(command=self.text.yview)

        tkinter.mainloop()



    def lees_berichten(self):
        self.text.tag_config("naam", background="darkgray", foreground="blue", font=('Arial', 14, 'bold'))
        self.text.tag_config("head", background="darkgray", foreground="black",font=('Arial', 12, 'italic'))
        self.text.tag_config("bericht", background="lightgray", foreground="black", font=('Arial', 12))
        query = "select voornaam, " \
                " bericht, " \
                " if(datum!=curdate(),datum,'vandaag ') datum," \
                " if(datum!=curdate(),tijd, concat(convert(timediff(curtime(),tijd), char),' geleden')) tijd," \
                " timestamp(datum,tijd) datumtijd" \
                " from student " \
                " natural join piep " \
                " where bericht like '%{}%'" \
                " order by datumtijd desc" \
                " limit 100 ".format(self.filter_var.get())

        conn = mysql.connector.connect(host=hostname,
                                       user=self.user_var.get()+"@"+hostname,
                                       passwd=self.passw_var.get())
        cursor = conn.cursor()
        cursor.execute("use dummy")
        cursor.execute(query)
        self.text.delete(1.0,END)
        for bericht in cursor:
            self.text.insert(END,bericht[0]+' ','naam')
            self.text.insert(END,str(bericht[2])+' '+bericht[3]+'\n','head')
            self.text.insert(END, bericht[1]+'\n','bericht')
        cursor.close()
        conn.close()


my_gui = PyPiepGUI()



