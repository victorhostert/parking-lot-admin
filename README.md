# Parking Lot Admin

### Developed by Victor William Hostert

---
## 🧪 Technologies used in this project

This project is in development with these technologies:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)


## 🚀 How to execute

The first step is having Git installed in your PC. If you haven't downloaded it, you can do it [with this link](https://git-scm.com/downloads). To verify if you have git, use the following command:

```bash
$ git --version # If you have git, the version number should appear on your console
```

Clone the project using the HTTPS url, in a folder of your preference, clicking in "clone" at the repository page, selecting the HTTPS option and using the following command:

```bash
$ git clone <URL HTTPS>
```

Alternatively, you can download the repository in .zip

In your local machine, ensure that you have [PIP](https://pip.pypa.io/en/stable/installation/) working, and install the libraries specified in the ```requirements.txt``` file.

Now, to access the project, just type the following commands on your console:

```bash
$ python manage.py migrate
$ python manage.py runserver
```

As this is just an API, you will find the endpoints available in [this url](http://localhost:8000/api/v1/)

The available endpoints are:

```bash
{
    "customer": "http://localhost:8000/api/v1/customer/", # Create and update customers
    "vehicle": "http://localhost:8000/api/v1/vehicle/", # Create and update customer's vehicles
    "movement": "http://localhost:8000/api/v1/movement/", # Create and update parking lot movements
    "movement_exit": "http://localhost:8000/api/v1/movement_exit/", # Set an exit_date for an existing movement
}
```
