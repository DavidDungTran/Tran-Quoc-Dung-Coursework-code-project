import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateVideos:
    def __init__(self, window):
        window.title("Create Videos")

        self.videos_in_list_txt = tkst.ScrolledText(window, width=64, height=12, wrap="none")
        self.videos_in_list_txt.grid(column=0, row=1, rowspan=4, sticky="w", padx=10, pady=10)

        self.playing_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.playing_txt.grid(column=1, row=1)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=0)

        create_list_btn = tk.Button(window, text="Create a queue list", command=self.create_list_queue)
        create_list_btn.grid(column=1, row=0)

        detele_btn = tk.Button(window, text="Delete the list", command=self.delete_list)
        detele_btn.grid(row=2, column=1, sticky="EW")

        self.play_btn = tk.Button(window, text="play", command=self.play)
        self.play_btn.grid(row=2, column=2, sticky="EW")

    def create_list_queue(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{key}: {name}, {director}, rating: {rating}, play counts: {play_count}"
            text = self.videos_in_list_txt.get("1.0", tk.END)
            if text == "":
                self.videos_in_list_txt.insert(tk.END, video_details)
            else:
                self.videos_in_list_txt.insert(tk.END, "\n" + video_details)
        else:
            # Do nothing, don't add anything to the list
            pass
    def delete_list(self):
        self.videos_in_list_txt.delete("1.0", tk.END)

    def play(self):
        current_text = self.videos_in_list_txt.get("1.0", tk.END)
        if current_text:
            lines = current_text.split("\n")
            if len(lines) > 1:
                second_item = lines[1]
                parts = second_item.split(": ")
                key = parts[0]
                if key in lib.library:
                    item = lib.library[key]
                    lib.increment_play_count(key)
                    set_text(self.playing_txt, f"Now playing: {item.name}\nDirector: {item.director}\nrating: {item.rating}\nplaycounts: {item.play_count}")
                    self.videos_in_list_txt.delete("2.0", "3.0")
                else:
                    set_text(self.playing_txt, "Error: Video not found")
            else:
                set_text(self.playing_txt, "Not enough videos in list")
        else:
            set_text(self.playing_txt, "No videos in list")



if __name__ == "__main__":
    window = tk.Tk()
    CreateVideos(window)
    window.mainloop()