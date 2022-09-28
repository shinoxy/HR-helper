from functions import *


print("Print your list of requirements:")
requirements_list = (re.sub(r'[^A-Za-z ]', '', input().lower())).split()

list_of_candidates = []
default_path = Path(Path.home(), "Desktop")

print("Import data from file or enter manually? 1/2")
mode = input()
if mode == '1':
    mode_1(list_of_candidates, requirements_list, default_path)
elif mode == '2':
    mode_2(list_of_candidates, requirements_list)
else:
    print("Error")
