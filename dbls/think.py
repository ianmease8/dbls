

import sqlite3

# Connect to the database
connection = sqlite3.connect('records.db')
cursor = connection.cursor()


#tables customer, contract, services, charges

#customer customer id, first name, class id
#contract customerid,  service id
#services service id,  price,      description
#class    class id,    markup,     fuel charge,    

#makes the table sets the primary and foreign keys
tablemaking = '''
            CREATE TABLE class(
            class_id TEXT,
            markup REAL,
            fuel_charge REAL,
            PRIMARY KEY(class_id)
            );


            CREATE TABLE customer(
            ids TEXT,
            name TEXT,
            class_id,
            PRIMARY KEY(ids),
            FOREIGN KEY(class_id) REFERENCES class(class_id)
            );

            CREATE TABLE services(
            service_id TEXT,
            price REAL,
            description TEXT,
            PRIMARY KEY(service_id)
            );

            CREATE TABLE contract(
            c_ids TEXT,
            s_ids TEXT,
            FOREIGN KEY(c_ids) REFERENCES customer(ids),
            FOREIGN KEY(s_ids) REFERENCES services(service_id)
                
            );

'''
cursor.executescript(tablemaking)

#gets the name of the class 
def get_class_name(cursor):
    cursor.execute("SELECT class_id FROM class")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No class in database")
        return None
    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")
    choice = 0
    while choice < 1 or choice > len(results):
        choice = int(input("class ID: "))
    return results[choice-1][0]


#manual additions when i was stuck
def add_customer(cursor):
    ids = input("customerID: ")
    name = input("Name: ")
    classt = input("Class: ")
    values = (ids, name, classt)
    cursor.execute("INSERT INTO customer VALUES (?,?,?)", values)
    connection.commit()

def add_contract(cursor):
    ids = input("customer ID: ")
    price = input("contract ID: ")
    values =(ids, price)
    cursor.execute("INSERT INTO contract Values (?,?)", values)
    connection.commit()

def add_class(cursor):
    class_id = input("Class ID: ")
    markup = int(input("markup: "))
    fuel_charge = int(input("Fuel Charge: "))
    values =(class_id,markup,fuel_charge)
    cursor.execute("INSERT INTO class Values (?,?,?)", values)



def add_services(cursor):
    service_id = input("service ID: ")
    price = int(input("price: "))
    description = input("desc: ")
    values =(service_id,price,description)
    cursor.execute("INSERT INTO services Values (?,?,?)", values)

#adds items to the database
populate = '''
            INSERT INTO class(class_id,markup,fuel_charge) values
            ("G",50,100),
            ("S",25,50),
            ("B",10,15);
            INSERT INTO customer(ids,name,class_id) values
            ("1","steve", "G"),
            ("2","jobs","S"),
            ("3","mark","B");
            INSERT INTO services(service_id,price,description) values
            ("f",500,"fertilizer");
            INSERT INTO contract(c_ids,s_ids) values
            ("1","f"),
            ("2","f"),
            ("3","f");

'''
cursor.executescript(populate)

#joins tables together so math can be performed on them
sql = '''
        SELECT services.price, class.markup, class.fuel_charge
        from customer inner join contract on contract.c_ids = customer.ids 
        inner join services on services.service_id = contract.s_ids 
        inner join class on class.class_id  =  customer.class_id;
        '''

choice = None
while choice != "6":
    print("1) Display Class")
    print("2) Add Class")
    print("3) Update Class Markup")
    print("4) Delete Class")
    print("5) Display Charges")
    print("6) Quit")
    choice = input("> ")
    print()
    if choice == "1":
        cursor.execute("select * from class")
        for value in cursor.fetchall():
            print(value)
    elif choice == "2": 
        try:
            name = input("class id: ")
            title = int(input("markup: "))
            pay = int(input("fuel charge: "))
            values = (name, title, pay)
            cursor.execute("INSERT INTO class VALUES (?,?,?)", values)
            connection.commit()
        except ValueError:
            print("Invalid markup or fuel charge!")   
    elif choice == "3":
        try:
            name = input("class id: ")
            pay = int(input("markup: "))
            values = (pay, name) # Make sure order is correct
            cursor.execute("UPDATE class SET markup = ? WHERE class_id = ?", values)
            connection.commit()
            if cursor.rowcount == 0:
                print("Invalid class id!")
        except ValueError:
            print("Invalid markup!") 
    elif choice == "4":
        name = get_class_name(cursor)
        if name == None:
            continue
        values = (name, )
        cursor.execute("DELETE FROM class WHERE class_id = ?", values)
        connection.commit()
    elif choice == "5":
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            steve = row[0]*row[1]+row[2]
            print(steve)
    print()
connection.close()

#testing
# maybe = '''
#         SELECT customer.name, contract.s_ids
#         from customer inner join contract on contract.c_ids = customer.ids
# '''




