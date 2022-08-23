# Authentication-Project

**To use this program, run login_main.py.** This will begin a series of prompts, that when 
followed, allow a user to either sign up or log in. If signing up, your name and password will be stored securely in an SQL database. If logging in, your credentials will be compared against that database, and a correct set of credentials will grant you access to the application. 

The only dependency is sqlite3. All other libraries are built-in. 
 
This is a toy project to practice different ways to ensure secure login information for a given user. I relied on Robert Heaton's fantastic [blog](https://robertheaton.com/2019/08/12/programming-projects-for-advanced-beginners-user-logins/) for the idea and general steps. Eventually I'd like to add two-factor authentication to get experience implementing more strict security practices. In the meantime, I intend to add functionality for successfully logged-in users as well as a UI to facilitate using this program outside the terminal.


### How this all works in more detail:
First, the user inputs whether they'd like to sign up or log in.

***To sign up:*** \
The user inputs a username which is checked for validity and uniqueness against the database. \
The user then inputs a password, which is also checked for validity. \
A randomly-generated 32-bit salt is then created and added to the database. \
The user password and the salt are combined and hashed using sha256 encryption, the result 
of which is also 
added to 
the 
database. This value will be used to compare against future log-in attempts.

***To log in:*** \
When a user logs in, they supply a username and a password. \
If a username is valid, the corresponding salt from the database is retrieved. \
The inputted password is combined with the retrieved salt and hashed with the same encryption 
process as during sign-up. \
The resulting hash value is compared against the database's hash value. \
If the two are the same, the user is granted access.


## Next steps:
1. ### ~~Persist user data across each new signup~~
    
Done! used json to create a users.txt that serves as the database
   instead of the previous users.py file. for signup, wrote to this
   new users.txt using json.dumps() to create a persistent copy of the
   information, and for login, read from users.txt using json.loads().
   
2. ### ~~Implement hashing~~

Done! I used hashlib in the login_main file as well as the sign_up 
      file. Specifically, I chose sha-256 as the hash function. when 
      registering, the user's password is never stored in the database, and is instead converted into a hash. (although it IS stored in a variable until the next user registers, how does this ultimately affect the security?) when logging in, the user's un-hashed password is hashed, then compared against the hashed value in the database.
      
3. ### ~~Add some salt to it!~~

Done! I added salt via the secrets library, recommended by the documentation for cryptographic use cases. The salt is generated upon registration, and stored alongside the hashed password and salt in the database. During login, the salt value is retrieved from the database, appended to the password, and hashed. This value is then compared against the hashed value from the database, and if it matches, the user is granted access.
   
4. ### ~~Store user data in a database instead of a JSON config~~ 

Done! Used sqlite3 to locally store and retrieve all user data. For posterity, all the JSON logic can be found in the sqlite-and-config branch. 
