"""
@author: Mohab Elhasade
"""

import csv


class Leopard:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        global empty
        empty = False
        # Attempt to open the file and check its length.
        try:
            testF = open(filepath, 'r')
            val = testF.read()
            testF.close()
            if len(val) == 0:
                empty = True
                print("Empty file.")
                self.header = None
                self.data = None
            else:
                with open(filepath, 'r') as fp:
                    reader = csv.reader(fp)
                    self.header = next(reader)  # Gets the header
                    self.data = [row for row in reader]  # Creates a list
        except FileNotFoundError:
            print("File not found.")
            empty = True
            self.header = None
            self.data = None

    def get_header(self) -> list:
        # checks if file is empty
        if empty:
            return None
        else:
            return self.header

    def get_data(self) -> list:
        if empty:
            return None
        else:
            return self.data

    def stats(self) -> dict:
        if empty:
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
            except (ValueError, IndexError):
                runningMax = 0
            try:
                runningMin = float(self.data[i][j])
            except (IndexError, ValueError):
                runningMin = 100000
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
        if empty:
            return None
        # Initalizes the html variable that stores the code.
        html = """<html>
        <head>
        <title>Stats</title>
        </head>
        <body>
        <table>
        <style>
        td:nth-child(even), th:nth-child(even) {
        background-color: #45C4B0;
        }
        td:nth-child(odd), th:nth-child(odd) {
        background-color: #13678A;
        }
        table, th, td {
        border: 1px solid white;
        text-align: center;
        border-collapse: collapse;
        }
        table {
        width: 50%;
        }
        th, td {
        color: white;
        }
        table {
        padding: 10px;
        margin-left: auto;
        margin-right: auto;
        }
        h1 {
        text-align: center;
        }
        * {
        font-family: Arial, Helvetica, sans-serif;
        }
        table {
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
        }
        th {
        border: 1px solid white;
        text-align: center;
        border-collapse: collapse;
        }
        </style>
        <h1>Stats of the CSV file</h1>
        <tr>
        <th>Stats</th>
        <th>Count</th>
        <th>Mean</th>
        <th>Max</th>
        <th>Min</th>
        </tr>
        """
        for column in stats:
            html += f"<tr><th>{column.capitalize()}</th>"
            for key in stats[column]:
                html += f"<td>{stats[column][key]}</td>"
            html += "</tr>"
        html += "</table></body></html>"
        with open(filepath, 'w') as fp:
            fp.write(html)
            fp.close()

    def count_instances(self, c1Name: str = "None", c1Val: str = "None",
                        c2Name: str = "None", c2Val: str = "None",
                        c3Name: str = "None", c3Val: str = "None") -> int:
        """
    To count the number of instances in the data that satisfy the conditions,
    the user must enter 3 critera followed by the value of the criteria.
    For example:
    objectName.count_instances("column1", "value1", "column2",
                               "value2", "column3", "value3")
    The values entered could be integers or strings.
    Integers have to be passed by as a string, for example:
    objectName.count_instances("column1", "1", "column2", "2")
    If less than 3 criteria are submitted an error is given.
    Returned is the count of when all criterias are True in the same row.
    If a criteria is given that doesnt exist it returns an error message.
        """
        if empty:
            return None
        self.header = [head.lower() for head in self.header]
        count = 0
        criteria = [c1Name, c2Name, c3Name]
        countList = []
        criteriaIndex = []
        criteria = [crit.lower() for crit in criteria]
        if "None" in criteria:
            countList.append("Error: 3 Criterias not passed.")
            return countList[0]
        # Attempts to access the index of criterias
        try:
            for i in criteria:
                criteriaIndex.append(self.header.index(i))
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
                if self.data[i][criteriaIndex[0]] == str(c1Val):
                    if self.data[i][criteriaIndex[1]] == str(c2Val):
                        if self.data[i][criteriaIndex[2]] == str(c3Val):
                            count += 1
        except IndexError:
            pass
        except ValueError:  # If the value is not an integer it passes
            pass
        # Below adds the counts with names & values to an array to be returned.
        answer = (f"The amount of instances where {c1Name.capitalize()} == ")
        answer += (f"{c1Val} and {c2Name.capitalize()} == {c2Val} and ")
        answer += (f"{c3Name.capitalize()} == {c3Val} is ({count})")
        # Returns as a string
        return answer


if __name__ == "__main__":
    # DO NOT COMMENT ALL WHEN SUBMIT YOUR FILE, cannot have an if statement
    # with nothing afterwards.

    # test diabetes_data.csv
    # test = Leopard("diabetes_data.csv")
    # print(test.get_header())
    # print(test.get_data())
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
    # print(test2.count_instances("Rank", 18, "Country", "RUS", "Games", "0"))
    # print()

    # test student.csv
    # test3 = Leopard("testing.csv")
    # print(test3.get_header())
    # print(test3.get_data())
    # stats3 = test3.stats()
    # print(stats3)
    # test3.html_stats(stats3, "student.html")
    # print(test3.count_instances("STUDYTIME", "3", "sex", "F", "age", "18"))
    print()
