import os, shutil

from textnode import *

def delete_directory(dir):
  if os.path.exists(dir):
    shutil.rmtree(dir)

def copy_directory(src, dst):
  shutil.copytree(src, dst)

def main():
  delete_directory("./public")
  copy_directory("./static", "./public")

main()
