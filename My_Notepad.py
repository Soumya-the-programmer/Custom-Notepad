from tkinter import *# importing tkinter module to create a GUI window
from tkinter import filedialog# importing filedialog to handle files from file explorer
from tkinter import messagebox as tmsg# importing messagebox to show messages to user
#MAIN WINDOW
root=Tk()# creating Tk() class instance
root.title("My Notepad")# title
root.iconbitmap("C:\\tkinter_python\\notepad_logo.ico")# icon
root.geometry("1400x900")# geometry size declaring
root.minsize(1400,900)# fixing minimum size

#File Menu Functions
#Save Function
def SAVE():
    #to get the written texts from the text box widget
    content=textbox.get("1.0",END)
    #asksaveasfilename() helps to get the file name as we use it instead of asksaveasfile()
    saved_loc=filedialog.asksaveasfilename(defaultextension="*.txt",#to specify the file extension
                            filetypes=[("Text files", "*.txt"),("C files","*.c"),("Python files","*.py"),
                                       ("Java files","*.java"),("Java Script files","*.js"),("All files", "*.*")],#to mention file type options
                            initialdir="C:\\My Notepad files",#to mention directory
                            initialfile="my_notepad.txt",#initial by default name will be that
                            title="Save"#for title
                            )
    try:
        #to write the contents that are written in text to that corresponding saved file
        with open(f"{saved_loc}","w") as f:
            f.write(content)#writing the contents to the file
    # handling the exception here
    except Exception:
        pass
#Save As Function
def SAVEAS():
    #to get the written texts from the text box widget
    content=textbox.get("1.0",END)
    #asksaveasfilename() helps to get the file name as we use it instead of asksaveasfile()
    file_name=filedialog.asksaveasfilename(defaultextension="*.txt",#to specify the file extension
                            filetypes=[("Text files", "*.txt"),("C files","*.c"),("Python files","*.py"),
                                       ("Java files","*.java"),("Java Script files","*.js"),("All files", "*.*")],#to mention file type options
                            initialdir="/",#to mention directory
                            initialfile="my_notepad.txt",#initial by default name will be that
                            title="Save As"#for title
                            )
    try:
        #to write the contents that are written in text to that corresponding saved file
        with open(f"{file_name}","w") as f:
            f.write(content)#writing the contents to the file
    # handling the exception here
    except Exception:
        pass
#Close Function
def CLOSE():
    root.quit()#quits from the window
    root.destroy()#destroys the window

#Font Menu Functions
#fonts function
def FONT(font_name):
    #using try-except statements to catch exception like if no text is selected
    try:
        #current_tags variable stores the current tag that are in the text
        current_tags = textbox.tag_names("sel.first")#stores tags as a tuple()
        if len(current_tags)==2:
            font_sz=int(current_tags[1])
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_name, "sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_name, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_name, font=(font_name, font_sz))#configuring the font tag here
        elif len(current_tags)==3:
            font_sz=int(current_tags[2])
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_name, "sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_name, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_name, font=(font_name, font_sz))#configuring the font tag here
        elif len(current_tags)==4:
            font_sz=int(current_tags[3])
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_name, "sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_name, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_name, font=(font_name, font_sz))#configuring the font tag here
        elif len(current_tags)==5:
            font_sz=int(current_tags[4])
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_name, "sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_name, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_name, font=(font_name, font_sz))#configuring the font tag here
        elif len(current_tags)==6:
            font_sz=int(current_tags[5])
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_name, "sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_name, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_name, font=(font_name, font_sz))#configuring the font tag here
        else:
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_name, "sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_name, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_name, font=(font_name, 14))#configuring the font tag here
    except Exception:
        pass  # No text is selected
    
#fontsize function
def FONTSIZE(font_size):
    #converting the font size into integer.
    font_size=int(font_size)
    #using try-except statements to catch exception like if no text is selected
    try:
        #current_tags variable stores the current tag that are in the text
        current_tags = textbox.tag_names("sel.first")#stores tags as a tuple()
        #checking the length of current_tags
        if len(current_tags)==2:
            font_sty=current_tags[1]
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_size,"sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_size, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_size, font=(font_sty,font_size))#configuring the font tag here
        elif len(current_tags)==3:
            font_sty=current_tags[2]
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_size,"sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_size, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_size, font=(font_sty,font_size))#configuring the font tag here
        elif len(current_tags)==4:
            font_sty=current_tags[3]
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_size,"sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_size, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_size, font=(font_sty,font_size))#configuring the font tag here
        elif len(current_tags)==5:
            font_sty=current_tags[4]
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_size,"sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_size, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_size, font=(font_sty,font_size))#configuring the font tag here
        elif len(current_tags)==6:
            font_sty=current_tags[5]
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_size,"sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_size, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_size, font=(font_sty,font_size))#configuring the font tag here
        else:
            #checking if selected font tag is present in the text or not
            if font_name in current_tags:
                textbox.tag_remove(font_size,"sel.first", "sel.last")#removing the selected font tag if already present
            #if selected font tag is not present then adding the selected font tag
            else:
                textbox.tag_add(font_size, "sel.first", "sel.last")#adding the font tag to the selected text
                textbox.tag_configure(font_size, font=("Times of roman",font_size))#configuring the font tag here
    except Exception:
        pass  # No text is selected
    
# bold function
def BOLD():
    #using try-except statements to catch exception like if no text is selected
    try:
        #current_tags variable stores the current tag that are in the text
        current_tags = textbox.tag_names("sel.first")#stores tags as a tuple()
        #checking if bold tag is present in the text or not
        if "bold" in current_tags:
            textbox.tag_remove("bold", "sel.first", "sel.last")#removing the bold tag if already present
        #if bold tag is not present then adding the bold tag
        else:
            textbox.tag_add("bold", "sel.first", "sel.last")#adding the bold tag to the selected text
            textbox.tag_configure("bold", font=("Arial", 14, "bold"))#configuring the bold tag here
    except Exception:
        pass  # No text is selected
    
#italic function
def ITALIC():
    #using try-except statements to catch exception like if no text is selected
    try:
        #current_tags variable stores the current tag that are in the text
        current_tags = textbox.tag_names("sel.first")
        #checking if italic tag is present in the text or not
        if "italic" in current_tags:
            textbox.tag_remove("italic", "sel.first", "sel.last")#removing the italic tag if already present
        #if italic tag is not present then adding the italic tag
        else:
            textbox.tag_add("italic", "sel.first", "sel.last")#adding the italic tag to the selected text
            textbox.tag_configure("italic", font=("Arial", 14, "italic"))#configuring the italic tag here
    except Exception:
        pass  # No text is selected

#underline function
def UNDERLINE_():
    #current_tags variable stores the current tag that are in the tex
    try:
        current_tags = textbox.tag_names("sel.first")
        #checking if underline tag is present in the text or not
        if "underline" in current_tags:
            textbox.tag_remove("underline", "sel.first", "sel.last")#removing the underline tag if already present
        #if underline tag is not present then adding the underline tag
        else:
            textbox.tag_add("underline", "sel.first", "sel.last")#adding the underline tag to the selected text
            textbox.tag_configure("underline", underline=True)#configuring the underline tag here
    except Exception:
        pass  # No text is selected

#Help Menu options
#Rate menu
def RATE():
    rate_window=Toplevel(root)# copying the Tk() class instance from root
    rate_window.title("Rate Us")# title
    rate_window.iconbitmap("C:\\tkinter_python\\notepad_logo.ico")# heading
    rate_window.geometry("300x275")# geometry size
    rate_window.maxsize(300,275)# maxsize
    rate_window.minsize(300,275)# minsize
    uframe=Frame(rate_window,bg="seagreen1",pady=20,borderwidth=4,relief="groove")# frame 1
    uframe.pack(fill=X)
    title=Label(uframe,text="Rate us here please",font=("poppins",15,"bold"),bg="white",fg="black")# heading
    title.pack()
    lframe=Frame(rate_window,bg="aquamarine2",pady=20,borderwidth=4,relief="groove")# frame 2
    lframe.pack(fill=X)
    # Scale for rating
    rate_scale=Scale(lframe,from_=0, to=100, orient="horizontal",sliderlength=5,sliderrelief="sunken",tickinterval=50,bg="aquamarine2",borderwidth=2,relief="solid",font=("poppins",10,"bold"))
    rate_scale.set(50)# setting the scale at 50
    rate_scale.pack()
    f_label=Label(lframe,text="\n",bg='aquamarine2')# show label to create free space
    f_label.pack()
    # submit button
    s_button=Button(lframe,text="Submit",borderwidth=2,relief="solid",font=("poppins",10,"bold"),padx=10,pady=10,bg="brown1",fg="white",command=rmessage)
    s_button.pack()
    rate_window.mainloop()# mainloop() to show the GUI window in screen
#message window after rating
def rmessage():
    # showing this message
    tmsg.showinfo("Thank You!","Thank You! for your rating :)")
#About us menu
def ABOUT():
    # showing this message
    tmsg.showinfo("About Us","This  CUSTOM NOTEPAD is made by Soumyajeet Das.\nIt is created using tkinter module in Python.\nDate: 21/07/2024")
#File Menu
file_menu=Menu(root)# file menu
#Inside File Menu
fin_menu=Menu(file_menu,tearoff=0)# sub menu of file menu
# file menu options
fin_menu.add_command(label="Save",command=SAVE)
fin_menu.add_command(label="Save As    ",command=SAVEAS)
fin_menu.add_separator()#to separate
fin_menu.add_command(label="Close",command=CLOSE)
#config sub file menu to change the font 
fin_menu.config(font=("Helvetica",12))#Inside file menu font and font size will be changed
file_menu.add_cascade(label="   File   ",menu=fin_menu)# add_cascade the sub file menu here
root.configure(menu=file_menu)# #configuring File Menu

#Font Menu
font_menu=Menu(root)
#Inside font Menu
in_font_menu=Menu(file_menu,tearoff=0)
#submenu of inside font menu
fonts=Menu(in_font_menu,tearoff=0)
# List of fonts for checkbuttons
font_list = [
    "Calibri",
    "Times of Roman",
    "Poppins",
    "Algerian",
    "Arial",
    "Arial Black",
    "Castellar",
    "Cinzel Black",
    "Bernard MT Condensed",
    "Bookman Old Style"
]
# Create checkbuttons for each font using lambdas and partial
for font_name in font_list:
    fonts.add_radiobutton(label=font_name, command=lambda f=font_name: FONT(f))
in_font_menu.add_cascade(label="Fonts",menu=fonts)#add_cascade() to adding the fonts menu into the submenu of font
#config the sub font menu to change font size
in_font_menu.config(font=("Helvetica",12))#changing font of sub font menu to increase the menu size

font_size=Menu(in_font_menu,tearoff=0)
# List of fonts for checkbuttons
font_size_list = ['8','9','10','11','12','14','16','18','20','22','24','26','28','36','48','72']
# Create checkbuttons for each font using lambdas and partial
for font_sizes in font_size_list:
    font_size.add_radiobutton(label=font_sizes, command=lambda f=font_sizes: FONTSIZE(f))
in_font_menu.add_cascade(label="Font Size",menu=font_size)#add_cascade() to adding the fonts menu into the submenu of font
#config the sub font menu to change font size
in_font_menu.config(font=("Helvetica",12))#changing font of sub font menu to increase size
file_menu.add_cascade(label="   Font   ",menu=in_font_menu)
#configuring Font Menu
root.configure(menu=file_menu)
#BOLD menu
bold=Menu(root)
file_menu.add_cascade(label="   Bold   ",command=BOLD)
root.configure(menu=file_menu)
#ITALIC menu
italic=Menu(root)
file_menu.add_cascade(label="   Italic   ",command=ITALIC)
root.configure(menu=file_menu)
#UNDERLINE menu
underline=Menu(root)
file_menu.add_cascade(label="   Underline   ",command=UNDERLINE_)
root.configure(menu=file_menu)
#HELP Menu
help_menu=Menu(root)
#Inside help Menu
in_help_menu=Menu(file_menu,tearoff=0)
in_help_menu.add_command(label="Rate Us",command=RATE)
in_help_menu.add_separator()
in_help_menu.add_command(label="About Us    ",command=ABOUT)
#config the sub help menu to change font size
in_help_menu.config(font=("Helvetica",12))#changing font of sub help menu to increase the menu size
#configuring help Menu
file_menu.add_cascade(label="   Help   ",menu=in_help_menu)
root.configure(menu=file_menu)
#scrollbar to scroll in text box
scbar=Scrollbar(root,width=25)
scbar.pack(side="right",anchor="ne",fill=Y)
#text widget to write text
textbox=Text(root,height=1000,width=1000,font=("Times of roman",14),yscrollcommand=scbar.set)
textbox.pack()
#configuring the scrollbar in textbox yview
scbar.config(command=textbox.yview)

root.mainloop()# mainloop() to show the GUI window in screen