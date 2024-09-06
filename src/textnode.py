from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def text_node_to_html_node(text_node):
  match text_node.text_type:
    case "text":
      return LeafNode(None, text_node.text)
    case "bold":
      return LeafNode("b", text_node.text)
    case "italic":
      return LeafNode("i", text_node.text)
    case "code":
      return LeafNode("code", text_node.text)
    case "link":
      return LeafNode("a", text_node.text, {"href": text_node.url})
    case "image":
      return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    case _:
      raise Exception("Text type not recognized")

class TextNode:
  def __init__(self, text, text_type, url = None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other_node):
    if (other_node.text == self.text and 
        other_node.text_type == self.text_type and 
        other_node.url == self.url
        ):
      return True
    return False

  def __repr__(self):
    if self.url: 
      return f"TextNode({self.text}, {self.text_type}, {self.url})"
    else: 
      return f"TextNode({self.text}, {self.text_type})"