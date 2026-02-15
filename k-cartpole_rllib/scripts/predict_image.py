with open("example_image.png", "rb") as f:
    result = predictor.predict(f.read())

print(result)
