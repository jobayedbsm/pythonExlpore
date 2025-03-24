class UserAuth:
    def __init__(self):
        self.users = {"jobayed": "securepassword"}  # Sample user database

    def login(self, username, password):
        """Validate user login credentials."""
        if username in self.users and self.users[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password.")

    def register(self, username, password):
        """Register a new user - To be implemented."""
        pass  # Future implementation for adding users

    def reset_password(self, username):
        """Reset user password - To be implemented."""
        pass  # Future password reset logic

# Usage
auth = UserAuth()
auth.login("jobayed", "securepassword")  # ✅ Login successful!
auth.register("newuser", "newpass")      # Currently does nothing
