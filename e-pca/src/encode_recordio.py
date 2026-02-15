import numpy as np
import io
import sagemaker.amazon.common as smac

def encode():

    data_np = np.load("data/customers.npy")

    buffer = io.BytesIO()

    smac.write_numpy_to_dense_tensor(
        buffer,
        data_np
    )

    buffer.seek(0)

    with open("data/customers.recordio", "wb") as f:
        f.write(buffer.getvalue())

    print("RecordIO file created")

if __name__ == "__main__":
    encode()
