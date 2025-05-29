import pytest
from src.gen_ai_content import generate_content

def test_generate_content():
    student_data = {"text_input": "Test", "learning_style": "visual"}
    content = generate_content(student_data)
    assert isinstance(content, str)
    assert len(content) > 0
