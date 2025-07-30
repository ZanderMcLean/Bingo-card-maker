#Bingo card maker by Zander McLean!
#Started 18/07/2025

#Version 1

#Imports tkinter to allow the GUI to appear.
from tkinter import *
class Bingo:
    
    def __init__(self):
        #Gives window a name and defines the root
        self.root = Tk()
        self.root.title("Bingo Card maker!")
        #makes the frame everything visible will go in.
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0,sticky ="nsew")
        
        #A dictionary of the diferant frames that will be used in the program
        self.frames = {}
        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["To_NumFrame"] = self.create_to_numframe() 
        self.frames["To_WordFrame"] = self.create_to_wordframe()
        self.frames["To_PlayFrame"] = self.create_to_playframe()
        self.frames["To_ManFrame"] = self.create_to_manframe()
        
        self.show_frame("MainFrame")
        
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
        
        
        '''Creates a label that covers the background as the bg 
        can change colour.'''
        self.background = Label(frame, bg="#6C94C4")
        self.background.grid(sticky="nsew",columnspan=3, rowspan=5)
        
        '''Shows the title'''
        self.title = Label(frame, text="Bingo Card Maker!",bg ="#90BADE",
                           font = "Verdana 25 bold")
        self.title.grid(row=0, columnspan=3,ipady =5,
                        ipadx=10,pady=11,padx = 10, sticky="ew")        
        
        
        
        '''The button that sends the user to the number Bingo maker,
        or to_numframe as it's called'''
        self.to_num_button = Button(frame,text='''Number Bingo 
Creator''', bg ="#DFC759", font = "Verdana 12 bold",
                                          command=lambda: 
                                          self.show_frame("To_NumFrame"))
        self.to_num_button.grid(row=1, column=0,pady =6, padx=9)
        
        
        
        '''The button that sends the user to the word Bingo maker,
        or to_wordframe as it's called'''
        self.to_word_button = Button(frame,text='''Word Bingo 
Creator''', bg = "#DFC759", font = "Verdana 12 bold",
                                           command=lambda: 
                                           self.show_frame("To_WordFrame"))
        self.to_word_button.grid(row=1, column=2,pady =7, padx=9)
        
        
        '''The button to send users to the manual'''
        self.to_manuel_button = Button(frame,text="Manuel", bg ="#D8E7DC",
                                       font = "Verdana 12",
                                       command=lambda: 
                                       self.show_frame("To_ManFrame"))
        self.to_manuel_button.grid(row=2, column=0,pady =10, padx=12,
                                   stick="ws")
        '''The button to send users to the play bingo frame'''
        self.to_play_button = Button(frame,text="Play Bingo", bg ="#93C32F",
                                     font = "Verdana 17 bold",
                                     command=lambda: 
                                     self.show_frame("To_PlayFrame"))
        self.to_play_button.grid(row=2, column=1,pady =8, padx=0,
                                 sticky="nsew",ipady=3)         
        '''The button to end the program'''
        self.quit_button = Button(frame,text="Quit Program", bg ="#E16053",
                                  font = "Verdana 11", command= self.quit)
        self.quit_button.grid(row=3, column=1,pady =10, padx=0,
                              sticky="s",ipady=4)        
        
        '''Switchs colours between a light and dark pallet'''
        self.theme_button = Button(frame,text="Change theme",
                                   font = "Verdana 12",bg="#D8E7DC",
                                   command= self.set_colours)
        self.theme_button.grid(row=3, column=0,pady =10, padx=0,
                               sticky="s",ipady=4)
        return frame




    #Creates and sends user to the number Bingo maker.
    def create_to_numframe(self):
        frame = Frame(self.container) 
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.to_main_button = Button(frame,text="To title", bg ="light blue",
                                     font = "Verdana 12 bold", 
                                     command=lambda: 
                                     self.show_frame("MainFrame"))
        self.to_main_button.grid(row=1, column=1,pady =10, padx=10)
        
        self.quit_button = Button(frame,text="Quit Program", bg ="red",
                                  font = "Verdana 12 bold", command= self.quit)
        self.quit_button.grid(row=1, column=1,pady =100, padx=10)        
        return frame
  
    #Creates and sends user to the word Bingo maker.
    def create_to_wordframe(self):
        frame = Frame(self.container) 
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.to_main_button = Button(frame,text="To title", bg ="light blue",
                                     font = "Verdana 12 bold",
                                     command=lambda: 
                                     self.show_frame("MainFrame"))
        self.to_main_button.grid(row=1, column=0,pady =10, padx=10)

        self.quit_button = Button(frame,text="Quit Program", bg ="red",
                                  font = "Verdana 12 bold", command= self.quit)
        self.quit_button.grid(row=1, column=1,pady =100, padx=10)
        return frame
    
    #Creates and sends user to the Bingo player
    def create_to_playframe(self):
        frame = Frame(self.container) 
        frame.grid(row=0, column=0, sticky="nsew")
        return frame
    
    #Creates and sends user to the manual
    def create_to_manframe(self):
        frame = Frame(self.container) 
        frame.grid(row=0, column=0, sticky="nsew")
        self.to_main_button = Button(frame,text="To title", bg ="light blue",
                                     font = "Verdana 12 bold",
                                     command=lambda: 
                                     self.show_frame("MainFrame"))
        self.to_main_button.grid(row=1, column=0,pady =10, padx=10)        
        return frame
    
    #ends the program when run.
    def quit(self):
        self.root.destroy()
    
    #changes the colours when the change theme button is pressed
    def set_colours(self):
        if self.dark == False:
            '''If the change theme button is pressed and the theme isn't
            dark mode the colours are changed to dark mode 
            and dark is set to true.'''
            self.theme_button.configure(bg="#FFFFFF")
            self.background.configure(bg="#202547")
            self.title.configure(bg = "#0B7EAE")
            self.to_num_button.configure(bg = "#FFDE79")
            self.to_word_button.configure(bg = "#FFDE79")
            self.to_play_button.configure(bg = "#50B68B")
            self.to_manuel_button.configure(bg = "#FFFFFF")
            self.quit_button.configure(bg = "#E35151")
            self.dark = True
        else:
            '''If the frame is on dark mode it changes the colours to light mode
            and sets dark to false.'''
            self.theme_button.configure(bg="#D8E7DC")
            self.background.configure(bg = "#6C94C4") 
            self.title.configure(bg = "#90BADE")
            self.to_num_button.configure(bg = "#DFC759")
            self.to_word_button.configure(bg = "#DFC759")
            self.to_play_button.configure(bg = "#93C32F")
            self.to_manuel_button.configure(bg = "#D8E7DC")
            self.quit_button.configure(bg = "#E16053")
            self.dark = False
            
#Main code
#Makes everything start.
if __name__ == "__main__":
    app = Bingo()
    app.run()