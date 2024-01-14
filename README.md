# pegb_project
Technical assessment test of PegB Python Developer

author: Do Duy Manh

INSTRUCTION TO RUN BACKEND IN LOCAL
* All of my source code are in /docker/backend/image/pegbbackend/

I. Tools:
- Docker Desktop
- Postman

II. Setup
1. Change SOURCEROOT in /docker/.env to path of folder pegbbackend (/docker/backend/image/pegbbackend).
2. Open Docker Desktop, open terminal and run "docker network create pegbnetwork".
3. Open file hosts and add hosts:
	127.0.0.1 pegb.staff.me
    127.0.0.1 pegb.customer.me
    127.0.0.1 pegbdb

4. Open Terminal/cmd and cd to folder docker. 
    - run "docker build -t be-python-3-12:1.0.0 ./backend/image/"
    - run "docker compose up -d". There are 4 container are executed (pegb-nginx, pegbstaffapi, pegbcustomerapi, pegbdb).
    * If you already have other docker containers, please make sure ports 3306 and 80 are available.

5. In Docker Desktop, open container pegbstaffapi, tab Exec. Execute the following commands to migrate database
	- bash
	- python manage.py makemigrations --settings=pegbbackend.settings.staff.settings
	- python manage.py migrate --settings=pegbbackend.settings.staff.settings

6. Open Postman, import collections and environment:
    - Collections and environment file are in folder postman
    - MUST SEND THE REQUEST "init-data" in Pegb Staff collection first.

7. After the request "init-data" respond success, the rest requests are able to test now.

* NOTE: Some of apis have to be filled data in body correctly.
- In collection Pegb Staff:
    - update-product: "old_name" 
    - remove-product: "name", "description", "category"
    Send request "get-list-product" to get these data.

- In collection Pegb Customer:
    - remove-from-cart: "name"
    Send request "get-list-in-cart" to get these data.

Thanks
