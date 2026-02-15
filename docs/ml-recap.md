


| Training     | Inference         |
| ------------ | ----------------- |
| Uses dataset | Uses single input |
| Saves model  | Loads model       |
| Runs once    | Runs many times   |
| Heavy        | Lightweight       |


Inference:
You already have:

✅ Local training → model/model.joblib

✅ SageMaker training → model.tar.gz stored in S3

Now we’ll build one unified inference script that works for:

🖥 LOCAL mode

☁ AWS SageMaker mode

First: Understand the Difference
🖥 Local

After training:

a-simple-linear-regression/
    model/
        model.joblib


You just load it directly using joblib.

☁ SageMaker

After training:

SageMaker compresses model into:

model.tar.gz


Uploads it to S3

When deployed, SageMaker extracts it to:

/opt/ml/model/


So inside SageMaker container, your model is located at:

/opt/ml/model/model.joblib