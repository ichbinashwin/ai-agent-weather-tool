############################################################################################
# Architecture of AI Agent
############################################################################################
#                              [ Prompt Template ]
#                                      |
#                                      |
#                                      V
#  [User] <--- Prompt/Response --> [ Agent ] <----- Planning/Reasoning -----> [ LLM ]
#                                      |
#                                      |
#               ___________________________________________
#               |                                         |
#               |                                         |
#             Actions                                Store/Retrieve
#               |                                         |
#               |                                         |
#               V                                         V
#           [ Tools ]                                  [ Memory ]
#
#############################################################################################
# Types of AI Agent
- Simple Reflex Agent
- Model-based Reflex Agent
- Goal-based Agent
- Utility-based Agent
- Learning Agent
# AI Models for Agent
- Amazon Bedrock Agent Components
-- Agent
-- Action Groups [ Schema, Lambda ]
-- Foundation Model
-- Knowledge Bases [ Vector DB ]

############################################################################################
RAG
