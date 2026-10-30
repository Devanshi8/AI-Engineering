ReAct = REASONING + ACTION
is a concept where LLM take self decision which tools/apis is available and utilize as per prompt.
which tool it need to use, where to use, how to use, when to use.

Process of ReAct look like

1. Add LLM + Tools / APIs

2. Repeat this untill you get the final answer
   - System Prompt - decide what to do and which tool/api are available to use
   - execute tool
   - observation(answer/output from that tool)
   - reuse observation
