Basic details extract from customer prompt. **Ticket Management System**
to make it more readable using JSON pydantic.
to make structured output

#Errors Debuggung

1. schema=Ticket.model_json_schema()
   ^^^^^^^^^^^^^^^^^^^^^^^^
   AttributeError: type object 'Ticket' has no attribute 'model_json_schema'
   =>bcoz class Ticket() #BaseModel not included
   class ticket(BaseModel) => error resolved

2. Line33 :- Extract personal information from the ticket strictly based on this schema. (gives an error)
   Error code: 400 - {'error': {'message': "'messages' must contain the word 'json' in some form, to use 'response_format' of type 'json_object'.", 'type': 'invalid_request_error'}}
   in system_prompt

   after adding give a json output. it resolved.

uv add pydantic
