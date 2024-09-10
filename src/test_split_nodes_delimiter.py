import unittest
from textnode import *
from split_nodes_delimiter import split_nodes_delimiter
from htmlnode import LeafNode

class TestSplitNodesDelimiter(unittest.TestCase):
  def test_basic(self):
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")

    self.assertEqual(new_nodes[0], TextNode("This is text with a ", "text"))
    self.assertEqual(new_nodes[1], TextNode("code block", "code"))
    self.assertEqual(new_nodes[2], TextNode(" word", "text"))

  def test_text_no_delimiter_found(self):
    node = TextNode("There is no delimiter in here", "text")
    new_nodes = split_nodes_delimiter([node], "*", text_type_italic)

    self.assertEqual(new_nodes, [node])

  def test_not_text_type_node(self):
    node = TextNode("Some image", "image", "https://google.com/image.jpg")
    new_nodes = split_nodes_delimiter([node], "**", "bold")
    self.assertEqual(new_nodes, [node])
  
  def test_multiple_delimiter_pairs(self):
    node = TextNode("Here is **text** where I bolded **multiple** things.", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", "bold")
    self.assertEqual(new_nodes[0], TextNode("Here is ", text_type_text))
    self.assertEqual(new_nodes[1], TextNode("text", text_type_bold))
    self.assertEqual(new_nodes[2], TextNode(" where I bolded ", text_type_text))
    self.assertEqual(new_nodes[3], TextNode("multiple", text_type_bold))
    self.assertEqual(new_nodes[4], TextNode(" things.", text_type_text))

  def test_starts_with_delimiter(self):
    node = TextNode("*The beginning of this sentence* is italic.", text_type_text)
    new_nodes = split_nodes_delimiter([node], "*", "italic")
    self.assertEqual(new_nodes[0], TextNode("The beginning of this sentence", text_type_italic))
    self.assertEqual(new_nodes[1], TextNode(" is italic.", text_type_text))

  def test_text_ends_with_delimiter(self):
    node = TextNode("This one ends *with the delimiter*", text_type_text)
    new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
    self.assertEqual(new_nodes[0], TextNode("This one ends ", text_type_text))
    self.assertEqual(new_nodes[1], TextNode("with the delimiter", text_type_italic))

  def test_italic_and_bold(self):
    # only works if we do bold BEFORE italic
    node = TextNode("Here we have some *italic text* and also some **bold text**", text_type_text)
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    self.assertEqual(new_nodes[0], TextNode("Here we have some *italic text* and also some ", text_type_text))
    self.assertEqual(new_nodes[1], TextNode("bold text", text_type_bold))

if __name__ == "__main__":
  unittest.main()