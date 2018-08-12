# import tkMessageBox
# import ttk
#
# import MySQLdb
# from Tkinter import *
#
#
# def show_table():
#     # rows = []
#     for widget in bFrame.winfo_children():
#         widget.destroy()
#     bFrame.pack(side=BOTTOM)
#     i = 0
#     j = 0
#     try:
#         for p in range(len(cur.description)):
#             e = Label(bFrame, relief=GROOVE, text=cur.description[p][0])
#             e.grid(row=i, column=j, sticky=NSEW)
#             j = j + 1
#         i = 1
#     except Exception, e:
#         print "no col name"
#     for data_row in cur.fetchall():
#         # cols = []
#         j = 0
#         for data_col in data_row:
#             # e = Entry(bFrame, relief=RIDGE, yscrollcommand=scrollbar.set)
#             e = Label(bFrame, relief=GROOVE, text=data_col)
#             e.grid(row=i, column=j, sticky=NSEW)
#             # e.insert(END, data_col)
#             # cols.append(e)
#             j += 1
#         # rows.append(cols)
#         i += 1
#
#
# def okOnClick():
#     print(queryEntry.get())
#     try:
#         cur.execute(queryEntry.get())
#         show_table()
#     except Exception, e:
#         print repr(e)
#         tkMessageBox.showinfo("Error!!??\n wat???", "Something's wrong!")
#
#
# def gui_setup():
#     global bFrame, scrollbar, window
#     window = Tk()
#
#     bFrame = Frame(window)
#     uFrame = Frame(window)
#     # bFrame.pack(side = BOTTOM)
#     uFrame.pack(side=TOP)
#
#     # scrollbar = Scrollbar(bFrame)
#     # scrollbar.pack(side=RIGHT, fill=Y)
#
#     window.title("Health Care System")
#     # window.geometry('{}x{}'.format(500, 200))
#
#     queryLabel = Label(uFrame, text="Enter Query: ")
#     queryLabel.pack()
#
#     global queryEntry
#     queryEntry = Entry(uFrame, width=100)
#     queryEntry.insert(END, "select * from drug")
#     queryEntry.pack(side=LEFT)
#
#     okButton = Button(uFrame, text="OK", command=okOnClick)
#     okButton.pack(side=RIGHT)
#
#     # resultLabel = Label(uFrame, text="Result: ")
#     # resultLabel.pack()
#
#
#
#
#     window.mainloop()
#
#
# db = MySQLdb.connect(host="localhost",  # your host, usually localhost
#                      user="root",  # your username
#                      passwd="95649",  # your password
#                      db="chcs")  # name of the data base
#
# # you must create a Cursor object. It will let
# #  you execute all the queries you need
# cur = db.cursor()
#
# # Use all the SQL you like
# # cur.execute("SELECT * FROM Patient;")
#
# # print all the first cell of all the rows
# # for row in cur.fetchall():
# #     print row
# gui_setup()
#
#
# # db.close()
