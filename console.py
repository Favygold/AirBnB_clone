#!/usr/bin/python3
"""Defines the HBnB Console"""

import cmd
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines HBnB command interpreter"""

    prompt = '(hbnb) '

    __classes = {
        "BaseModel"
    }

    __attributes = {
        "email"
    }

    @staticmethod
    def parse(arg, id=" "):
        """
        Returns a list containing the parsed arguments from the string
        """
        arg_list = arg.split(id)
        list_items = []

        for item in arg_list:
            if item != '':
                list_items.append(item)
        return list_items

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit console"""
        return True

    def emptyline(self):
        """empty line. Do nothing"""
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in HBNBCommand.__classes:
            models.storage.save()
            print(eval(arg)().id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class `name` and `id`
        """
        obj_dict = storage.all()
        arg_lst = HBNBCommand.parse(arg)
        if len(arg_lst) == 0:
            print("** class name missing **")
        elif arg_lst[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_lst) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_lst[0], arg_lst[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_lst[0], arg_lst[1])])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        obj_dict = storage.all()
        arg_lst = HBNBCommand.parse(arg)
        if len(arg_lst) == 0:
            print("** class name missing **")
        elif arg_lst[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_lst) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_lst[0], arg_lst[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del(obj_dict["{}.{}".format(arg_lst[0], arg_lst[1])])
            storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        arg_lst = HBNBCommand.parse(arg)
        if len(arg_lst) > 0 and arg_lst[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(arg_lst) > 0 and arg_lst[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg_lst) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        obj_dict = storage.all()
        arg_lst = HBNBCommand.parse(arg)
        if len(arg_lst) == 0:
            print("** class name missing **")
            return False
        if arg_lst[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_lst) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_lst[0], arg_lst[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_lst) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_lst) == 3:
            try:
                type(eval(arg_lst[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        
        if len(arg_lst) == 4:
            obj = obj_dict["{}.{}".format(arg_lst[0], arg_lst[1])]
            if arg_lst[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_lst[2]])
                obj.__dict__[arg_lst[2]] = valtype(arg_lst[3])
            else:
                obj.__dict__[arg_lst[2]] = arg_lst[3]
        elif type(eval(arg_lst[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_lst[0], arg_lst[1])]
            for key, value in eval(arg_lst[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
