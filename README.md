# kinetiq-erp-mrp-backend


## Software requirements
- Python 3.12
- Command Prompt or Windows Powershell
- VSCode
- Postgresql (Global RDS Configured if not please set it up [see here](https://docs.google.com/document/d/1NmH_GS6NpMKZxBPbKqozTPoMK6dHiAJu00b_YAovWyc/edit?fbclid=IwZXh0bgNhZW0CMTEAAR6-Ngf63KTtD31ES4fc-zDIYxgOxA6uI_SLaHC0d7NK-MFvgCCVDDNojVp4tA_aem_pqTglMc8FedXJpgAwblCcA&tab=t.wiqck6z0ce11#heading=h.hwjc1ymddv4z))
## Run Locally

Clone the project

```bash
$ git clone https://github.com/Kinetiq-PLM/kinetiq-erp-mrp-backend.git
```

Go to project directory
```bash
$ cd kinetiq-erp-mrp-backend
```

Create virtual environment
```bash
$ python -m venv venv
```

Activate virtual environment
```bash
$ venv\Scripts\activate
```

Install requirements
```bash
$ pip install -r requirements.txt

```

Go to backend project directory

```bash
$ cd mrp_backend
```

Open in VSCode
```bash
$ code .
```
### In terminal of VSCode

Switch branch to mrp/main
```bash
$ git checkout mrp/main
```

Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Run the server
```bash
$ python manage.py runserver
```
