import unittest
from textnode import *
from inline_markdown_methods import *

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

class TestExtractMarkdownImages(unittest.TestCase):
  def test_extract_single_image(self):
    text = "Here is some text with an image ![alt text](https://someurl.com/aeiou.jpg) in it."
    image_extracted = extract_markdown_images(text)
    self.assertEqual(image_extracted, [("alt text", "https://someurl.com/aeiou.jpg")])

  def test_extract_multiple_images(self):
    text = "Let's do several images ![First one](https://mysite.com/randome.png) and another ![second one](https://thatsite.org/what.bmp)"
    image_extracted = extract_markdown_images(text)
    self.assertEqual(image_extracted, [
      ("First one", "https://mysite.com/randome.png"),
      ("second one", "https://thatsite.org/what.bmp")
    ])

class TestExtractMarkdownLinks(unittest.TestCase):
  def test_extract_single_link(self):
    text = "Here is some text with a link [alt text](https://someurl.com/) in it."
    link_extracted = extract_markdown_links(text)
    self.assertEqual(link_extracted, [("alt text", "https://someurl.com/")])

  def text_extract_multiple_links(self):
    text = "Let's do several links [First one](https://mysite.com/) and another [second one](https://thatsite.org/)"
    link_extracted = extract_markdown_links(text)
    self.assertEqual(link_extracted, [
      ("First one", "https://mysite.com/"),
      ("second one", "https://thatsite.org/")
    ])

class TestSplitNodesImage(unittest.TestCase):
  def test_split_nodes_image(self):
    node = TextNode("This is text with a single ![img](https://www.google.com/pny.jpg) image.", text_type_text)
    split_nodes = split_nodes_image([node])
    self.assertEqual(split_nodes, [
      TextNode("This is text with a single ", text_type_text),
      TextNode("img", text_type_image, "https://www.google.com/pny.jpg"),
      TextNode(" image.", text_type_text)
    ])

class TestSplitNodesLink(unittest.TestCase):
  def test_split_nodes_link(self):
    node = TextNode("This is text with a single [link](https://www.google.com/) link.", text_type_text)
    split_nodes = split_nodes_link([node])
    self.assertEqual(split_nodes, [
      TextNode("This is text with a single ", text_type_text),
      TextNode("link", text_type_link, "https://www.google.com/"),
      TextNode(" link.", text_type_text)
    ])

class TestTextToTextNodes(unittest.TestCase):
  def test_text_to_textnodes(self):
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    self.assertEqual(nodes, [
    TextNode("This is ", text_type_text),
    TextNode("text", text_type_bold),
    TextNode(" with an ", text_type_text),
    TextNode("italic", text_type_italic),
    TextNode(" word and a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" and an ", text_type_text),
    TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", text_type_text),
    TextNode("link", text_type_link, "https://boot.dev"),
])

if __name__ == "__main__":
  unittest.main()