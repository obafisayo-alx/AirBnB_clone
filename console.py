#!/usr/bin/python3
"""module of console containing entry point of command interpreter"""

import cmd
import shlex
import ast 
import re
from models.user import User
from models.base_model import BaseMOdel
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
from models import storage


def split_curly_braces(e_arg):
    """split curly braces for update model"""
    curly_braces = re.search(r"\{(.*?)\}", e_arg)
    
    if curly_braces:
        id_with_comma = shlex.splite(e_arg[:curly_braces.span()[0]])
        id = [x.strip(",") for x in id_with_comma][0]

        str_data = curly_braces.group(1)
        try:
            arg_dict = ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("** invalid dictionary format **")
            return
        return id, arg_dict
    else:
        commands = e_arg.split(",")
        if commands:
            try:
                id = commands[0]
            except Exception:
                return "", ""
            try:
                attr_name = commands[1]
            except Exception:
                return id, ""
            try:
                attr_val = commands[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_val}"


class HBNBCommand(cmd.Cmd):
    """HBNBCommand console"""

    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Review", "Amenity",
            "State", "Place" "City"]

    def emptyline(self):
        """when an empty line is entered, take no action"""

        pass

    def do_EOF(self, arg):
        """use EOF(Ctrl+D) key to end the application"""

        return True

    def do_quit(self, arg):
        """To end te program,use the Quit commad"""

        return True

    def do_ceate(self, arg):
        """Make a fresh BaseModel instance and store it in the JSON
           file Usa: Create <class_name>"""

           commands = shlex.split(arg)

           if len(commands) == 0:
               print("** class name missing **")
           elif commands[0] not in self.valid_classes:
               print("** class doesn't exist **")
           else:
               new_instance = eval(f"{commands[0]}()")
               storage.save()
               print(new_istance.id)
    def do_show(self, arg):
        """Display instance's string representation,
           Use:show<class_name><id>"""

        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
              print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
    def do_destroy(self, arg):
        """On the basis of class name and id, delete an instance.
           Use:destroy <class_name><id>"""

           commands = shlex.split(arg)

           if len(commands) == 0:
               print("** class name missing **")
           elif commands[0] not in self.valid_classes:
                print("** class doesn't exist **")
           elif len(command) < 2:
               print("** instance id missing **")
           else:
               objects = storage.all()
               key = "{}.{}".format (commands[0], commands[1])
               if key in objects:
                   print(objects[key])
                   storage.save()
               else:
                   print("** no instace found **")
    def do_all(self, arg):
        """print every instance or a selected class string representation.
           Use:<User>.all() <User>.show()"""

           objects = storage.all()

           commands = shlex.split(arg)

           if len(commands) == 0:
               for key, val in objects.items():
                   print(str(val))
           elif  commands[0] not in self.valid_classes:
                print("** class doesn't exist **")
           else:
               for key, val in objects.items():
                   if key.split(".")[0] == commands[0]:
                       print(str(val))
    
    def do_count(self, arg):
        """The function<class_name> counts and gets the number of instances of s class"""

        objects = storage.all()

        commands = shlex.split(arg)

        if arg:
            cls_nam = commands[0]

        count = 0

        if commands:
            if cls_nam in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__ == cls_nam:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def d_update(self, arg):
        """Add or modify an attribute to update an instance. update<class_name><id><attribute_name>"<attribute_value>" """

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()


            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                curly_braces = re.search(r"\{{.*?)\}", arg)

                if curly_braces:
                    try:
                        str_data = curly_braces.ground(1)

                        arg_dict = ast.literal_eval("{" + str_data + "}")

                        attribute_names = list(arg_dict.keys())
                        attribute_values = list(arg_dict.values())
                        try:
                            attr_nam1 = attribute_names[0]
                            attr_val1 = attribute_values[0]
                            setattr(obj, attr_nam1, attr_val1)
                        except Exception:
                            pass
                        try:
                            attr_nam2 = attribute_names[1]
                            attr_val2 = attribute_values[1]
                            setattr(obj, attr_nam2, attr_val2)
                        except Exception:
                            pass
                    except Exception:
                        pass
                else:

                    attr_nam = commands[2]
                    attr_val = commands{3}

                    try:
                        attr_val = eval(attr_val)
                    except Exception:
                        pass
                    setattr(obj, attr_nam, attr_val)

                obj.save()


    def default(self, arg):
        """The cmd module default action when input is deemed invalid"""

        arg_list = arg.split(".")

        cls_nam = arg_list[0] # incoming command method

        command = arg.list[1].split(")")[0] # extra arguments

        method_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "count": self.do_count
                }

        if cmd_met in method_dict.keys():
            if cmd_met != "update":
                return method_dict[cmd_met]("{} {}".format(cls_nam, e_arg))
            else:
                if not cls_nam:
                    print("** class name missing **")
                    return
                try:
                    obj_id, arg_dict = split_curly_braces(e_arg)
                except Exception:
                    pass
                try:
                    call = method_dict[cmd_met]
                    return call("{} {}".format(cls_nam, obj_id, arg_dict))
                except Exception:
                    pass
            else:
                print("*** Uknown syntax: {}".format(arg))
                return False



    if __name__ == '__main__':
    HBNBCommand().cmdloop(
