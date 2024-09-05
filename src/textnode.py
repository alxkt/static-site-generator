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