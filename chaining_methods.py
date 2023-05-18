# Assignment: User
# For this assignment you will create the user class and add a couple methods!

class User:

    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    # Attributes:
    # On instantiation of a user, the following attributes should be passed in as arguments:

    # first_name
    # last_name
    # email
    # age
    # Also include default attributes:

    # is_rewards_member - default value of False
    # gold_card_points = 0


    # Methods:
    # display_info(self) - Have this method print all of the users' details on separate lines.

    def display_info(self):
        print("--------------------------------------")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("--------------------------------------")

        return self # method must return self in order to chain


    # spend_points(self, amount) - have this method decrease the user's points by the amount specified.

    def spend_points(self, amount):

    # Add logic in the spend points method
    # to be sure they have enough points to
    # spend that amount and handle appropriately.

        if (self.gold_card_points) < amount:
            print("\n","ATTENTION!","\n","***Member has Insufficient Points***","\n")
            return self # method must return self in order to chain
                # exit function!

        # decrease the user's points by the amount specified.
        self.gold_card_points -= amount

        return self # method must return self in order to chain

    def enroll(self):

        # Add logic in the enroll method to check if
        # they are a member already, and if they are,
        # print "User already a member." and return False, otherwise return True.

        if self.is_rewards_member:
            print("User already a member.")
            return self # method must return self in order to chain

        # Have this method change the user's member
        # status to True and
        self.is_rewards_member = True

        # set their gold card points to 200.
        self.gold_card_points = 200

        return self # method must return self in order to chain


# User 1 -----
print("\n")
print("User 1: ")
my_user = User("James", "Williams", "jbrandonw88@gmail.com", 35)
my_user.display_info().spend_points(50).enroll().spend_points(50).display_info() #chained

# User 2 -----
print("User 2: ")
user2 = User("Shakira", "Sampson", "shakirasampson94@gmail.com", 30)
user2.enroll().spend_points(80).display_info() #chained

# User 3 -----
print("User 3: ")
user3 = User("Sara", "Amato", "sara_amato89@gmail.com", 33)
user3.spend_points(40).display_info() #chained