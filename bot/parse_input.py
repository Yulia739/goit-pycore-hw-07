def parse_input(user_input):
    """Parses the string entered by the user into a command and its arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
