import tkinter as tk
import tkinter.scrolledtext as tkst#import interface tkinter into the file to create GUI
from PIL import ImageTk 

import video_library as lib
import font_manager as fonts #import python files video_library and font_manager in the same folder to this file

def set_text(text_area, content): #create function set_text
    text_area.delete("1.0", tk.END) #delete the first existing content
    text_area.insert(1.0, content) #insert the existing content from the second variable


class CheckVideos(): #create a class for functions
    def __init__(self, window): #create a function to create a window
        window.geometry("750x350") #create a GUI window with 750 pixels wide and 350 pixels tall
        window.title("Check Videos") #create GUI title

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10) #create a button with a command value

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10) 

        self.input_txt = tk.Entry(window, width=3) #create a slot to insert the number in the list
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10) 

        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) #create a scrolng bar at one side of the list of videos

        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.filter= tk.Entry(window, width=24)
        self.filter.grid(column=3, row=1)

        filter_btn = tk.Button(window, text="Filter", command=self.filterlist)
        filter_btn.grid(column=3, row=2)

        self.list_videos_clicked()

    def check_video_clicked(self):#create a function for the command check_video
        key = self.input_txt.get() #set key as a variable for the function with self as value
        name = lib.get_name(key)
        if name is not None:
            image = lib.get_image(key)
            if image is not None:
                image_window = tk.Toplevel(None)
                image_window.title(name)
                image.thumbnail((400, 400))
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(image_window, image=photo)
                image_label.image = photo
                image_label.pack()
            director = lib.get_director(key) #calling out the function from the file video_library to input the variable
            rating = lib.get_rating(key) #calling out the function from the file video_library to input the variable
            play_count = lib.get_play_count(key) #calling out the function from the file video_library to input the variable
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}" 
            set_text(self.video_txt, video_details) #calling out the function set_text
        else:
            set_text(self.video_txt, f"Video {key} not found")
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):#create a function for the command list_videos to display the list of video
        video_list = lib.list_all() #collect all variables in the list
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

    def filterlist(self):
        filter_text = self.filter.get().lower()
        text = self.list_txt.get('1.0', tk.END)
        lines = text.split('\n')
        filter_lines = [line for line in lines if filter_text in line.lower()]
        self.list_txt.delete('1.0', tk.END)
        self.list_txt.insert('1.0', '\n'.join(filter_lines))
        

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
