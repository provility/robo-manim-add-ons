generate_animation_instructions_template="""
You are given a class called LessonScene along with its base class RobogebraScene.
LessonScene Definition: {lesson_scene_definition}
RobogebrScene Definition: {robogebra_scene_definition}

Your task is to add a new method named {method_name} to the LessonScene class.
The new method should call one or more existing methods in the RobogebraScene class 
in order to satisfy the following requirements: {requirements}
"""

visual_aid_teacher_personality = """You are a smart Math teacher who is good 
at making use of visual aids and diagrams 
to explain mathematical ideas to students. You are familiar with the use of tools 
like Geogebra, Desmos and Mathematica. You apply lot of ideas inspired 
these tools though you dont use them directly with students.
You prefer writing custom programs yourself.
    """

step_to_visualization_map=""" 
For the given the expression {expression}, {problem_command}, you are provided 
with a 'step by step' solution here in JSON: {step_list}.

Your task is identify, among the given 'step by step' solution, which steps need visualization support, to make the student understand the concepts better.
If a step uses just algebraic manipulation, say None in the visualization_step field.

Explain how each visualization step would help the student in visualization_purpose field.

visual step constraints:
1. Should have exactly the same number of steps in 'step by step' solution. For example, if the JSON has 4 steps, the total visualization steps should also be 4.
2. The visual step should be correlated with the given step in 'step by step' solution.
3. The current visualization should not make use of values that are yet to be derived from the next steps.
For example the 'visual_step' 4 should not make use of values or results obtained in step 5 of 'step_by_step' solution.

formatting instructions: {format_instructions}
"""

visual_step_details_template=""" 
You can broadly make use of the following visualization methods: {visualization_methods}

"""