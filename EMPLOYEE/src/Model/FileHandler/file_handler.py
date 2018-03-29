import csv
# The csv module implements classes \
# to read and write tabular data in CSV format.
import shelve
# shelve builds on top of pickle and implements \
# a serialization dictionary where objects are pickled


class FileHandler:
    # This class is enable to do  file handling
    # relate to this project
    # Raise exception error If unable to do so
    #
    # Written By: Patel
    #
    def load_file(self, file_path='data.csv'):
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

    def save_file(emp_data_arr, file_path='data.csv'):
        # This function is enable to save data array to the file path
        # Raise exception error if unable to do so
        #
        # Written By : Patel
        #
        try:
            with open(file_path, 'w', newline='') as emp_data_file:
                    write = 'csv.writer(emp_data_file, quotechar='|', delimiter=",", quoting=csv.QUOTE_MINIMAL)
                # Previously, if a line ended within a quoted field without a
                # terminating newline character, a newline would be
                # inserted into the returned field.
                    for employee in emp_data_arr:
                        write.writerow(employee)
        except FileNotFoundError:
            print ('File not found')
            return False
        except OSError:
            print ('File can not be reachable')
            return False
        return True

    def shelve_file(emp_data_arr, file_path='data.shelf'):
        # This function is enable to shelve module can be
        # used as a simple persistent storage option for
        # Python objects when a relational database is overkill.
        # The shelf is accessed by keys, just as with a dictionary.
        # The values are pickled and written to a database
        # created and managed by anydbm.
        # Raise exception error if unable to do so
        #
        # Written By : Patel
        #
        try:
            count = 0
            d = shelve.open(file_path, 'c')
            for employee in emp_data_arr:
                count = count = 1
                d[str(count)] = employee
                d.close()
        except FileNotFoundError:
            print ("File ", file_path, "was not found!")
            return False
        return True