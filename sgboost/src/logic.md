
data_generator.py Is

It simulates real transaction data for your fraud system 


Split Features and Label
X = data.drop("label", axis=1)
y = data["label"]


Because SageMaker expects:

Features separate

Label explicitly first column