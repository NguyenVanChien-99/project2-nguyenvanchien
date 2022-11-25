import os
from re import S

### Explain:
# Check the path is a file with suffix equal to the suffix we put then return this path
# If the path is a file with suffix not equal to the suffix we put then we return an empty list
# If the path is a dir , we get all sub dirs and use recursion to check sub dir find_files(suffix, sub_dir_path)

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if suffix is None or suffix =="" or path is None or path =="" or len(suffix)>= len(path):
        return []
    out = []
    if os.path.isfile(path) and path[len(path)-len(suffix):len(path)]==suffix:
        return [path]
    if not os.path.isdir(path):
        return []

    sub_dir = os.listdir(path)
    for sub in sub_dir:
        out += find_files(suffix,path+"/"+sub)
    return out


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
if find_files(".c", "./prob2")==['./prob2/subdir1/a.c', './prob2/subdir3/subsubdir1/b.c', './prob2/subdir5/a.c', './prob2/t1.c']:
    print("Test case 1 passed")
else:
    print("Test case 1 failed")
# Test Case 2
# not found
if find_files(".abcxyz", "./prob2")==[]:
    print("Test case 2 passed")
else:
    print("Test case 2 failed")
# Test Case 3
if find_files("", None)==[]:
    print("Test case 3 passed")
else:
    print("Test case 3 failed")
