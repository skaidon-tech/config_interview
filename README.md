Overview
--------
config_interview helps in creation of interactive
user interviews that can be used to gather complex
configuration. This is similar to the interactive
interview conducted during installation of the OS.

Features
--------
- questions are configured using hierarchical data structure
- incorporate documentation directly with the questions
- offer user guidance on what option is default and what
  answers are possible
- allow user to backtrack to previous questions and remember
  the answers
- support readline integration for choice selection and 
  autocompletions
- gather answers to interview questions into a single plain
  file in an acceptable format (json, yaml, pickle)
- automatically handle question dependencies and exceptions
- validate user choices at each question
- allow interview to be satisfied using pre-recorded
  answers for non-interactive runs
- incorporate color and enhanced text attributes when the 
  running terminal supports it

To Run Package Tests
--------------------
1. Install test dependencies in a virtual environment:
   pip install -r tests/requirements.txt

2. In project top directory run tests by executing
   pytest
