import re
from Employee import *
import doctest


class DataValidator:

    def validate_emp_data(self, valid_data_arr):
        # where valid employee data stores
        clean_employee = []

        try:
            for valid_employee in valid_data_arr:
                print ('valid_employee_data', valid_employee)

                if len(valid_employee) == 7:
                    cleaned_employee = []
                    print ("employee data is correct length")

                    if self.validate_empid (str (valid_employee[0])):
                        print ("Valid employeeID: " + str (valid_employee[0]))
                        cleaned_employee.append (str (valid_employee[0]))

                    if self.validate_gender (str (valid_employee[1])):
                        print ("Valid gender: " + str (valid_employee[1]))
                        cleaned_employee.append (str (valid_employee[1]))

                    if self.validate_age (str (valid_employee[2])):
                        print ("Valid age: " + str (valid_employee[2]))
                        cleaned_employee.append (str (valid_employee[2]))

                    if self.validate_sales (str (valid_employee[3])):
                        print ("Valid Sales: " + str (valid_employee[3]))
                        cleaned_employee.append (str (valid_employee[3]))

                    if self.validate_bmi (str (valid_employee[4])):
                        print ("Valid BMI: " + str (valid_employee[4]))
                        cleaned_employee.append (str (valid_employeen[4]))

                    if self.validate_salary (str (valid_employee[5])):
                        print ("Valid salary: " + str (valid_employee[5]))
                        cleaned_employee.append (str (valid_employee[5]))

                    if self.validate_birthday (str (valid_employee[6])):
                        print ("Valid birthday: " + str (valid_employee[6]))
                        cleaned_employee.append (str (valid_employee[6]))
                    else:
                        return "Not enough feilds: " + str (len (valid_employee))

                    filter (None, cleaned_employee)

                    print ("Cleaned person after filter: ", cleaned_employee)

                    if len (cleaned_employee) == 7:
                        clean_employee.append (cleaned_employee)

        except TypeError:
                    print(TypeError)
                    print("Wrong Data type entered!")

                    print("Cleaned employee after filter: ", clean_employee)

                    return clean_employee

    @staticmethod
    def validate_employeeID(empID):
        """
        Checks empID = [A-Z][0-9]{3}) e.g. E101
        >>> DataValidator.validate_employeeID("E111")
        True
        """
        if re.compile ("^[A-Z][0-9]{3}$").match (empID):
            return True
        else:
            return False

    @staticmethod
    def validate_gender(gender):
        """
        Checks gender = M or F e.g. M or F
        >>> DataValidator.validate_gender("F")
        True
        """
        if re.compile ("^[M|F]$").match (gender):
            return True
        else:
            return False

    @staticmethod
    def validate_age(age):
        """
        Checks age = [0-9]{2} e.g. 0 to 99
        >>> DataValidator.validate_age(str(64))
        True
        """
        if re.compile ("^[0-9]{2}$").match (age):
            return True
        else:
            return False

    @staticmethod
    def validate_sales(sales):
        """
        Checks Sales = [0-9]{3} e.g. 330
        >>> DataValidator.validate_sales(str(999))
        True
        """
        if re.compile ("^[0-9]{3}$").match (sales):
            return True
        else:
            return False

    @staticmethod
    def validate_bmi(bmi):
        """
        Checks BMI = normal|overweight|obesity|underweight case insensitive
        >>> DataValidator.validate_bmi("Overweight")
        True
        """
        if re.compile ("^Normal|Overweight|Obesity|Underweight$").match (bmi):
            return True
        else:
            return False

    @staticmethod
    def validate_salary(salary):
        """
        Checks Salary = [0-9]{2,3} e.g. 33 or 330
        >>> DataValidator.validate_salary(str(24))
        True
        """
        if re.compile ("^[0-9]{2,3}$").match (salary):
            return True
        else:
            return False

    @staticmethod
    def validate_birthday(birthday):
        """
        Checks birthday = [0-9]{1,2}-[0-9]{1,2}-[0-9]{4} e.g. 2-5-1967
        >>> DataValidator.validate_birthday("2-6-2014")
        True
        """
        if re.compile ("^([0-9]{1,2})-([0-9]{1,2})-([0-9]{4})$").match (birthday):
            # TODO make it smarter to get the month a days in the correct order
            return True

        else:
            return False

# doctest.testmod(verbose=True)
