import unittest
from block_markdown_methods import *
class TestBlockMarkdownMethods(unittest.TestCase):
  def test_markdown_to_blocklist(self):
    markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item\n"
    blocklist = markdown_to_block(markdown)
    self.assertEqual(blocklist[0],"# This is a heading")
    self.assertEqual(blocklist[1],"This is a paragraph of text. It has some **bold** and *italic* words inside of it.")
    self.assertEqual(blocklist[2],"* This is the first list item in a list block\n* This is a list item\n* This is another list item")

  def test_excess_line_breaks(self):
    markdown = "   Also too much whitespace.   \n\n\n Alright.... "
    blocklist = markdown_to_block(markdown)
    self.assertEqual(blocklist[0], "Also too much whitespace.")
    self.assertEqual(blocklist[1], "Alright....")

  def test_heading(self):
    block = "# Basic Heading"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_heading)

  def test_another_heading(self):
    block = "### Three Heading"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_heading)
  
  def test_last_heading(self):
    block = "###### Six Heading"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_heading)

  def test_code_block(self):
    block = "```\ncode_string = 'hello world'\n```"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_code)

  def test_quote_block(self):
    block = ">HEre is a quote block\n>-Albert Einstein"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_quote)

  def test_unordered_list(self):
    block = "* HEre is a list block\n* item two"
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_unordered_list)
  
  def test_ordered_list(self):
    block = "1. HEre is a list block\n2. item two\n3. Third item."
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_ordered_list)

  def test_paragraph(self):
    block = "Here is just a paragraph block.\nIt has two lines *and some italics*."
    block_type = block_to_block_type(block)
    self.assertEqual(block_type, block_type_paragraph)

  def test_markdown_to_html_node_simplest_case(self):
    markdown = "Hello world."
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><p>Hello world.</p></div>")

  def test_markdown_to_html_node_single_node(self):
    markdown = "Here is **some** text."
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><p>Here is <b>some</b> text.</p></div>")


  def test_markdown_to_html_node_multiple_nodes(self):
    markdown = "One paragraph.\n\nAnd a *second* paragraph."
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><p>One paragraph.</p><p>And a <i>second</i> paragraph.</p></div>")

  def test_markdown_to_html_node(self):
    markdown = "Here is some text and it is **bold** and\n\n```\ndef taco()\n```\n\n>cool I guess"
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><p>Here is some text and it is <b>bold</b> and</p><pre><code>def taco()</code></pre><blockquote>cool I guess</blockquote></div>")

  def test_markdown_to_html_quote(self):
    markdown = ">I have a blockquote here.\n>It has multiple lines."
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><blockquote>I have a blockquote here. It has multiple lines.</blockquote></div>")

  def test_markdown_to_html_quote_two(self):
    markdown = "> All that is gold does not glitter"
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><blockquote>All that is gold does not glitter</blockquote></div>")

  def test_markdown_to_html_unordered_list(self):
    markdown = "* Item one.\n* Item two\n* Item three."
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><ul><li>Item one.</li><li>Item two</li><li>Item three.</li></ul></div>")

  def test_markdown_to_html_unordered_list_two(self):
    markdown = "* Disney *didn't ruin it*"
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><ul><li>Disney <i>didn't ruin it</i></li></ul></div>")

  def test_markdown_to_html_ordered_list(self):
    markdown = "1. First item.\n2. Second item.\n3. fourth itemmm"
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><ol><li>First item.</li><li>Second item.</li><li>fourth itemmm</li></ol></div>")

  def test_markdown_to_html_heading(self):
    markdown = "# Heading 1"
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><h1>Heading 1</h1></div>")

  def test_markdown_to_html_heading6(self):
    markdown = "###### Heading 6"
    html_node = markdown_to_html_node(markdown)
    self.assertEqual(html_node.to_html(), "<div><h6>Heading 6</h6></div>")

  def test_extract_title(self):
    markdown = "# My Title\n\nSome text."
    title = extract_title(markdown)
    self.assertEqual(title, "My Title")