class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group is None:
        return False
    #Check user is in list user of current group or not
    users = group.get_users()
    for u in users:
        if user==u:
            return True
    
    #Use recursion to check all sub group
    #If one of groups is True-> stop and return
    for g in group.get_groups():
        if is_user_in_group(user,g):
            return True 
    return False


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1 - Normal case
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child_user2 = "sub_child_user22"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
child.add_user("User 1")
child.add_user("User 2")
parent.add_group(child)
if not is_user_in_group(sub_child_user,parent):
    raise SystemExit("Test case 1 failed")
print("Test case 1 passed")

# Test Case 2 - Not found in group
parent2 = Group("parent")
child2 = Group("child")
sub_child2 = Group("subchild")

sub_child_user22 = "sub_child_user"
sub_child2.add_user(sub_child_user)

child2.add_group(sub_child2)
parent2.add_group(child2)

if is_user_in_group("ABCXYZ",parent2):
    raise SystemExit("Test case 2 failed")
print("Test case 2 passed")

# Test Case 3 - Input None

if is_user_in_group("ABCXYZ",None):
    raise SystemExit("Test case 3 failed")
print("Test case 3 passed")

# Test Case 4 - Empty group
parent4 = Group("parent")

if is_user_in_group("parent",parent4):
    raise SystemExit("Test case 4 failed")
print("Test case 4 passed")