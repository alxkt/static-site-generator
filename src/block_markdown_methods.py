from inline_markdown_methods import text_to_textnodes
from textnode import *
from htmlnode import *

block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"
block_type_paragraph = "paragraph"

def markdown_to_block(markdown):
  block_list = markdown.split("\n\n")
  new_block = []
  for block in block_list:
    if block != "\n":
      new_block.append(block.strip(" \n"))
  return new_block

def block_to_block_type(block):
  if block.startswith("# "): return block_type_heading
  if block.startswith("## "): return block_type_heading
  if block.startswith("### "): return block_type_heading
  if block.startswith("#### "): return block_type_heading
  if block.startswith("##### "): return block_type_heading
  if block.startswith("###### "): return block_type_heading

  if block.startswith("```") and block.endswith("```"): return block_type_code

  lines = block.split("\n")
  quote = True
  for line in lines:
    if not line.startswith(">"): quote = False
  if quote: return block_type_quote
  
  unordered_list = True
  for line in lines:
    if not (line.startswith("* ") or line.startswith("- ")):
      unordered_list = False
  if unordered_list: return block_type_unordered_list

  ordered_list = True
  for i, line in enumerate(lines):
    if not line.startswith(f"{i+1}. "): ordered_list = False
  if ordered_list: return block_type_ordered_list

  return block_type_paragraph

def markdown_to_html_node(markdown):
  blocks = markdown_to_block(markdown)
  block_nodes = []
  for block in blocks:
    block_type = block_to_block_type(block)
    match block_type:
      case "paragraph":
        text_nodes = text_to_textnodes(block)
        leaf_nodes = []
        for text_node in text_nodes:
          html_node = text_node_to_html_node(text_node)
          leaf_nodes.append(html_node)
        node = ParentNode("p", leaf_nodes)
        # full = ParentNode("div", [node])
        # print(full.to_html())
        block_nodes.append(node)
      case "code":
        print("HOT HERE")
      case "quote":
        print("QUOTE")
      case _:
        raise Exception("Failed to determine block type. (This is not possible)")
  wrapped = ParentNode("div", block_nodes)
  return wrapped