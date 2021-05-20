import sys
sys.path.append('objection_engine/')
import objection_engine
# You can also import the components like this
from objection_engine.renderer import render_comment_list
from objection_engine.beans.comment import Comment
foo = [objection_engine.comment.Comment(), objection_engine.comment.Comment(text_content='Second comment',  user_name="Second user")]
objection_engine.renderer.render_comment_list(foo)
