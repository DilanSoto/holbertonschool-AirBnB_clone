#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Nothing happens on ENTER + empty line"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it to the JSON file and
        prints the id.
        """
        if not line:
            print("** class name missing **")
            return
        try:
            args = shlex.split(line)
            if args[0] != "BaseModel":
                raise NameError
            obj = BaseModel()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representations of all instances based or not on the
        class name.
        """
        args = shlex.split(line)
        if args and args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        print([str(obj) for obj in all_objs.values()
              if not args or args[0] == obj.__class__.__name__])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute.
        """
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        key = f"{args[0]}.{args[1]}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        obj = all_objs[key]
        setattr(obj, args[2], args[3].strip("\""))
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
