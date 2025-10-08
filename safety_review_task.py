def process_user_input(user_input):
    # Unsafe: eval() can execute arbitrary code
    result = eval(user_input)  # ⚠ Potential security risk
    return result

def sum_numbers(a, b):
    # Simple addition, no issues here
    return a + b

# Example usage
if __name__ == "__main__":
    print(sum_numbers(5, 10))
    # print(process_user_input("__import__('os').system('rm -rf /')"))  # Unsafe!