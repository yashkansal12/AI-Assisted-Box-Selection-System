# AI-Assisted-Box-Selection-System

Design and build a small Django-based system that recommends the most suitable box for an order.

When a customer places an order, the warehouse team
needs to know which shipping box should be used. Each product has dimensions and
weight. Each box has internal dimensions, maximum weight capacity, and cost.



## Features

- Product Management
- Box Management
- Order Management
- Automatic Box Recommendation
- Django Admin
- REST APIs
- Unit Tests


## Tech Stack

 Python 3.x
 Django


## Installation

```bash

cd BoxSelector

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```


## API Endpoints

### Products

GET

```
/api/products/
```

POST

```
/api/products/
```

### Boxes

GET

```
/api/boxes/
```

POST

```
/api/boxes/
```

### Orders

POST

```
/api/orders/
```

### Recommendation

GET

```
/api/orders/<id>/recommend/
```

---

## Recommendation Logic

The recommendation algorithm:

1. Calculates package dimensions using:
 Maximum Length
 Maximum Width
 Sum of Heights

3. Calculates total package weight.

4. Filters boxes that satisfy:
   Dimension constraints
   Weight constraints
   
6. Returns the lowest-cost suitable box.

---

## Assumptions

Products are assumed to be stacked vertically.

This assignment does not implement a full 3D bin-packing algorithm.

---

## Running Tests

```bash
python manage.py test
```
