def auth(u, p):
    if u == "admin" and p == "admin123":
        return True
    else:
        return False

def reg_user(u, p):
    users = {}
    users[u] = p
    return users