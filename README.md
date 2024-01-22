# Study Tracker

Study Tracker is a desktop application that helps you track your study hours and goals. It uses Microsoft SQL Server, stored procedures, and Python with tkinter and pypyodbc libraries to insert data and display total study hours.

## Installation

To install and run Study Tracker, you need to have the following:

- Microsoft SQL Server
- Python 3.7 or higher
- tkinter and pypyodbc libraries

You can install the libraries using pip:

```bash
pip install tkinter
pip install pypyodbc
```

Then, clone this repository to your local machine:
git clone https://github.com/Ahmed-Elzayat112/study-tracker.git

To use Study Tracker, you need to create a database and a table in Microsoft SQL Server. You can use the following SQL script to create them:
CREATE DATABASE StudyTracker;
GO

USE StudyTracker;
GO

CREATE TABLE StudyLog (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Subject VARCHAR(50) NOT NULL,
    Date DATE NOT NULL,
    Hours INT NOT NULL
);
GO

Then, you need to modify the connection string in the study_tracker.py file to match your server name, database name, user name, and password.
After that, you can run the study_tracker.py file to launch the application. You will see a window like this:
!Study Tracker screenshot
You can use the buttons to add, edit, delete, or view your study logs. You can also see the total study hours for each subject and the overall progress.

Contributing

Study Tracker is an open source project and welcomes contributions from anyone. If you want to contribute, you can:

    Report bugs or suggest features by opening an issue.
    Fix bugs or implement features by submitting a pull request.
    Contact me by email at ahmedelzayat625@gmail.com.


