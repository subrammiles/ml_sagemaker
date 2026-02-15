import io
import numpy as np
import sagemaker.amazon.common as smac

new_customers = np.array([
    [600, 3],
    [2900, 14]
], dtype=np.float32)

buffer = io.BytesIO()
smac.write_numpy_to_dense_tensor(buffer, new_customers)
buffer.seek(0)

response = predictor.predict(buffer.getvalue())
print(response)
