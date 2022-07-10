# Authentication-Project
 
This is a toy project to practice different ways to ensure secure login information for a given user. Eventually I'd like to add hashing in the event the "database" is compromised, and even past that, two-factor authentication. In the meantime, it's additional experience building a functioning program, which is always a good thing. 

As I work on it and improve it, the code will be cleaner, but for now I'm focused mostly on development speed, given that I'm the only one working on this and it's just for my own edification. 


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
