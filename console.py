#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    '''Command interpreter for my HBNB'''
    prompt = ('(hbnb) ')

    def do_EOF(self, line):
        print()
        return True

    def emptyline(self):
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()

