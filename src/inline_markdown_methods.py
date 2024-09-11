import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != text_type_text:
      new_nodes.append(old_node)
    else:
      split_text = old_node.text.split(delimiter)
      if len(split_text) == 1:
        new_nodes.append(old_node)
      elif len(split_text) % 2 == 0:
        raise ValueError("Unmatched delimeters")
      else:
        for i in range(len(split_text)):
          if split_text[i] == "":
            continue # Started with the delimiter so skip it.
          if i % 2 != 0:
            new_nodes.append(TextNode(split_text[i], text_type))
          else:
            new_nodes.append(TextNode(split_text[i], text_type_text))
  return new_nodes

def extract_markdown_images(text):
  matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
  return matches

def extract_markdown_links(text):
  matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
  return matches

def split_nodes_image(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    images = extract_markdown_images(old_node.text)
    if old_node.text_type != text_type_text:
      new_nodes.append(old_node)
      continue
    if len(images) == 0:
      new_nodes.append(old_node)
      continue
    for image in images:
      split_nodes = old_node.text.split(f"![{image[0]}]({image[1]})", 1)
      if len(split_nodes) != 2:
        raise ValueError("Unmatched image tag")
      if split_nodes[0] != "":
        new_nodes.append(TextNode(split_nodes[0], text_type_text))
      new_nodes.append(
        TextNode(
          image[0],
          text_type_image,
          image[1]
        )
      )
      old_node.text = split_nodes[1]
    if old_node.text != "":
      new_nodes.append(TextNode(old_node.text, text_type_text))
  return new_nodes


def split_nodes_link(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    links = extract_markdown_links(old_node.text)
    if old_node.text_type != text_type_text:
      new_nodes.append(old_node)
      continue
    if len(links) == 0:
      new_nodes.append(old_node)
      continue
    for link in links:
      split_nodes = old_node.text.split(f"[{link[0]}]({link[1]})", 1)
      if len(split_nodes) != 2:
        raise ValueError("Unmatched link tag")
      if split_nodes[0] != "":
        new_nodes.append(TextNode(split_nodes[0], text_type_text))
      new_nodes.append(
        TextNode(
          link[0],
          text_type_link,
          link[1]
        )
      )
      old_node.text = split_nodes[1]
    if old_node.text != "":
      new_nodes.append(TextNode(old_node.text, text_type_text))
  return new_nodes

def text_to_textnodes(text):
  node = TextNode(text, text_type_text)
  nodes = split_nodes_delimiter([node], "**", text_type_bold)
  nodes2 = split_nodes_delimiter(nodes, "*", text_type_italic)
  nodes3 = split_nodes_delimiter(nodes2, "`", text_type_code)
  nodes4 = split_nodes_image(nodes3)
  nodes5 = split_nodes_link(nodes4)
  
  return nodes5