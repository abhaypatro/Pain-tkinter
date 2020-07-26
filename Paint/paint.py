from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
import PIL
from PIL import Image,ImageDraw,ImageGrab,ImageTk

root=Tk()
root.title('Paint Program by Abhay Patro')
root.geometry("800x800")
brush_colour="black"
def paint(e):
	brush_width=int(myslider.get())
	
	brush_style=brush_type.get()
	x1=e.x-1
	y1=e.y-1
	x2=e.x+1
	y2=e.y+1
	mycanvas.create_line(x1,y1,x2,y2,fill=brush_colour,width=brush_width,capstyle=brush_style,smooth=True)

def change_brush_size(e):
	slider_val.config(text=int(myslider.get()))

def brush_color():
	global brush_colour
	brush_colour="black"
	brush_colour=colorchooser.askcolor(color=brush_colour)[1]

def canvas_color():
	global bg_color
	bg_color="white"
	bg_color=colorchooser.askcolor(color=bg_color)[1]
	mycanvas.config(bg=bg_color)

def screen_cleaner():
	mycanvas.delete(ALL)
	mycanvas.config(bg="white")

def image_saver():
	result=filedialog.asksaveasfilename(filetypes=(("png file", "*.png"),("All Files", "*.*") ))
	print(result)
	if result.endswith(".png"):
		pass
	else:
		result+=".png"
	print(result)
	if result:
		x=root.winfo_rootx() + mycanvas.winfo_x()

		y=root.winfo_rooty() + mycanvas.winfo_y()

		x1=x+mycanvas.winfo_width()

		y1=y+mycanvas.winfo_height()

		ImageGrab.grab().crop((x,y,x1,y1)).save(result)

		messagebox.showinfo("Image Saved","Your Image has been saved")

w=600
h=400

mycanvas=Canvas(root,width=w, height=h ,bg="white")
mycanvas.pack(pady=20)



mycanvas.bind('<B1-Motion>',paint)

#Frame for options

brush_options_frame=Frame(root)
brush_options_frame.pack(pady=20)

brush_size_frame=LabelFrame(brush_options_frame,text="Brush Size")
brush_size_frame.grid(row=0,column=0,padx=50)

myslider=ttk.Scale(brush_size_frame,from_=1,to=100,command=change_brush_size,value=10,orient=VERTICAL)
myslider.pack(padx=10,pady=10)

slider_val=Label(brush_size_frame,text=int(myslider.get()))
slider_val.pack(pady=5)

brush_type_frame=LabelFrame(brush_options_frame,text="Brush Type",height=4000)
brush_type_frame.grid(row=0,column=1,padx=50)

brush_type = StringVar()
brush_type.set("round")

radio1=ttk.Radiobutton(brush_type_frame,text="Round", variable=brush_type,value="round")
radio1.pack(padx=10,pady=10,anchor=W)
radio2=ttk.Radiobutton(brush_type_frame,text="Diamond", variable=brush_type,value="projecting")
radio2.pack(padx=10,pady=10,anchor=W)
radio3=ttk.Radiobutton(brush_type_frame,text="Slash", variable=brush_type,value="butt")
radio3.pack(padx=10,pady=10,anchor=W)

#Change Colors
change_color_frame=LabelFrame(brush_options_frame,text="Change Colors")
change_color_frame.grid(row=0,column=2,padx=50)

brush_color_button=ttk.Button(change_color_frame,text="Brush Color",command=brush_color)
canvas_color_button=ttk.Button(change_color_frame,text="Canvas Color",command=canvas_color)
brush_color_button.pack(padx=10,pady=10)
canvas_color_button.pack(padx=10,pady=10)

#Program options
options_frame=LabelFrame(brush_options_frame,text="Program Options")
options_frame.grid(row=0,column=3,padx=50)

clear_button=ttk.Button(options_frame,text="Clear Screen",command=screen_cleaner)
clear_button.pack(padx=10,pady=10)

save_button=ttk.Button(options_frame,text="Save Image",command=image_saver)
save_button.pack(padx=10,pady=10)
root.mainloop()