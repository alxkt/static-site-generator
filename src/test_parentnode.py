import unittest

from htmlnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

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