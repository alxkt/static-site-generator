import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

  def test_to_html_no_tag(self):
    node = LeafNode(None, "Here is some text.")
    self.assertEqual(node.to_html(), "Here is some text.")

  def test_to_html(self):
    node = LeafNode("p", "Whatever.", {"class": "something"})
    self.assertEqual(node.to_html(), '<p class="something">Whatever.</p>')

if __name__ == "__main__":
  unittest.main()