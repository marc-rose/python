import tkinter  # must have tkinter for GUI functionality


class templateView(tkinter.Frame):
    """
    class templateView is the VIEW for a simple program that exemplifies the MODEL/VIEW/CONTROLLER
    architecture. This VIEW class is a tkinter.Frame that contains Buttons, an Entry, and a Label.
    Two Buttons notify the CONTROLLER when they are pressed, and the other Button quits the app. The Label displays
    the return value called function in the MODEL.
    """

    def __init__(self, controller):
        """
        Initializes the templateView object, creates a reference to the CONTROLLER, and creates widgets
        """
        tkinter.Frame.__init__(self)
        self.pack()
        self.controller = controller  # creates reference to controller object sent as input
        self.createWidgets()

    def createWidgets(self):
        """
        Creates all widgets for tkinter.Frame object
        """
        self.inputEntry = tkinter.Entry()  # tkinter.Entry for text input
        self.inputEntry.insert(0, "Input Entry")  # default text
        self.inputEntry.pack({"side": "left"})

        self.function_a_Button = tkinter.Button(self)  # tkinter.Button to be pressed
        self.function_a_Button["text"] = "call function_a"
        self.function_a_Button["command"] = self.controller.buttonAPressed  # calls CONTROLLER function
        self.function_a_Button.pack({"side": "left"})  # positioning of widget

        self.function_b_Button = tkinter.Button(self)  # tkinter.Button to be pressed
        self.function_b_Button["text"] = "call function_b"
        self.function_b_Button["command"] = self.controller.buttonBPressed  # calls CONTROLLER function
        self.function_b_Button.pack({"side": "left"})  # positioning of widget

        self.outputLabel = tkinter.Label(self)  # tkinter.Label for displaying text output
        self.outputLabel["text"] = 0  # called from CONTROLLER and text replaced
        self.outputLabel.pack({"side": "left"})  # positioning of widget

        self.quitButton = tkinter.Button(self)  # tkinter.Button to be pressed
        self.quitButton["text"] = "Quit"
        self.quitButton["command"] = self.quit  # calls tkinter.Button.quit function
        self.quitButton.pack({"side": "left"})  # positioning of widget
