from interpreter_controller import IInterpreterController
from View.iView import *
from Model.Interpreter import *
from FileHandler.FileHandler import *
from DataValidation.EmpDataValidator import *
from Model.Database.Database import *
import sys

if __name__ == '__main__':
    InterpreterController(EmployeeData_View(), Interpreter(
        FileHandler(), DataValidator(), Database(),
        InterpreterController.set_file_path(sys.argv))).cmdloop()

# sys.argv is a list in Python,
# which contains the command-line
# arguments passed to the script.
# With the len(sys.argv) function
# you can count the number of arguments.
