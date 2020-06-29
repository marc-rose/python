import tkinter  # must have tkinter for GUI functionality
import tkinterView  # the VIEW
import tkinterModel  # the MODEL


class templateController:
    """
    The CONTROLLER for an app that follows the MODEL/VIEW/CONTROLLER architecture.
    When the user presses a Button on the VIEW, this CONTROLLER calls the appropriate
    functions in the MODEL. The CONTROLLER handles all communication between the MODEL
    and the VIEW.
    """
    def __init__(self):
        """
        This starts the Tk framework up, Instantiates the VIEW (a MyFrame object),
        and starts the event loop that waits for the user to press a Button on the VIEW.
        """
        root = tkinter.Tk()
        self.model = tkinterModel  # reference ConvertModel module (not class) for functions (not methods) later
        self.view = tkinterView.templateView(self)  # self.view is an instance of the templateView Class
        self.view.mainloop()
        root.destroy()

    def buttonAPressed(self):
        """
        When function_a_Button is pressed in the VIEW, the VIEW calls this function
        """
        entry = self.view.inputEntry.get()  # get text value from VIEW inputEntry widget
        self.view.outputLabel["text"] = "function_a return: " + self.model.function_a(entry)
        # set VIEW's Label text from MODEL's function output

    def buttonBPressed(self):
        """
        When function_a_Button is pressed in the VIEW, the VIEW calls this function
        """
        entry = self.view.inputEntry.get()  # get text value from VIEW inputEntry widget
        self.view.outputLabel["text"] = "function_b return: " + self.model.function_b(entry)
        # set VIEW's Label text from MODEL's function output


if __name__ == '__main__':
    program = templateController()  # create a templateController object