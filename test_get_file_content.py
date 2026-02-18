from functions.get_file_content import get_file_content

print(get_file_content("calculator", "lorem.txt"))
print("========================================")
print(get_file_content("calculator", "main.py"))
print("========================================")
print(get_file_content("calculator", "pkg/calculator.py"))
print("========================================")
print(get_file_content("calculator", "/bin/cat")) # this should return an error string
print("========================================")
print(get_file_content("calculator", "pkg/does_not_exist.py")) # this should return an error string
