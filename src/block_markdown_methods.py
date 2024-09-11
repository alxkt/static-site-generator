import re
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

def determine_heading_tag(block):
  if block.startswith("# "): return "h1"
  if block.startswith("## "): return "h2"
  if block.startswith("### "): return "h3"
  if block.startswith("#### "): return "h4"
  if block.startswith("##### "): return "h5"
  if block.startswith("###### "): return "h6"

def block_to_leafnodes(block):
  text_nodes = text_to_textnodes(block)
  leaf_nodes = []
  for text_node in text_nodes:
    html_node = text_node_to_html_node(text_node)
    leaf_nodes.append(html_node)
  return leaf_nodes

def markdown_to_html_node(markdown):
  blocks = markdown_to_block(markdown)
  block_nodes = []
  for block in blocks:
    block_type = block_to_block_type(block)
    match block_type:
      case "paragraph":
        leaf_nodes = block_to_leafnodes(block)
        node = ParentNode("p", leaf_nodes)
        block_nodes.append(node)
      case "code":
        cleaned_block = block.strip("```")
        cleaned2_block = cleaned_block.strip("\n")
        leaf_nodes = block_to_leafnodes(cleaned2_block)
        node = ParentNode("code", leaf_nodes)
        node2 = ParentNode("pre", [node])
        block_nodes.append(node2)
      case "quote":
        cleaned_block = block.split("\n")
        cleaned_block2 = []
        for b in cleaned_block:
          cleaned_block2.append(b.lstrip("> "))
        cleaned_block3 = " ".join(cleaned_block2)
        leaf_nodes = block_to_leafnodes(cleaned_block3)
        node = ParentNode("blockquote", leaf_nodes)
        block_nodes.append(node)
      case "unordered list":
        cleaned_block = block.split("\n")
        cleaned_block2 = []
        for b in cleaned_block:
          if b.startswith("* "): cleaned_block2.append(b.lstrip("* "))
          elif b.startswith("- "): cleaned_block2.append(b.lstrip("- "))
          else: raise Exception("Assert: Improper unordered list not possible")
        node = ParentNode("ul", [])
        for clean_block in cleaned_block2:
          leaf_nodes = block_to_leafnodes(clean_block)
          pare = ParentNode("li", leaf_nodes)
          node.children.append(pare)
        block_nodes.append(node)
      case "ordered list":
        cleaned_block = block.split("\n")
        cleaned_block2 = []
        for i, b in enumerate(cleaned_block):
          cleaned_block2.append(b.lstrip(f"{i+1}. "))
        node = ParentNode("ol", [])
        for clean_block in cleaned_block2:
          leaf_nodes = block_to_leafnodes(clean_block)
          pare = ParentNode("li", leaf_nodes)
          node.children.append(pare)
        block_nodes.append(node)
      case "heading":
        heading_tag = determine_heading_tag(block)
        cleaned_block = block.lstrip("# ")
        leaf_nodes = block_to_leafnodes(cleaned_block)
        node = ParentNode(heading_tag, leaf_nodes)
        block_nodes.append(node)
      case _:
        raise Exception("Failed to determine block type. (This is not possible)")
  wrapped = ParentNode("div", block_nodes)
  return wrapped

def extract_title(markdown):
  x = re.search("^# .+", markdown)
  title = x.group().lstrip("# ")
  return title