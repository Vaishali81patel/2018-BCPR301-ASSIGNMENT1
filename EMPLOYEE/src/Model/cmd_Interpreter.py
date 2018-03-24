import cmd
import string, sys
import os
    #  import os Executing a shell command os.system() Get the users environment os.

class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '>>> '
        self.intro = "WELCOME TO THE EMPLOYEE HELP CONSOLE! "

    def do_hello(self, arg):
        print (hello,again, arg)

    def help_hello(self):
        print (hello [message])

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print (terminate)

    # shortcuts
    do_q = do_quit

#
# try it out

cli = CLI()
cli.cmdloop()
