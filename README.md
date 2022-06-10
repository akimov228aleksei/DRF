# Application for personnel management
[![Python-package Actions Status](https://github.com/akimov228aleksei/DRF/workflows/Linter/badge.svg?branch=prod)](https://github.com/akimov228aleksei/DRF/actions)
[![Python-package Actions Status](https://github.com/akimov228aleksei/DRF/workflows/Coverage/badge.svg?branch=prod)](https://github.com/akimov228aleksei/DRF/actions)
[![Coverage Status](https://coveralls.io/repos/github/akimov228aleksei/DRF/badge.svg?branch=prod)](https://coveralls.io/github/akimov228aleksei/DRF?branch=prod)

## The application consists of two parts - frontend and backend. The backend contains an API for working with the database. Frontend contains an interface for communicating with the API.

## Quick start
1. Define environment variables for DB (or you may not define any environment variables. Then the default variables for sqlite3 will be used):
  * ENGINE_DB
  * NAME_DB
  * USER_DB
  * PASSWORD_DB
  * HOST_DB
  * PORT_DB

2. Open directory where located __manage.py__ file.
3. Use command `make init_app` to install all required dependencies.
4. Use command `make run` to run server.
5. You can login as administrator using username `admin` and password `123_pw_admin`, or as manager using username `manager` and password `123_pw_manager`.
