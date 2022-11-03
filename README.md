# PasswordGenerator
Generates a password and stores it in a list
Currently in developement --> v0.1

Current Functionality:
    - User can generate passwords for the "site" of their choosing with 3 different strengths
    - Passwords are saved to a list that can be viewed from within the application

Planned updates:
    - Add a "Delete" button to delete entries
    - Add hashing to generated passwords for security
    - Replace test.txt with encrypted password file
    - Two factor authentication to limit access to password list
    - Ability to send password file to secure server for retrieval on multiple devices
    
Bug Fixes:
    - Removed whitespace issue where whitespace was being added to old passwords when generating new passwords
    - "Sites" are now converted to uppercase to account for case in the "Site" entry box
    - Added spell check to reduce user error when entering a "site"
    - Added more symbols to the random generator and omitted the ":" to avoid conflict with the update_file function
    - Fixed an issue where the spell check popup window would not close
