import sys

def reverse(inputpath, outputpath):
    try:
        with open(inputpath, mode='r', encoding='utf-8') as inputfile:
            content = inputfile.read()

        reversed = content[::-1]

        with open(outputpath, mode='w', encoding='utf-8') as outputfile:
            outputfile.write(reversed)

        print(f"Successfully reversed {inputpath} and saved to {outputpath}.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def copy(inputpath, outputpath):
    try:
        with open(inputpath, mode='r', encoding='utf-8') as inputfile:
            content = inputfile.read()

        with open(outputpath, mode='w', encoding='utf-8') as outputfile:
            outputfile.write(content)

        print(f"Successfully copied {inputpath} to {outputpath}.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def duplicate(inputpath, n):
    try:
        duplicate_times = int(n)
        if duplicate_times <= 0:
            raise Exception
    except:
        print("Error: n must be a positive integer.")
        sys.exit(1)

    try:
        with open(inputpath, mode='r', encoding='utf-8') as inputfile:
            content = inputfile.read()

        with open(inputpath, mode='w', encoding='utf-8') as outputfile:
            outputfile.write(content * duplicate_times)

        print(f"Successfully duplicated contents of {inputpath} {duplicate_times} times")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def replace(inputpath, needle, newstring):
    try:
        with open(inputpath, mode='r', encoding='utf-8') as inputfile:
            content = inputfile.read()

        replaced_content = content.replace(needle, newstring)

        with open(inputpath, mode='w', encoding='utf-8') as outputfile:
            outputfile.write(replaced_content)
        
        print(f"Successfully replaced {needle} with {newstring} in {inputpath}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def print_error():
    print("Error: No command provided.")
    print("Supported command:")
    print("python3 file_manipulator.py reverse inputpath outputpath")
    print("python3 file_manipulator.py copy inputpath outputpath")
    print("python3 file_manipulator.py duplicate-contents inputpath n")
    print("python3 file_manipulator.py replace-string inputpath needle newstring")
    sys.exit(1)


commands = sys.argv
if len(commands) != 4 and len(commands) != 5:
    print_error()


command = commands[1]
if command == "reverse":
    reverse(commands[2], commands[3])
elif command == "copy":
    copy(commands[2], commands[3])
elif command == "duplicate-contents":
    duplicate(commands[2], commands[3])
elif command == "replace-string":
    replace(commands[2], commands[3], commands[4])
else:
    print_error()
