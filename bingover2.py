#Bingo card maker by Zander McLean!
#Started 30/07/2025

#Version 2

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
        self.frames["To_ManFrame"] = self.create_to_manframe()
        self.show_frame("To_ManFrame")
        
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
    def create_to_manframe(self):
        
        frame = Frame(self.container) 
        frame.grid(row=0, column=0, sticky="nsew")
        
        #The default text for the manual page. Will be replaced with json file.
        self.tuttitle = "Welcome to the Manual!"
        self.tutpara= '''To get started, click onone of the left-hand buttons
to help awnser any questions you may have!'''
        '''Creates a label that covers the background as the bg 
        can change colour.'''
        
        #sets the background colour.
        self.background = Label(frame, bg="#6C94C4")
        self.background.grid(sticky="nsew",columnspan=4, rowspan=13)
        
        #Button for returning to title screen.
        self.to_main_button = Button(frame,text="To title", bg ="#90BADE",
                                     font = "Verdana 10 bold",
                                     command=lambda: 
                                     self.show_frame("MainFrame"))
        self.to_main_button.grid(row=0, column=2,rowspan=2,pady =9, padx=0,
                              sticky="n",ipady=2)
        
        #Shows the title
        self.title = Label(frame, text= self.tuttitle,bg ="#90BADE",
                           font = "Verdana 20 bold")
        self.title.grid(row=1,column=1, columnspan=3,rowspan=3,ipady =5,
                        ipadx=10,padx = 10, sticky="ew")
        
        #Shows the information paragraph.
        self.para = Label(frame, text= self.tutpara,bg ="#90BADE",
                           font = "Verdana 11")
        self.para.grid(row=3,column=1, columnspan=3,rowspan=9,ipady =5,
                        ipadx=5,padx = 10,pady = (25,0), sticky="n")          
        
        '''Switchs colours between a light and dark pallet'''
        self.theme_button = Button(frame,text="Change theme",
                                   font = "Verdana 10 bold",bg="#D8E7DC",
                                   command= self.set_colours)
        self.theme_button.grid(row=0, column=1,pady =9,rowspan=2, padx=0,
                              sticky="n",ipady=2)
        
        '''The button to end the program'''
        self.quit_button = Button(frame,text="Quit Program", bg ="#E16053",
                                  font = "Verdana 10 bold", command= self.quit)
        self.quit_button.grid(row=0, column=3,rowspan=2,pady =9, padx=0,
                              sticky="n",ipady=2)   


        self.wordq_button = Button(frame,text='What does "Word Bingo" mean?', bg ="#D8E7DC",
                                  font = "Verdana 11", command=lambda: self.draw_json(0))
        self.wordq_button.grid(row=0, column=0,sticky="wne")
        
        
        self.numq_button = Button(frame,text='What does "Number Bingo" mean?', bg ="#90BADE",
                                  font = "Verdana 11", command=lambda: self.draw_json(1))
        self.numq_button.grid(row=1, column=0,sticky="wne")
        
        
        self.modeq_button = Button(frame,text='What does "Bingo Mode" mean?', bg ="#D8E7DC",
                                  font = "Verdana 11", command=lambda: self.draw_json(2))
        self.modeq_button.grid(row=2, column=0,sticky="wne")
        
        
        self.saveq_button = Button(frame,text="How do I save my Bingo Cards?", bg ="#90BADE",
                                  font = "Verdana 11", command=lambda: self.draw_json(3))
        self.saveq_button.grid(row=3, column=0,sticky="wne")   
        
        
        self.titleq_button = Button(frame,text="How do I return to the Title?", bg ="#D8E7DC",
                                  font = "Verdana 11", command=lambda: self.draw_json(4))
        self.titleq_button.grid(row=4, column=0,sticky="wne")
        
                
        self.freeq_button = Button(frame,text='What does "Free Space" mean?', bg ="#90BADE",
                                  font = "Verdana 11", command=lambda: self.draw_json(5))
        self.freeq_button.grid(row=5, column=0,sticky="wne")
            
        
        self.genq_button = Button(frame,text='What does "Generate" do?', bg ="#D8E7DC",
                                  font = "Verdana 11", command=lambda: self.draw_json(6))
        self.genq_button.grid(row=6, column=0,sticky="wne")          
        
        
        self.h_wq_button = Button(frame,text='What does "Change Height/Width" do?', bg ="#90BADE",
                                  font = "Verdana 11", command=lambda: self.draw_json(7))
        self.h_wq_button.grid(row=7, column=0,sticky="wne")          
        
        
        self.max_minq_button = Button(frame,text='What does "Max/Min Number" do?', bg ="#D8E7DC",
                                  font = "Verdana 11", command=lambda: self.draw_json(8))
        self.max_minq_button.grid(row=8, column=0,sticky="wne")          
        
        
        self.listq_button = Button(frame,text='What is a "List?"', bg ="#90BADE",
                                  font = "Verdana 11", command=lambda: self.draw_json(9))
        self.listq_button.grid(row=9, column=0,sticky="wne")          
        
        
        self.editq_button = Button(frame,text="How do I edit my lists?", bg ="#D8E7DC",
                                  font = "Verdana 11", command=lambda: self.draw_json(10))
        self.editq_button.grid(row=10, column=0,sticky="wne")          
        
        
        self.playq_button = Button(frame,text="How do I play Bingo?", bg ="#90BADE",
                                  font = "Verdana 11", command=lambda: self.draw_json(11))
        self.playq_button.grid(row=11, column=0,sticky="wne")          
        
        
        self.blackoutq_button = Button(frame,text='What is "Blackout Bingo?"', bg ="#D8E7DC",
                                  font = "Verdana 11", command=lambda: self.draw_json(12))
        self.blackoutq_button.grid(row=12, column=0,sticky="wne")          
        
        return frame
    
    
    
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