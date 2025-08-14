#Bingo card maker by Zander McLean!
#Started 12/08/2025

#Version 3

#Imports tkinter to allow the GUI to appear.
from tkinter import *
import json
class Bingo:
    
    def __init__(self):
        #Gives window a name and defines the root
        self.root = Tk()
        self.root.title("Bingo Card maker!")
        self.root.resizable(0,0)
        #makes the frame everything visible will go in.
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0,sticky ="nsew")
        
        #A dictionary of the diferant frames that will be used in the program
        self.frames = {}
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["To_NumFrame"] = self.create_to_numframe()
        self.show_frame("To_NumFrame")
        
        #Sets dark mode to false.
        self.dark = False
                        
    #Runs the Gui
    def run(self):
        self.root.mainloop()
          
    #Makes the currently shown frame what name is and raises it to the front.    
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
        
    #Creates the main/ selection window.
    def create_main_frame(self):     
        '''Makes the frame everything is kept in appear'''
        frame = Frame(self.container)
        frame.grid(row=0, column=0, sticky="nsew")
        return frame


    #Creates and sends user to the manual
    def create_to_numframe(self):
                 
        
        frame = Frame(self.container) 
        frame.grid(row=0, column=0, sticky="nsew")
        
        
        #sets the background colour.
        self.background = Label(frame, bg="#6C94C4")
        self.background.grid(sticky="nsew",columnspan=4, rowspan=13)
        
        #Button for returning to title screen.
        self.to_main_button = Button(frame,text="To Title", bg ="#90BADE",
                                     font = "Verdana 10 bold",
                                     command=lambda: 
                                     self.show_frame("MainFrame"))
        self.to_main_button.grid(row=0, column=2,rowspan=2,pady =9, ipadx=17,
                              sticky="n",ipady=2)
        
        
        self.clearnum_button = Button(frame,text="Clear Board", bg ="#D8E7DC",
                                  font = "Verdana 10 bold", command=lambda: self.draw_json(12))
        self.clearnum_button.grid(row=0, column=1, rowspan=2,pady =9, padx=0,
                              sticky="n",ipady=2)          
        
        
        #Shows the title
        self.title = Label(frame, text= "Create A Number Bingo Card!",bg ="#90BADE",
                           font = "Verdana 20 bold")
        self.title.grid(row=2,column=0, columnspan=4,rowspan=3,ipady =5,
                        ipadx=10,padx = 10, sticky="ews", pady = 20)
                
        
        '''Switchs colours between a light and dark pallet'''
        self.theme_button = Button(frame,text="Change Theme",
                                   font = "Verdana 10 bold",bg="#D8E7DC",
                                   command= self.set_colours)
        self.theme_button.grid(row=0, column=0, rowspan=2,pady =9, padx=0,
                              sticky="n",ipady=2)
        
        '''The button to end the program'''
        self.quit_button = Button(frame,text="Quit Program", bg ="#E16053",
                                  font = "Verdana 10 bold", command= self.quit)
        self.quit_button.grid(row=0, column=3,rowspan=2,pady =9, padx=0,
                              sticky="n",ipady=2)
        
        
        
        
        
        self.boardh_button =  Label(frame,text="Board Height", bg ="#D8E7DC",
                                  font = "Verdana 11")
        self.boardh_button.grid(row=5, column=0,sticky="nsew")
        
        self.boardh_scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, bg ="#D8E7DC",
                                  font = "Verdana 10")
        self.boardh_scale.grid(row=5, column=1,sticky="")        
        
        
        
        self.boardw_label =  Label(frame,text="Board Width", bg ="#D8E7DC",
                                  font = "Verdana 11")
        self.boardw_label.grid(row=5, column=2,sticky="nsew")                
        
        self.boardw_scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, bg ="#D8E7DC",
                                  font = "Verdana 10")
        self.boardw_scale.grid(row=5, column=3,sticky="") 
        
        
        
        self.minnum_label = Label(frame,text="Min Number", bg ="#D8E7DC",
                                  font = "Verdana 11")
        self.minnum_label.grid(row=6, column=0,sticky="nsew")  
        
        self.minnum_scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, bg ="#D8E7DC",
                                  font = "Verdana 10")
        self.minnum_scale.grid(row=6, column=1,sticky="") 
        
        
        self.maxnum_label = Label(frame,text="Max Number", bg ="#D8E7DC",
                                  font = "Verdana 11")
        self.maxnum_label.grid(row=6, column=2,sticky="nsew")        
        
        self.maxnum_scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL, bg ="#D8E7DC",
                                  font = "Verdana 10")
        self.maxnum_scale.grid(row=6, column=3,sticky="") 
        
   
        self.freespace_label = Label(frame,text="Include Free Space", bg ="#D8E7DC",
                                  font = "Verdana 11")
        self.freespace_label.grid(row=7, column=2,sticky="nsw", pady = 10, padx = 5, columnspan = 2,ipadx = 14)  
        
        self.freespace_check = IntVar()
        self.freespace_checkbox = Checkbutton(frame, variable=self.freespace_check,bg ="#D8E7DC")
        self.freespace_checkbox.grid(row=7, column=3,sticky="nse", pady = 10, padx = 15, ipadx = 3)        
        
        
        self.gennum_button = Button(frame,text="Generate Board", bg ="#D8E7DC",
                                  font = "Verdana 11", command=lambda: self.draw_json(12))
        self.gennum_button.grid(row=7, column=0,sticky="ew", pady = 10, padx = 5)  
        
        
        self.savenum_button = Button(frame,text="Save Board", bg ="#D8E7DC",
                                  font = "Verdana 11", command=lambda: self.draw_json(12))
        self.savenum_button.grid(row=7, column=1,sticky="ew", pady = 10, padx = 5) 
        
        
        
        
        
        
        
       
        return frame
    
    
    #Draws information from the json file to display the tutorials.
    def draw_json(self, bid):
        with open("tutorials.json") as f:
            tutorials = json.load(f)
            for key in tutorials[f"{bid}"]:
                self.title.configure(text = key)
            for value in tutorials[f"{bid}"].values():
                self.para.configure(text = value)
        
        return 
    
    
    
    
    
    
    
    
    
    
    #ends the program when run.
    def quit(self):
        self.root.destroy()
    
    #changes the colours when the change theme button is pressed
    #This will be changed out for a json file in the future.
    def set_colours(self):
        if self.dark == False:
            '''If the change theme button is pressed and the theme isn't
            dark mode the colours are changed to dark mode 
            and dark is set to true.'''
            self.wordq_button.configure(bg = "#CD6180")
            self.numq_button.configure(bg = "#FFDE79")
            self.modeq_button.configure(bg = "#CD6180")
            self.saveq_button.configure(bg = "#FFDE79")
            self.titleq_button.configure(bg = "#CD6180")
            self.freeq_button.configure(bg = "#FFDE79")
            self.genq_button.configure(bg = "#CD6180")
            self.h_wq_button.configure(bg = "#FFDE79")
            self.max_minq_button.configure(bg = "#CD6180")
            self.listq_button.configure(bg = "#FFDE79")
            self.editq_button.configure(bg = "#CD6180")
            self.playq_button.configure(bg = "#FFDE79")
            self.blackoutq_button.configure(bg = "#CD6180")
            
            self.to_main_button.configure(bg = "#0B7EAE")
            self.para.configure(bg = "#0B7EAE")
            self.theme_button.configure(bg="#CD6180")
            self.background.configure(bg="#202547")
            self.title.configure(bg = "#0B7EAE")
            self.quit_button.configure(bg = "#E35151")
            self.dark = True
        else:
            '''If the frame is on dark mode it changes the colours to light mode
            and sets dark to false.'''
            self.to_main_button.configure(bg = "#90BADE")
            self.para.configure(bg = "#90BADE")
            self.theme_button.configure(bg="#D8E7DC")
            self.background.configure(bg = "#6C94C4") 
            self.title.configure(bg = "#90BADE")
            self.quit_button.configure(bg = "#E16053")
            
            self.wordq_button.configure(bg = "#D8E7DC")
            self.numq_button.configure(bg = "#90BADE")
            self.modeq_button.configure(bg = "#D8E7DC")
            self.saveq_button.configure(bg = "#90BADE")
            self.titleq_button.configure(bg = "#D8E7DC")
            self.freeq_button.configure(bg = "#90BADE")
            self.genq_button.configure(bg = "#D8E7DC")
            self.h_wq_button.configure(bg = "#90BADE")
            self.max_minq_button.configure(bg = "#D8E7DC")
            self.listq_button.configure(bg = "#90BADE")
            self.editq_button.configure(bg = "#D8E7DC")
            self.playq_button.configure(bg = "#90BADE")
            self.blackoutq_button.configure(bg = "#D8E7DC")
            self.dark = False
            
#Main code
#Makes everything start.
if __name__ == "__main__":
    app = Bingo()
    app.run()