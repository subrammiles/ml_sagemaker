
# Business Problem:
A bank needs to decide in real time whether a credit card transaction is fraudulent.
Core Question
“Is this transaction legitimate or fraudulent?”

Real-World Constraints
1.Latency is critical → decision in milliseconds
2.Accuracy matters, but speed matters more
3.Model must retrain periodically as fraud patterns change
4.Must work as a real-time API used by transaction systems


# Output label:
A binary classification:
Value	Meaning
0	Legitimate transaction
1	Fraudulent transaction

# Input Features (Realistic Transaction Data):
For every transaction, the model receives numerical features such as:
Feature	Description
(i).amount	         Transaction amount
(ii).hour	        Hour of day (0–23)
(iii). distance_km	Distance from user’s home
(iv).txns_last_24h	Number of transactions in past 24 hours
⚠️ These are inputs, not predictions.


Eg:
When a customer swipes their card ,Transaction service sends the following  data
{
  "amount": 245.60,
  "hour": 23,
  "distance_km": 1200,
  "txns_last_24h": 7
}


# pre request
python projects/sgboost/data_generator.py

