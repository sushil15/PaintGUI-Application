from tkinter import *
from tkinter import ttk, colorchooser,filedialog
import PIL
from PIL import ImageGrab

class main:
    def __init__(self, master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.draw_widgets()
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset_screen)
        #self.labelfun()


    def paint(self, e):
        if self.old_x and self.old_y:
           self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg,
                               capstyle="round", smooth=True)
        self.old_x = e.x
        self.old_y = e.y

    def reset_screen(self, e):
        self.old_x = None
        self.old_y = None

    def change_penwidth(self, e):
        self.penwidth = e

    def save_file(self):
        file = filedialog.asksaveasfilename(filetypes=[('Portable Network Graphics', '*.png')])
        if file:
            x = self.master.winfo_rootx() + self.c.winfo_x()
            y = self.master.winfo_rooty() + self.c.winfo_y()
            x1 = x + self.c.winfo_width()
            y1 = y + self.c.winfo_height()

            PIL.ImageGrab.grab().crop((x, y, x1, y1)).save(file + '.png')

    def clear_screen(self):
        self.c.delete(ALL)

    def change_fgcolor(self):
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

    def change_bgcolor(self):
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def open_file(self):
        self.file1 = filedialog.askopenfile()
        self.file1.pack()

    #def mes_box(self):
       # self.Message("1.Draw with mouse\n2.choose option through menubar\n3.save file to your computer")

    def draw_widgets(self):
        self.controls = Frame(self.master, padx=5, pady=5,bg="deepskyblue")
        self.label=Label(self.controls, text='Pen Width: ', font=('courier', 15),bg='darkcyan',fg='darkmagenta').grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=5, to=100, command=self.change_penwidth, orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=30)
        self.controls.pack(fill=X)

        self.c = Canvas(self.master, width=500, height=400, bg=self.color_bg, )
        self.c.pack(fill=BOTH, expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='File..', menu=filemenu)
        filemenu.add_command(label='Save As..', command=self.save_file)

        colormenu = Menu(menu)
        menu.add_cascade(label='Colors', menu=colormenu)
        colormenu.add_command(label='Brush Color', command=self.change_fgcolor)
        colormenu.add_command(label='Background Color', command=self.change_bgcolor)

        optionmenu = Menu(menu)
        menu.add_cascade(label='Options', menu=optionmenu)

        optionmenu.add_command(label='Clear Canvas', command=self.clear_screen)
        optionmenu.add_command(label='Exit', command=self.master.destroy)

        filemenu1 = Menu(menu)
        menu.add_cascade(label='Help..', menu=filemenu1)
        filemenu1.add_command(label='help..')

    #def labelfun(self):
        #self.c = Label(self.master,text="Developer:Sushil Tanaji Varande", fg="yellow", bg='black',height=2)
        #self.c.pack(side=LEFT,fill=X ,padx=34)


if __name__ == '__main__':
   root = Tk()
   root.geometry("600x600+0+0")
   obj=main(root)
  # main(root)
   root.title('PaintGui Application')
   frame1= Frame(root)
   frame1.pack(side=BOTTOM)
   frame1.pack(side=RIGHT)
   label2=Label(frame1,text="created by sushil varande", font=('courier', 15) )
   label2.pack()

root.mainloop()