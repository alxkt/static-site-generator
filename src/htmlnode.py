class HTMLNode:
  def __init__(self, tag = None, value = None, children = None, props = None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
    
  def to_html(self):
    raise NotImplementedError("to_html not implemented")
  
  def props_to_html(self):
    result = ""
    if self.props:
      for key, value in self.props.items():
        result += f" {key}=\"{value}\""
    return result

  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props = None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag == None:
      raise ValueError("ParentNode has no tag")
    if self.children == None:
      raise ValueError("ParentNode has no children")
    child_html = ""
    for child in self.children:
      child_html += child.to_html()
  
    return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"

  def __repr__(self):
    return f"ParentNode({self.tag}, {self.children}, {self.props})"