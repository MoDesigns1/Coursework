"""
@author: Mohab Elhasade
"""

import csv


class Leopard:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.header = self.get_header()
        self.data = self.get_data()

    def get_header(self) -> list:
        # get headers from the csv file
        try:
            with open(self.filepath, 'r') as fp:
                reader = csv.reader(fp)
                header = next(reader)  # Gets the header
            return header
        except StopIteration:  # If the file is empty it returns None
            return ("File is empty.")
        except FileNotFoundError:  # If the file is not found it returns None
            return ("File not found.")

    def get_data(self) -> list:
        try:
            with open(self.filepath, 'r') as fp:
                reader = csv.reader(fp)
                next(reader)  # Skips the header
                data = [row for row in reader]  # Creates a list of lists
            return data
        except StopIteration:
            return None
        except FileNotFoundError:
            return None

    def stats(self) -> dict:
        if self.header is None:  # Checks if file is empty
            return None
        if self.data is None:  # Checks if file is empty
            return None
        stats = {}  # Creates a dictionary
        j = -1
        for col in self.header:  # Loops through the columns
            # Values below are reset for each column
            count = 0
            addition = 0
            mean = 0
            j += 1
            i = self.header.index(col)
            try:
                runningMax = float(self.data[i][j])
            except ValueError:
                runningMax = 0
            except ValueError:
                runningMax = 0
            try:
                runningMin = float(self.data[i][j])
            except IndexError:
                pass
            except ValueError:  # If the value is not an integer it passes
                pass
            for i in range(0, len(self.data)):  # Loops through the rows
                try:
                    # Converts the value to an integer
                    number = float(self.data[i][j])
                    count += 1
                    # Adds the value to the addition
                    addition += float(self.data[i][j])
                    # Checks if the value is greater than the runningMax
                    if number > runningMax:
                        runningMax = number
                    # Checks if the value is less than the runningMin
                    if number < runningMin:
                        runningMin = number
                    mean = addition / count  # Calculates the mean
                    mean = round(mean, 2)  # Rounds to 2 decimal places
                    # Adds the values to the dictionary
                    stats[col] = {'count': count, 'mean': mean,
                                  'max': runningMax, 'min': runningMin}
                except IndexError:
                    pass
                except ValueError:  # If the value is not an integer it passes
                    pass
        return stats

    def html_stats(self, stats: dict, filepath: str) -> None:
        if self.header is None:  # Checks if file is empty
            return None
        if self.data is None:  # Checks if file is empty
            return None
        with open(filepath, 'w') as fp:  # Creates a new file
            # Below is the html code
            fp.write("<html>\n")
            fp.write("<head>\n")
            fp.write("<title>Stats</title>\n")
            fp.write("</head>\n")
            fp.write("<body>\n")
            fp.write("<table>\n")
            fp.write("<style>\n")
            # Below is CSS styling to make the table look nicer.
            fp.write("td:nth-child(even), th:nth-child(even)")
            fp.write("{ background-color: #D6EEEE; }\n")
            fp.write("td:nth-child(odd), th:nth-child(odd)")
            fp.write("{background-color: #F0F8FF; }\n")
            fp.write("table, th, td { border: 1px solid black;")
            fp.write("text-align: center; \n")
            fp.write("border-collapse: collapse; }\n")
            fp.write("table { width: 100%; }\n")
            fp.write("</style>\n")
            fp.write("<tr>\n")
            fp.write("<th>\n")
            fp.write("<th>Count</td>\n")
            fp.write("<th>Mean</td>\n")
            fp.write("<th>Max</td>\n")
            fp.write("<th>Min</td>\n")
            fp.write("</th>\n")
            fp.write("</tr>\n")
            for column in stats:  # Loops through the columns
                fp.write("<tr>\n")
                # Writes column names.
                fp.write(f"<th>{column.capitalize()}</th>\n")
                for key in stats[column]:
                    # Writes the key and value
                    fp.write("<td>")
                    fp.write(f"{(stats[column][key])}</td>\n")
                fp.write("</tr>\n")
            fp.write("</table>\n")
            fp.write("</body>\n")
            fp.write("</html>\n")

    def count_instances(self, c1Name: str = "None", c1Val: int = 0,
                        c2Name: str = "None", c2Val: str = "None",
                        c3Name: str = "None", c3Val: str = "None") -> int:
        """
    To count the number of instances in the data that satisfy the conditions,
    the user must enter upto 3 critera followed by the value of the criteria.
    For example:
    objectName.count_instances("column1", intVal (i.e 1), "column2",
                               "value2", "column3", "value3")
    If less than 3 criteria are submitted, the empty ones are printed as None.
    Returned is the count of each instance that meets the criteria in the data.
    If a criteria is given that doesnt exist it returns an error message.
        """
        if self.header is None:
            return None
        if self.data is None:
            return None
        count1 = 0
        count2 = 0
        count3 = 0
        countList = []
        # Attempts to access the index of criterias
        try:
            self.header.index(c1Name)
            self.header.index(c2Name)
            self.header.index(c3Name)
        # If the criteria is not present it returns a error.
        except IndexError:
            countList.append("Error: One or more of criteria not found.")
            return countList[0]
        except ValueError:
            countList.append("Error: One or more of criteria not found.")
            return countList[0]
        try:
            for i in range(0, len(self.data)):  # Loops through the rows
                # Checks if the value is equal to the criteria.
                # adds to count if it matches.
                if self.data[i][self.header.index(c1Name)] == str(c1Val):
                    count1 += 1
                if self.data[i][self.header.index(c2Name)] == str(c2Val):
                    count2 += 1
                if self.data[i][self.header.index(c3Name)] == str(c3Val):
                    count3 += 1
        except IndexError:
            pass
        except ValueError:  # If the value is not an integer it passes
            pass
        # Below adds the counts with names & values to an array to be returned.
        countList.extend([f"the amount of instances of '{c1Name}"
                          f" = {c1Val}' is {count1}", "the amount of"
                          f" instances of '{c2Name} = {c2Val}' is"
                          f" {count2}", "the amount of instances of"
                          f" '{c3Name} = {c3Val}' is {count3}"])
        # Returns as a string
        return (f"\n{countList[0]} \n{countList[1]} \n{countList[2]}")


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    # test = Leopard("diabetes_data.csv")
    # print(test.get_header())
    # (test.get_data())
    # stats = test.stats()
    # print(stats)
    # test.html_stats(stats, "diabetes.html")
    # print()

    # test fide2021.csv
    # test2 = Leopard("fide2021.csv")
    # print(test2.get_header())
    # print(test2.get_data())
    # stats2 = test2.stats()
    # print(stats2)
    # test2.html_stats(stats2, "fide2021.html")
    # print()

    # test student.csv
    # test3 = Leopard("student.csv")
    # print(test3.get_header())
    # print(test3.get_data())
    # stats3 = test3.stats()
    # print(stats3)
    # test3.html_stats(stats3, "student.html")
    # print(test3.count_instances("studytime", 3, "sex", "F", "age", 18))
    print("TEST")
