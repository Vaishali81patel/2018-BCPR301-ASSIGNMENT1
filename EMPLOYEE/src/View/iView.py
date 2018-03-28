from plotly import *
import plotly.graph_objs as ob


class EmployeeData_View:
    # This class is enable to display employee
    # As well as display charts by using pickle
    # Also able to display graph based on the data store in the system
    #
    # Written By: Patel
    #

    @staticmethod
    def display(display_string):
        # This function enable to display a given string to the screen.
        #
        print (display_string)

    @staticmethod
    def read(prompt):
        # This function enable to read and input data on to the screen
        # while giving prompt to the user
        # which is then passed into the method.
        #
        # Written: Patel
        #
        return input (prompt)


    def manual_employee_data_entry(self):
        # This function is enable user to enter employee's data manually
        # Hereby; I have made the employee_data_arr "array"
        # Which will be keep appending as the user put the data over and over again
        #
        # Written ByL Patel
        #
        emp_data_arr = []
        employee_data = [self.read ("Enter Employee ID: "), self.read ("Enter gender: "),
                       self.read ("Enter age: "), self.read ("Enter sales count: "),
                       self.read ("Enter BMI: "), self.read ("Enter salary: "),
                       self.read ("Enter birthday, e.g. dd-mm-yyyy: ")]
        emp_data_arr.append (employee_data)
        return emp_data_arr


    @staticmethod
    def display_graph(graph_data):
        # This function is enable to take a graph object from the graph generator function
        # and display it in the web browser
        #
        # Written By: Patel
        #
        offline.plot(graph_data)

    def sales_by_gender_graph(self, emp_data_arr):
        # This function is enable to display the graph for the employee
        # sales vs gender based on the data store in the system
        #
        # Written By: Patel
        #
        emp_gender_data = []
        emp_sales_data = []
        for employee in emp_data_arr:
            emp_gender_data.append (employee[1])
            sales = int (employee[3])
            emp_sales_data.append (sales)
        graph_data = [ob.Bar (x=emp_gender_data, y=emp_sales_data)]
        graph_format = ob.Layout (title="Gender Verse Sales Bar Graph", xaxis=dict (title="Gender"),
            yaxis=dict (title="Sales"))
        graph = ob.Figure (data=graph_data, layout=graph_format)
        self.display_graph(graph)


    def employees_by_gender_graph(self, emp_data_arr):
        # This function is enable to display employee
        # Male and female ratio based on the employee data stored in the system
        #
        # Written By: Patel
        #
        emp_male_count = 0
        emp_female_count = 0
        for employee in emp_data_arr:
            if employee[1] == "M":
                emp_male_count += 1
            if employee[1] == "F":
                emp_female_count += 1

        graph_data = {'data': [{'labels': ['Male', 'Female'], 'values':
                                [emp_male_count, emp_female_count], 'type': 'pie'}],
            'layout': {'title': 'Number of Employees by Gender'}}
        self.display_graph(graph_data)


    def age_verse_salary_graph(self, emp_data_arr):
        # This function is enable to display Scatter graph of employee
        # Male vs Female and their salary based on the data stored in the system
        # The function calculate the actual salary by deviede the salary by 1000
        # Then pass that information to the display graph function
        #
        # Written By: Patel
        #
        emp_age_data = []
        emp_salary_data = []
        for employee in emp_data_arr:
            emp_age_data.append (employee[2])
            salary = int (employee[5]) * 1000
            salary_data.append (salary)
        graph_data = [
            ob.Scatter (x=emp_age_data, y=salary_data,
                        marker=dict (color="rgb(16, 32, 77)"),
                        name="Age Verse Salary")]
        graph_format = ob.Layout (title="Salary Verse Age Scatter Graph",
                                  xaxis=dict (title="Age"),
            yaxis=dict (title="Salary"))
        graph = ob.Figure (data=graph_data, layout=graph_format)
        self.display_graph(graph)


    def bmi_pie_graph(self, emp_data_arr):
        # Thie function is enable to display pie graphof the employee
        # BMI and matching them with each employee based on the data stored in the system
        #
        # Written By: Patel
        #
        emp_normal_count = 0
        emp_obesity_count = 0
        emp_underweight_count = 0
        emp_overweight_count = 0
        for employee in emp_data_arr:
            if employee[4] == "Normal":
                emp_normal_count += 1
            if employee[4] == "Overweight":
                emp_overweight_count += 1
            if employee[4] == "Obesity":
                emp_obesity_count += 1
            if employee[4] == "Underweight":
                emp_underweight_count += 1
        graph_data = {'data': [{'labels': ['Normal', 'Overweight', 'Obesity', 'Underweight'],
                                'values': [emp_normal_count, emp_overweight_count,
                                           emp_obesity_count, emp_underweight_count],
                                'type': 'pie'}], 'layout': {'title': 'Staff by BMI'}}
        self.display_graph(graph_data)