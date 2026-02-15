import numpy as np
import io
import sagemaker.amazon.common as smac

new_data = np.array([
    [2.0, 2.1, 1.0],
    [0.6, 0.8, 0.4]
], dtype="float32")

buffer = io.BytesIO()
smac.write_numpy_to_dense_tensor(buffer, new_data)
buffer.seek(0)

response = predictor.predict(buffer.getvalue())
print(response)
