Welcome to library management API:

Let's talk about several MarkUps about this API: 
Requests that can be performed in this API are:

For Users Management:
1. Post Request for Creation of User: This endpoint lets you create a new user in database. As you provide Name , Password and Role fields as BODY() param. This POST request will insert a new user row in databse schema.
2. Post Request for logging in of User: This endpoint will let you generate new refreshed jwt tokens for already registered users. incase if your token gets expired just use this request and get a new one.
3. DELETE Request for deletion of User: delete any user by passing his/her ID.


For Books Management:
1. GET Request for fetching of Books: This endpoint lets you see all the books that are available in database. It exposes unique ID of books that can be used while issuing any book.
2. POST request for adding up book in db: This endpoint lets you create a new book in database. As you provide Title , Author , Publication,'Subject' and No_of_copies fields as BODY() param. This POST request will insert a new user row in databse schema. Note that only Librarians are authorized and entitled to perform this task.
3. POST request for getting any book issued: To get any book issued from library , use this API end point. Any user , be it a librarian or student, can issue book from db.


Tech-Stack that has been used in it contains:
Database: Postgresql database has been used in creation of this project. It's a relational database which stores 
data in tabular format.
Framework:  FastAPI is used in creation of this project.
Migrations:  ALEMBIC is very efficient and swift performer for database migraions.
Security: JWT token based Authentication provides this API a very secured interface. Token gets expired after a while
hence user has to get new one. This makes chances of data leaking very less.


Relationship among schemas

One-Many relationships:
This kind of relationship means that one row in a table (usually called 
the parent table) can have a relationship with many rows in another table (usually called child table).
eg: 

1. One librarian may make several book insertions, but each pinsertion is made by a single librarian.


One-One relationship:
It’s a relationship where a record in one entity (table) is associated with exactly one record in
another entity (table).

1. Book - Author. One book can only have one author

Many-Many relationships:

1.One professor could teach one or many subjects, but one subject could also be taught by
one or many professors. It seems it is an M:N relationship

