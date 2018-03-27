import csv
# The csv module implements classes to read and write tabular data in CSV format.
import shelve
# shelve builds on top of pickle and implements a serialization dictionary where objects are pickled


class FileHandler:
    # This class is enable to do  file handling
    # relate to this project
    # Raise exception error If unable to do so
    #
    # Written By: Patel
    #
    def load_file (self,file_path='data.csv'):
        # This function enable to load file path and store the data array
        # Raise the exception error if unable to find the path
        #
        # Written By: Patel
        #
        emp_data_arr = []   # Declare data array
        try:
            with open(file_path, newline='') as file:
                file_read = csv.reader(file)
                for row in file_read:
                    emp_data_arr.append(row)
        except FileNotFoundError:
            print ('File not found')
            return False
        except OSError:
            print ('File can not be reachable')
            return False
        return emp_data_arr


    def save_file (emp_data_arr,file_path='data.csv'):
        # This function is enable to save data array to the file path
        # Raise exception error if unable to do so
        #
        # Written By : Patel
        #
        try:
            with open(file_path, 'w', newline='') as emp_data_file:
                file_write = 'csv.writer'(emp_data_file, quotechar='|', delimiter=",",
                                   quoting=csv.QUOTE_MINIMAL)
                # Previously, if a line ended within a quoted field without a
                # terminating newline character, a newline would be
                # inserted into the returned field.
                for employee in emp_data_arr:
                    file_write.writerow(employee)
        except FileNotFoundError:
            print ('File not found')
            return False
        except OSError:
            print ('File can not be reachable')
            return False
        return True


