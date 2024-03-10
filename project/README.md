# Online Organic Farm Shop program

#### Video Demo: [https://youtu.be/zQmzaYaQSBo](https://youtu.be/zQmzaYaQSBo)

# Description

Online Organic Farm Shop program is intended to select some products from the farm list, save, edit and get order in pdf format.

# Introduction

To start the program run `python project.py`. For details run `python project.py -h`. There 3 modes: create, edit and finish.

To create a new order run `python project.py -m create`. The short greeting of online organic farm store appears and invitation to select a product. Selection is performed by typing a number (index) of the product. There are an icon and a price of the product in the same line. For example, type 3, that is a cucumber and in 'select quantity' input type 1. After that the table with the name of the selected product, it's price, quantity and sum appears below. There is also a total sum of the cart under the table. It is possible to select any number of products from the list.

In any step it is possible to exit using Ctrl-D. After the exit the list of the products is saved in cart.csv file.

There are possible to edit the order saved in the cart.csv file by running `python project.py -m edit`. There are 3 options displayed on the screen:

1\. To add new product type: `1`.
2\. To delete existing product type: `2 <x>`, where x is the number of the product in the cart.
3\. To change quantity of exicting product type: `3 <x> <y>` where x is the number of the product and y is a new amount.

Any time it is possible to exit and save the changes to cart.csv file using Ctrl-D.

After each of the changes the updated table of selected products appears.

The last mode is finish, that generates the pdf file of the order. To do this run `python project.py -m finish`. In the folder appears the order.pdf file with the products in the order.

# Program Data

All user's data stored in list_product variable during user's selection of products.

After each exit using Ctrl-D the data is saved in cart.csv file and resaved after order modifications.

# Project files

All project files stored in project folder.

## Generated files

### **cart.csv file**

Cart.csv file contains header (Name, Icon, Price/Kg, Quantity, Sum $) and user's products accordingly.

### **order.pdf file**

Order.pdf file is the result of finish of the order. The file contains:

- title of the farm
- date and time when the order was created
- products selected by user: Product name, Price/Kg, Quantity, Sum $
- total sum of the order

## Program files

### **requirements.txt**

Requirements.txt file contains libraries of the project and their versions.

### **constants.py**

Constants.py file contains 4 constants to use throughout the code:

- CSV_FILE - name of the csv file
- FIELDNAMES - list of fieldnames for csv file
- FARM_LIST - list of available products (dicts)
- MAX_QUANTITY - max quantity that user is allowed to buy

### **project.py**

Project.py file consists of main function in which I use argparse to extract argument mode with 3 available options:

- \-m create - to create a new order
- \-m edit - to edit exists order
- \-m finish - to finish the order and generate order.pdf file

### **product.py**

In file product.py I created class Product with arguments name, icon and price. Also quantity and sum both set to 0.

I created class method `get_product()`, where I get the index from user's input and product data according to the index.

I have method `set_quantity_sum()`, where I get quantity of this product from user's input.

Next, I have `calculate_sum()` method where I calculate the sum of the product.

I have `save_to_csv()` method to save this product  to csv.file.

To get product data in the convinient format as a dict, I created `get_product_obj()` method.

### **create.py**

In the create.py file `create()` function performs:

- displays greeting to the user
- displays list of farm products
- opens csv file and cleans it from previous data
- creates empty `list_products`
- inside while loop when it is true:
  - creates a new product
  - checks if product is already in the cart
  - using next methods of the Product class:
    - sets quantity of the new product and calculates the sum,
    - saves new product to csv file
    - adds new product into list products as a dict
  - calls `display_cart()` function:
    - calculates sum of the order
    - displays the list products that user added

### **edit.py**

In the edit.py file `edit()` function performs:

- reads data from csv file into user's products list called `table`
- calculates total sum of the user's products list
- displays user's products list
- inside while loop when it is true:
  - informs user about 3 options to continue
  - prompts user for his choice
  - checks user's output
  - if user's output is valid and the selected option is `1`:
    - calls `add()` function with the table list as argument. `add()` function:
      - create a new product
      - check if the product is already in the cart. If yes, ignore.
      - add this product into the user's products list
      - display updated list products
  - if user's output is valid and the selected option is `2` and the typed number of the product is in the user's products list:
    - calls `delete()` function with 2 arguments - the table list and index of the product that user wants to delete. Deletes product from table list by the index of the product
  - if user output is valid and the selected option is 3, the typed number of the product is in the user's products list and a new amount of the product is valid:
    - calls `change_quantity()` function with 3 arguments - the table list, index of the product and a new amount of quantity. `change_quantity()` function:
      - checks legal index options
      - checks legal new quantity options
      - sets new quantity
      - calculates the sum of the product
  - if user output is not correct user again propmts to input
  - when user exits by Ctrl_D:
    - `save_to_cart()` function is called with the table list as argument. It writes the changed the user's products list data from the table list into csv file.

### **finish.py**

In the finish.py file `finish()` function performs:

- gets current date and time and converts it to the user readable format
- calls `get_data()` function to get user's order data and total sum from csv file
- initialises FPDF class instance
- adds title to the order
- adds date of the order
- creates table:
  - add header in the table
  - add rows(user's products, their price, quantity and sum) to the table
- add total sum of the order under the table

## Test file

### **test_project.py**

In file test_project.py I used pytest to test functions of the program.

The tests check:

- `test_product_calculate_sum()` checks if product sum is calculated correctly
- `test_get_product_obj()` checks format the product object is correct
- `test_delete()` checks if product is deleted correctly
- `test_change_quantity()` checks if product quantity is changed correctly
- `test_change_quantity_error_index()` checks if ValueError is raised when the index is not correct
- `test_change_quantity_error_quantity()`  checks if ValueError is raised when the quantity is not correct

# **How to run**

To start the program run `python project.py`.

For details run `python project.py -h`. There 3 modes: create, edit and finish.
