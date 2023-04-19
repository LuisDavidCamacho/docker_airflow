from airflow.models.baseoperator import BaseOperator

class HelloOperator(BaseOperator):
    #Constructor
    def __init__(self, name:str, **kwargs):
        super().__init__(**kwargs)
        self.name = name
    
    #Execute method
    def execute(self, context):
        print(f"Hello {self.name}")

