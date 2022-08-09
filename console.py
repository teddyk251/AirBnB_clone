#!/usr/bin/python3
"""
Consolof of AirBnB clone
"""

import cmd

from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    the cmd class
    """

    prompt = '(hbnb) '
    the__Classes = {
        BaseModel.__name__: BaseModel,
        User.__name__: User,
        State.__name__: State,
        City.__name__: City,
        Place.__name__: Place,
        Amenity.__name__: Amenity,
        Review.__name__: Review
    }
    __class_funcs = ["all", "count", "show", "destroy", "update"]

    @staticmethod
    def extract(arg, id=" "):
        """
        Returns a list of arg
        """

        the__arguments = arg.split(id)
        clean_arguments = []

        for x in the__arguments:
            if x != '':
                clean_arguments.append(x)
        return clean_arguments

    def do_quit(self, arg):
        """quit"""

        return True

    def help_quit(self):
        """Prints help for quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Exits"""

        print("")
        return True

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
        """

        argus = HBNBCommand.extract(arg)
        if len(argus) == 0:
            print("** class name missing **")
            return False

        if len(argus) > 1:
            print("** to many arguments **")
            return False

        if (argus[0] in HBNBCommand.the__Classes.keys()):
            new_obj = HBNBCommand.the__Classes[argus[0]]()
            new_obj.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """
            prints Help info for creating function
        """
        print("""Creats a new instance of the first argument
              stores it in the JSON file and prints its id""")

    def do_show(self, arg):
        """
            Prints the string representation of an instance based
            on the class name and id.
        """
        argus = HBNBCommand.extract(arg)
        db = storage.all()
        if not len(argus):
            print("** class name missing **")
        elif (argus[0] not in HBNBCommand.the__Classes.keys()):
            print("** class doesn't exist **")
        elif len(argus) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argus[0], argus[1]) not in db:
            print("** no instance found **")
        else:
            print(db["{}.{}".format(argus[0], argus[1])])

        # Extra case
        # elif len(argus) > 2:
        #    print("** to many arguments **")

    def help_show(self):
        """
            Prints Help
        """
        print("""Prints the string representation of an instance based
            on the class name and id.
                Ex: $ show BaseModel 1234-1234-1234
            """)

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file).
        """
        argus = HBNBCommand.extract(arg)
        storage.reload()
        db = storage.all()
        if not len(argus):
            print("** class name missing **")
        elif (argus[0] not in HBNBCommand.the__Classes.keys()):
            print("** class doesn't exist **")
        elif len(argus) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argus[0], argus[1]) not in db:
            print("** no instance found **")
        else:
            # print(storage.__class__.__name__.__objects)
            del db["{}.{}".format(argus[0], argus[1])]
            storage.save()

    def help_destroy(self):
        """
            Prints Help for destroy function
        """
        print("""Deletes an instance based on the class name and id
              (save the change into the JSON file).
                Ex: $ destroy BaseModel 1234-1234-1234""")

    def do_all(self, arg):
        """
            Prints all string of instances based or
            not on the class name.
        """
        the__arguments = HBNBCommand.extract(arg)
        if len(the__arguments) > 0 and the__arguments[0] not in HBNBCommand.the__Classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(the__arguments) > 0 and the__arguments[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(the__arguments) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def help_all(self):
        """
            prints help for all function
        """
        print("""Prints all string representation of all instances based or
            not on the class name.
                Ex: $ all BaseModel or $ all""")

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234 email
                      "aibnb@holbertonschool.com"
        """
        the__arguments = HBNBCommand.extract(arg)
        objdict = storage.all()

        if len(the__arguments) == 0:
            print("** class name missing **")
            return False
        if the__arguments[0] not in HBNBCommand.the__Classes:
            print("** class doesn't exist **")
            return False
        if len(the__arguments) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(the__arguments[0], the__arguments[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(the__arguments) == 2:
            print("** attribute name missing **")
            return False
        if len(the__arguments) == 3:
            try:
                type(eval(the__arguments[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(the__arguments) == 4:
            obj = objdict["{}.{}".format(the__arguments[0], the__arguments[1])]
            if the__arguments[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[the__arguments[2]])
                obj.__dict__[the__arguments[2]] = valtype(the__arguments[3])
            else:
                obj.__dict__[the__arguments[2]] = the__arguments[3]
        elif type(eval(the__arguments[2])) == dict:
            obj = objdict["{}.{}".format(the__arguments[0], the__arguments[1])]
            for k, v in eval(the__arguments[2]).items():
                if (k in obj.__class__.__dict__.keys() and type(
                        obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def help_update(self):
        """
            prints Help for the update function
        """
        print(
            """Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
                Ex: $ update BaseModel 1234-1234-1234
                      email "aibnb@holbertonschool.com""")

    def emptyline(self):
        """
            Do nothing if Empty line + enter is inserted.
        """
        pass

    def do_count(self, arg):
        """
            Prnits the number of elements inside the FileStorage that
            are of instances of cls
        """
        the__arguments = HBNBCommand.extract(arg)
        if len(the__arguments) > 0 and the__arguments[0] not in HBNBCommand.the__Classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(the__arguments) > 0 and the__arguments[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(the__arguments) == 0:
                    objl.append(obj.__str__())
            print(len(objl))

    def show(self, cls):
        """
            Gives all elements inside FileStorage that
            are of instances of cls
        """
        pass

    def destroy(self, cls):
        """
            Gives all elements inside FileStorage that
            are of instances of cls
        """
        pass

    def update(self, cls):
        """
            Gives all elements inside FileStorage that
            are of instances of cls
        """
        pass

    def default(self, line):
        """
            Handles case where the command has no equivlaent
            do_ method
        """

        line_p = HBNBCommand.extract(line, '.')
        if line_p[0] in HBNBCommand.the__Classes.keys() and len(line_p) > 1:
            if line_p[1][:-2] in HBNBCommand.__class_funcs:
                func = line_p[1][:-2]
                cls = HBNBCommand.the__Classes[line_p[0]]
                eval("self.do_" + func)(cls.__name__)
            else:
                print("** class doesn't exist **")
        else:
            super().default(line)
        return False


if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop()

