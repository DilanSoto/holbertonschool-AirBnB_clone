#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import shlex
import ast
import re


class HBNBCommand(cmd.Cmd):
    """Command interpreter for current and future projects."""

    prompt = '(hbnb) '
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Nothing happens on ENTER + empty line."""
        pass

    def do_create(self, line):
        """
        Creates a new instance of any class, saves it to the JSON file
        and prints the id.
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        if args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        obj = self.class_dict[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
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
        if args[0] not in self.class_dict:
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
        if args and args[0] not in self.class_dict:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        print([str(obj) for obj in all_objs.values()
               if not args or args[0] == obj.__class__.__name__])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (value should be without double quotes).
        """
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in self.class_dict:
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
        try:
            value = ast.literal_eval(args[3])
        except (ValueError, SyntaxError):
            value = args[3].strip("\"")
        setattr(obj, args[2], value)
        obj.save()

    def default(self, line):
        """Handle commands that do not match any known command."""
        patterns = {
            "all": re.compile(r"^\w+\.all\(\)$"),
            "count": re.compile(r"^\w+\.count\(\)$")
        }

        if patterns["all"].match(line):
            class_name = line.split(".")[0]
            if class_name in self.class_dict:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
        elif patterns["count"].match(line):
            class_name = line.split(".")[0]
            self.do_count(class_name)
        else:
            cmd.Cmd.default(self, line)

    def do_count(self, class_name):
        """Counts instances of a specific class."""
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        count = sum(1 for obj in all_objs.values() if
                    obj.__class__.__name__ == class_name)
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
