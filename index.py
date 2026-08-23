### ACTIVITY 1

# student managment..
# students = {}


# def add_student():
#     student_id = input("Enter Student ID: ")

    
#     if student_id in students:
#         print("Student ID already exists.")
#         return

#     student_name = input("Enter Student Name: ")
#     age = int(input("Enter Age: "))
#     course = input("Enter Course: ")
#     email = input("Enter Email: ")

    
#     students[student_id] = {
#         "Student ID": student_id,
#         "Student Name": student_name,
#         "Age": age,
#         "Course": course,
#         "Email": email
#     }

#     print("Student added successfully.")


# def display_students():
#     if not students:
#         print("No student records found.")
#         return

#     print("\n--- All Student Records ---")

#     for student in students.values():
#         print("----------------------------")
#         print("Student ID   :", student["Student ID"])
#         print("Student Name :", student["Student Name"])
#         print("Age          :", student["Age"])
#         print("Course       :", student["Course"])
#         print("Email        :", student["Email"])


# def search_student():
#     student_id = input("Enter Student ID to search: ")

#     if student_id in students:
#         student = students[student_id]

#         print("\n--- Student Details ---")
#         print("Student ID   :", student["Student ID"])
#         print("Student Name :", student["Student Name"])
#         print("Age          :", student["Age"])
#         print("Course       :", student["Course"])
#         print("Email        :", student["Email"])
#     else:
#         print("Student not found.")


# def delete_student():
#     student_id = input("Enter Student ID to delete: ")

#     if student_id in students:
#         del students[student_id]
#         print("Student deleted successfully.")
#     else:
#         print("Student not found.")



# while True:
#     print("\n=== STUDENT MANAGEMENT SYSTEM ===")
#     print("1. Add Student")
#     print("2. Display All Students")
#     print("3. Search Student")
#     print("4. Delete Student")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_student()

#     elif choice == "2":
#         display_students()

#     elif choice == "3":
#         search_student()

#     elif choice == "4":
#         delete_student()

#     elif choice == "5":
#         print("Thank you for using Student Management System.")
#         break

#     else:
#         print("Invalid choice. Please try again.")



#---------------------------------------------


# product managment system ..
products = {}


def add_product():
    product_id = input("Enter Product ID: ")


    if product_id in products:
        print("Product ID already exists. Product not added.")
        return

    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")


    try:
        price = float(input("Enter Price: "))
    except ValueError:
        print("Invalid price. Product not added.")
        return

    
    try:
        stock_quantity = int(input("Enter Stock Quantity: "))
    except ValueError:
        print("Invalid stock quantity. Product not added.")
        return

    
    products[product_id] = {
        "Product Name": product_name,
        "Category": category,
        "Price": price,
        "Stock Quantity": stock_quantity
    }

    print("Product added successfully.")


def display_products():
    if not products:
        print("No products available.")
        return

    print("\n=== ALL PRODUCTS ===")

    for product_id, product in products.items():
        print("\nProduct ID:", product_id)
        print("Product Name:", product["Product Name"])
        print("Category:", product["Category"])
        print("Price:", product["Price"])
        print("Stock Quantity:", product["Stock Quantity"])


def search_product():
    product_id = input("Enter Product ID to search: ")

    if product_id in products:
        product = products[product_id]

        print("\n=== PRODUCT DETAILS ===")
        print("Product ID:", product_id)
        print("Product Name:", product["Product Name"])
        print("Category:", product["Category"])
        print("Price:", product["Price"])
        print("Stock Quantity:", product["Stock Quantity"])
    else:
        print("Product not found.")


def delete_product():
    product_id = input("Enter Product ID to delete: ")

    if product_id in products:
        del products[product_id]
        print("Product deleted successfully.")
    else:
        print("Product not found.")



while True:
    print("\n=== PRODUCT MANAGEMENT SYSTEM ===")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        display_products()

    elif choice == "3":
        search_product()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        print("Exiting Product Management System...")
        break

    else:
        print("Invalid choice. Please try again.")
