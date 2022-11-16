#!/usr/bin/env python3

#import additional code to complete our task
import shutil
import os

def main():
    """cide to move files around"""
#move ino the working folder
os.chdir("/home/student/mycode/")
#copy file to fileb

shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy entire directoryA to the directoryB)
os.system("rm -rf /home/student/mycode/5g_research/sdn_network.txt.copy")
shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__:
    main()



