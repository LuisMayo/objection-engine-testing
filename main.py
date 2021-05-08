import sys
sys.path.append('objection_engine/')
import objection_engine
foo = [objection_engine.comment.Comment(), objection_engine.comment.Comment(text_content='Second comment',  user_name="Second user")]
objection_engine.renderer.render_comment_list(foo)