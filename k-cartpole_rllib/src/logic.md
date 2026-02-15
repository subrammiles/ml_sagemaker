Iris is tiny, free, and perfect for learning ML pipelines.
 No data cleaning needed → focus on SageMaker concepts.
 
🌼 Sepals of Iris
The sepals are the outer flower parts
In iris, sepals are large, colorful, and petal-like
They are called “falls”
Usually bend downward
🌸 Petals of Iris
The petals are the inner flower parts
They are called “standards”
Usually stand upright
We used sepal & petal measurements as INPUTS to predict the flower SPECIES as OUTPUT.

The model predicted the flower species (class 0, 1, or 2)
Input features (what you give the model)
For each flower, you gave 4 numbers:
1.Sepal length (cm)
2.Sepal width (cm)
3.Petal length (cm)
4.Petal width (cm)
Example input row:
[5.1, 3.5, 1.4, 0.2]
⚠️ In your code, these values were scaled using StandardScaler, but logically they represent the same measurements.
Output label (what the model predicts)
The model outputs one integer:
0, 1, or 2
Each number means a flower species:
Label	Species
0	Iris-setosa
1	Iris-versicolor
2	Iris-virginica

So when you saw:
1.0
It meant:
“This flower is Iris-versicolor”
