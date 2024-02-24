import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()  # Print a newline for better formatting
        return True

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
