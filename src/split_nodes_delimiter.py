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