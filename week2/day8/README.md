Promot Chaining : divide the prompt task by task

UseCases:

Debugging => u can easily find/check for the bug step by step. no need to reading entire output and find the bug
Modularity => change in patricular part of code
Different Model => uses

    - complex task uses heavy models e.g. claude fable
    - simple task uses basic/free models e.g. chatGPT free version

Retry Steps => retry particular steps using changes in particular prompt to get best result

#--------------------------------------------------------------------------------------

React - >
REASONING + ACTION
is a concept where LLM take self decision which tools/apis is available and utilize as per prompt.
which tool it need to use, where to use, how to use, when to use.

    LLM decide what, when, how to do

while

Prompt chaining - >
Developer decide which tool it need to use, where to use, how to use, when to use. by giving prompt
