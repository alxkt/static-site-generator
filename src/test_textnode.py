import unittest

from textnode import TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node, node2)

  def test_not_eq(self):
    node = TextNode("This is one", "italic", "hey.com")
    node2 = TextNode("This is two", "italic", "hey.com")
    self.assertNotEqual(node, node2)

  def test_not_eq_urls(self):
    node = TextNode("This is one", "italic", "hey.com")
    node2 = TextNode("This is one", "italic", "heyu.com")
    self.assertNotEqual(node, node2)
  
  def test_not_eq_type(self):
    node = TextNode("This is one", "italic", "hey.com")
    node2 = TextNode("This is one", "bold", "hey.com")
    self.assertNotEqual(node, node2)

  def test_repr(self):
    node = TextNode("This hah.", "j")
    return_string = "TextNode(This hah., j)"
    self.assertEqual(str(node), return_string)

  def test_to_html_text(self):
    text_node = TextNode("Here is some text.", "text")
    html_node = text_node_to_html_node(text_node)
    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "Here is some text.")

if __name__ == "__main__":
  unittest.main()