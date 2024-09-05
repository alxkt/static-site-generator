import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

  # Leafnode
  def test_to_html_no_tag(self):
    node = LeafNode(None, "Here is some text.")
    self.assertEqual(node.to_html(), "Here is some text.")

  def test_to_html(self):
    node = LeafNode("p", "Whatever.", {"class": "something"})
    self.assertEqual(node.to_html(), '<p class="something">Whatever.</p>')

  # Parentnode
  def test_to_html_one_leaf_child(self):
    leafnode = LeafNode("p", "Here is some text in a paragraph tag")
    parentnode = ParentNode("div", [leafnode], {"class": "navigation"})
    expect = '<div class="navigation"><p>Here is some text in a paragraph tag</p></div>'
    self.assertEqual(parentnode.to_html(), expect)

    parentnode2 = ParentNode(
        "h1",
        [
          LeafNode("div", "some text in a div"),
        ]
    )
    expect2 = '<h1><div>some text in a div</div></h1>'
    self.assertEqual(parentnode2.to_html(), expect2)

  def test_to_html_two_nested_children(self):
    parentnode = ParentNode(
        "h1",
        [
          ParentNode("div", [
            LeafNode("p", "Nested text.", {"style": "not real"})
            ]
          ),
        ]
    )
    expect = '<h1><div><p style="not real">Nested text.</p></div></h1>'
    self.assertEqual(parentnode.to_html(), expect)

  def test_to_html_multiple_nested_children(self):
    parentnode = ParentNode(
        "h1",
        [
          ParentNode("div", [
            LeafNode("p", "Nested text.", {"style": "not real"})
            ]
          ),
          ParentNode("h2", [
            LeafNode("span", "Sibling text.")
            ]
          ),

        ]
    )
    expect = '<h1><div><p style="not real">Nested text.</p></div><h2><span>Sibling text.</span></h2></h1>'
    self.assertEqual(parentnode.to_html(), expect)

if __name__ == "__main__":
  unittest.main()