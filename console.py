#!/usr/bin/env python3
"""module of console containing entry point of command interpreter"""

import cmd
import shlex
import re
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""

    prompt = "(hbnb) "
    __valid_args = {"BaseModel",
                    "User", "Review", "Amenity", "State", "Place", "City"}

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__valid_args:
            print("** class doesn't exist **")
            return
        new_instance = eval(f"{class_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__valid_args:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        object_id = args[1]
        key = f"{class_name}.{object_id}"
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__valid_args:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        object_id = args[1]
        key = f"{class_name}.{object_id}"
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__valid_args:
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objects.items()
               if key.split('.')[0] == class_name])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__valid_args:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        object_id = args[1]
        key = f"{class_name}.{object_id}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]
        instance = objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
