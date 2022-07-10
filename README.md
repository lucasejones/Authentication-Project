# Authentication-Project

**To use this program, run login_main.py.** This will begin a series of prompts, that when 
followed, allow a user to either sign up or log in. If signing up, your name and password will be stored securely in an SQL database. If logging in, your credentials will be compared against that database, and a correct set of credentials will grant you access to the application. 
 
This is a toy project to practice different ways to ensure secure login information for a given user. Eventually I'd like to add two-factor authentication to get experience implementing more strict security practices. In the meantime, I intend to add functionality for successfully logged-in users as well as a UI to facilitate using this program outside the terminal.


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

Done! Used sqlite3 to locally store and retrieve all user data.

5. ### Implement 2-factor authentication

6. ### Create some sort of non-bad UI
   
7. ### Add some actual functionality that's worth having an account and logging in for.
    consider using an api to grab some information and display it in your new UI as one way to achieve this.
