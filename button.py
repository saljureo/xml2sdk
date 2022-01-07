from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from xml2sdk import xml2sdk


def get_file():
  filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
  if not filename.endswith('.xml'):
     messagebox.showerror("Error", "Must select an XML file")
  else:
     file_to_convert.config(text=filename)
     run_button.config(state="normal")

def run_xml_to_sdk():
  filename = file_to_convert.cget("text")
  print("Running xml2Convert", filename)
  xml2sdk(filename)


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Select an .xml file to run xml2SDK: ").grid(column=0, row=0)
ttk.Button(frm, text="Open", command=get_file).grid(column=1, row=0)

file_to_convert = ttk.Label(frm, text="")
file_to_convert.grid(column=0, row=1)

run_button = ttk.Button(frm, text="Run xml2SDK", command=run_xml_to_sdk)
run_button.config(state="disabled")
run_button.grid(column=1, row=1)


root.mainloop()

#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

