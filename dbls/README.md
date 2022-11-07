# Overview

Goal

I wanted to make a database that allowed for a fluid updating between prices for a landscaping company, First I had to create a database with four tables to meet the basics of what I would need to have to be able to include a customer, a linking table of contract, and a services as well as a class table to help with dynamic prices. 

Description

I wrote software that is able to join two tables separated by two tables between them, to get the information needed for price depending on what level of client they are.

Purpose

I wanted to provide a way for a basic subscription based landscape company be able to dynamically improve and update pricing for a variety of different clauses.


[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

Relational database
I am using sqlite 3 which is the native database to python. 

databse overview
I created four tables, the first being a class table which determines what level of markup and fuelcharge those clients get, then a customer which has the name id and class level, followed by a linking table of contracts which connects customers to services to determine what services each customer is getting.
# Development Environment

python is the programming language
sql is the secondary language
and sqlite3 is the library 
# Useful Websites


* [SQL Tutorial](https://www.sqlitetutorial.net/)
* [Geeks for Geeks (join statements)](https://www.geeksforgeeks.org/python-sqlite-join-clause/#:~:text=INNER%20JOIN%20(OR%20JOIN)%20%E2%80%93,records%20from%20the%20left%20table.)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* change how the services table works, including different fertilizer services
* more updatable items in the main while loop
* expantion to include employees and time based charges and services