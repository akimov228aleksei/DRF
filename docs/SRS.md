- # Introduction 
    
  + ## Purpose
    Employee Management is a web based application for managing employees, departments and vacation. The application allows you to monitor employees in detail. Their department, salary, date of employment.

  + ## Document conventions
    DRF - django rest framework.

    API - Application Programming Interface.

- # Overall Description 
    
    + ## Product features
      - Show list of departments.

      - Show detailed information about the department.

      - Updating the list of departments (adding, deleting, editing). This operation is not available to all users.
   
      - Show list of employees. 

      - Show detailed information about an employee.

      - Updating the list of employees (adding, deleting, editing). This operation is not available to all users.
    
      - Employee vacation management
    
    + ## Operating environment
       - Python - v3.9
       - Ubuntu - v20.04
       - Postgres - v14.2
    
    + ## Design and implementation constraints
       - Django - v3.2
       - DRF - v3.13
       - Postgres - v14.2
       - Docker-compose - v3
       - Python - v3.9

- # External interface requirements
    + ## User interfaces: 
       The user will interact with the application through a graphical interface. The user will have access to 3 sections: employees, departments, vacations.
  
       Department: This mode is intended for viewing the list of departments, description, creation date, update date.    
       Employee: The mode is intended for displaying the list of employees, their salaries, department, job assignment and position.    
       Vacation: This mode is intended for viewing employees on vacation, deleting and editing the vacation date.
  
       An exemplary representation of the interface is shown in the figure:
       ![](https://i.imgur.com/Wv89eIO.png)
               
    + ## Communication interfaces
        There is an API for communication in the application. By sending requests to the API, third-party applications can receive various data. The application uses the API to get data from the database. The API allows you to query 3 tables: Department, Employee, Vacation. Also receive detailed information on these departments, if the user has the rights to do so. The general scheme of interaction is shown in the figure:
       
        ![](https://i.imgur.com/ebzNI5Y.png)

- # Non functional requirements 
    + ## Software quality attributes
       To check the quality of the code, use:
        - Unit tests and integration tests
        - Coverage  
        - Linters 
    
    + ## Security requirements 
       For security reasons, some functions are not available for certain categories of users:
       - Unregistered users: can view lists of employees, departments.
       - Registered users: can view employee lists, employee details, department lists, department details, vacation lists.
       - Administrator: can view all data, can edit all data, can delete all data.
