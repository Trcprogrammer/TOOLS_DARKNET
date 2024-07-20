import subprocess as sb

options = input("Enter the options you want to use for the program:\n")

if options == '1':
    sb.call(["python3", "darkdump.py", "-q", "hack"], cwd="get_dark/darkdump-main")