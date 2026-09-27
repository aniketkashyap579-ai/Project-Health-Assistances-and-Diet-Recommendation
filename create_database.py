import sys
import os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from rag import create_rag

print("Create Data....")
create_rag()
print("Database create")