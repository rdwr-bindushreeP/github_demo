def process_input(user_input):
    # BAD: This executes arbitrary code
    result = eval(user_input)
    return result

def write_file(data):
    f = open("data.txt", "w")
    f.write(data)
    # File not closed properly — potential resource leak