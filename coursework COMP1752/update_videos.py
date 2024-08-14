import tkinter as tk

import video_library as lib


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateVideos:
    def __init__(self,window):
        window.title("Update Videos")
        self.num_rate = tk.IntVar()

        display_btn = tk.Button(window, text="display Video", command=self.display)
        display_btn.grid(column=1, row=0, padx=10, pady=10)

        update_btn = tk.Button(window, text="Update", command=self.update)
        update_btn.grid(column=2, row=0, padx=10, pady=10)

        self.input_ID = tk.Entry(window, width=3)
        self.input_ID.grid(column=0, row=0, padx=10, pady=10)
        
        input_rating_btns = []
        for i in range(5):
            input_rating = tk.Radiobutton(window, text=[i+1], value=i+1, variable=self.num_rate)
            input_rating.grid(column=0, row=i+4, padx=2, pady=2)
            input_rating_btns.append(input_rating)

        self.output_txt = tk.Text(window, width=24, wrap="none")
        self.output_txt.grid(column=0, row=3, padx=10, pady=10)
    
    def display(self):
        key = self.input_ID.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key) 
            rating = lib.get_rating(key) 
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}" 
            set_text(self.output_txt, video_details)

            self.num_rate.set(rating)
        else:
            set_text(self.output_txt, f"Video {key} not found")

    def update(self):
        key = self.input_ID.get()
        rating = self.num_rate.get()
        lib.ratingupdate(key, rating)
        self.display()
        
if __name__ == "__main__":
    window = tk.Tk()
    UpdateVideos(window)
    window.mainloop()