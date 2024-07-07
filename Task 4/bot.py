def understand_input(user_input):
    user_input = user_input.strip().lower
    command, *args = user_input.split()
    return command, args



