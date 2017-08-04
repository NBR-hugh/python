# -*- coding:utf-8 -*-

# BE 00

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

print "So,you're %r old,%r tall and %r heavy." % (
        age,height,weight)

# DK
# 01 pydoc raw_input
    # -->    raw_input([prompt]) -> string
        
    #   Read a string from standard input.  The trailing newline is stripped.
    #   If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    #   On Unix, GNU readline is used if enabled.  The prompt string, if given,
    #   is printed without a trailing newline before reading.

# 03 pydoc 是做什么的?
   #  Documentation generator and online help system 文档生成器与在线帮助系统

# 04 使用 pydoc 看一下 open,file,os 与 sys,记下有趣的知识点
    # open(name[, mode[, buffering]]) -> file object
    # file(name[, mode[, buffering]]) -> file object
    # Programs that import and use 'os' stand a better chance of being
        #portable between different platforms.  Of course, they must then
        #only use functions that are defined by all platforms (e.g., unlink
        #and opendir), and leave all pathname manipulation to os.path
        #(e.g., split and join).(操作系统相关的模块)
    #  module "sys" provides access to some objects used or maintained by the
        #interpreter and to functions that interact strongly with the interpreter.(与解释器相关的模块)
