import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

  def test_props(self):
    props = {
      "href": "https://www.google.com",
      "target": "_blank",
    }
    node = HTMLNode("a", "Google", None, props)
    result = ' href="https://www.google.com" target="_blank"'
    self.assertEqual(node.props_to_html(), result)

  def test_props_blank(self):
    node = HTMLNode()
    self.assertEqual(node.props_to_html(), "")
  
  def test_repr(self):
    node = HTMLNode("li")
    self.assertEqual(str(node), "HTMLNode(li, None, None, None)")

  def test_repr_blank(self):
    node = HTMLNode()
    expect = "HTMLNode(None, None, None, None)"
    self.assertEqual(str(node), expect)

if __name__ == "__main__":
  unittest.main()