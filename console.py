#!/usr/bin/python3
"""Defines HBNBCommand"""

import cmd
from models import storage
from models.base_model import BaseModel


classes = ['BaseModel']
class HBNBCommand(cmd.Cmd):
    '''Command interpreter for my HBNB
    '''
    prompt = ('(hbnb) ')

    def do_create(self, class_name):
        """Creates a new instance of BaseModel
        """
        if not class_name:
            print("** class name missing **")
        elif class_name not in classes:
            print("** class doesn't exist **")
        else:
            new_model = eval(class_name + '()')
            print(new_model.id)
            new_model.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        for key, value in all_objs.items():
            obj_name = value.__class__.__name__
            obj_id = value.id
            if obj_name == args[0] and obj_id == args[1]:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an object
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif args == 1:
            print("** instance id missing **")
            return
        all_objs = storage.all()
        name = args[0] + '.' + args[1]
        for key, value in all_objs.items():
            if key == name:
                del(all_objs[name])
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, class_name):
        """Prints str repr"""
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all().values()
        lists = []
        for value in all_objs:
            if value.__class__.__name__ == class_name:
                lists.append(value.__str__())
        print(lists)

    def do_update(self, arg):
        """Update the value of an instance
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        all_objs = storage.all().values()

        for key in all_objs:
            if key.id == args[1]:
                setattr(key, args[2], args[3])
                return
        storage.save()

    def do_EOF(self, line):
        """Exiting the program
        """
        print()
        return True

    def emptyline(self):
        """Prevents the previous command from been executed
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
