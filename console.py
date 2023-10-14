#!/usr/bin/env python3
"""A program that contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains methods to manipulate other classes"""
    prompt = "(hbnb) "
    # update the all_classes as new classes are added
    all_classes = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        print(end="")

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        args = line.split()
        if len(args) != 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        model_class = globals().get(args[0])
        new_instance = model_class()
        print(new_instance.id)
        new_instance.save()

    def do_show(self, line):
        """Prints the string representation of an instance
            based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        all_obj = storage.all()
        if all_obj:
            for key, value in all_obj.items():
                class_name, class_id = key.split(".")
                if class_name == args[0] and class_id == args[1]:
                    print(value)
                    return
        print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
            (save the change into the JSON file)
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        all_obj = storage.all()
        if all_obj:
            for key, value in all_obj.items():
                class_name, class_id = key.split(".")
                if class_name == args[0] and class_id == args[1]:
                    del all_obj[key]
                    storage.save()
                    return
        print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
            based or not on the class name
        """
        args = line.split()
        try:
            if args[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return
        except IndexError:
            pass
        all_obj = storage.all()
        if all_obj:
            if len(args) == 1:
                for key, value in all_obj.items():
                    class_name, class_id = key.split(".")
                    if class_name == line:
                        print(value)
            else:
                for value in all_obj.values():
                    print(value)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
            or updating attribute (save the change into the JSON file)
        """
        args = line.split()
        if len(args) != 4:
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            return
        all_obj = storage.all()
        if all_obj:
            for key, value in all_obj.items():
                class_name, class_id = key.split(".")
                if class_name == args[0] and class_id == args[1]:
                    setattr(value, args[2], args[3])
                    value.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
