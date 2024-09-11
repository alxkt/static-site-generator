import os, shutil

from textnode import *
from block_markdown_methods import *


def delete_directory(dir):
  if os.path.exists(dir):
    shutil.rmtree(dir)

def copy_directory(src, dst):
  shutil.copytree(src, dst)

def get_file_contents(path):
  with open(path) as f:
    file_contents = f.read()
  return file_contents

def write_file(path, content):
  with open(path, mode='w') as f:
    f.write(content)

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
  markdown = get_file_contents(from_path)
  template = get_file_contents(template_path)

  html_node = markdown_to_html_node(markdown)
  html = html_node.to_html()

  title = extract_title(markdown)

  html_file = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

  write_file(dest_path, html_file)

def main():
  delete_directory("./public")
  copy_directory("./static", "./public")
  generate_page("./content/index.md", "./template.html", "./public/index.html")

main()
