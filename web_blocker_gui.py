import tkinter
from web_block import WebsiteBlocker


class Gui:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.geometry("350x350")
        self.icon = tkinter.PhotoImage(file="icon.png")
        self.top.iconphoto(False, self.icon)
        self.filename = tkinter.PhotoImage(file="blocker.png")
        self.background_label = tkinter.Label(image=self.filename)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.insert_line_label = tkinter.Label(text="Website URL", fg="black", font=('Arial', 11, 'bold'))
        self.insert_line_label.pack()
        self.insert_line = tkinter.Entry(width=40)
        self.insert_line.pack()
        self.table = tkinter.Entry(width=20, fg='blue', font=('Arial', 11))
        self.top.mainloop()

    def create_table(self, rows, columns, lst):
        for i in range(rows):
            for j in range(columns):
                self.table.grid(row=i, column=j)
                self.table.insert(lst[i][j])


def main():
    Gui()


if __name__ == "__main__":
    main()
