import tkinter


def create_button(root, text, button_action, row, col, rowspan, colspan):
    B = tkinter.Button(root, text=text, command=button_action)
    B.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan)