#!/usr/bin/python3
"""Defines HBNBCommand"""
import cmd


class HBNBCommand(cmd.Cmd):
    '''Command interpreter for my HBNB'''
    prompt = ('(hbnb) ')

    def do_EOF(self, line):
        """Exiting the program"""
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
