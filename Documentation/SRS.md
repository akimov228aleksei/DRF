- # Introduction 
    
    #### Purpose
        Employee Management is a web based 
        application for managing employees,
        departments and vacation.

    #### Document conventions
        DRF - django rest framework.
        API - Application Programming Interface.

- # Overall Description 
    
    #### Product features
      - Show list of departments.

      - Show detailed information about the department.

      - Updating the list of departments (adding, deleting, editing). This operation is not available to all users.
   
      - Show list of employees. 

      - Show detailed information about an employee.

      - Updating the list of employees (adding, deleting, editing). This operation is not available to all users.
    
      - Employee vacation management
    
    #### Operating environment
        Python - v3.9
        Ubuntu - v20.04
        Postgres - v14.2

- # External interface requirements
    #### User interfaces: 
        The user will interact with the application through a graphical interface. The user will have access to 3 sections: employees, departments, vacations.
        Department: This mode is intended for viewing the list of departments, description, creation date, update date.
        Employee: The mode is intended for displaying the list of employees, their salaries, department, job assignment and position.
        Vacation: This mode is intended for viewing employees on vacation, deleting and editing the vacation date.
        
    #### Communication interfaces
        There is an API for communication in the application. By sending requests to the API, third-party applications can receive various data.

- # Non functional requirements 
    #### Software quality attributes
        To check the quality of the code, use:
         - Unit tests and integration tests
         - Coverage  
         - Linters 


