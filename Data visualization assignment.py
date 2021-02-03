import plotly_express as px
import seaborn as sns


iris = sns.load_dataset('iris')
iris.head()

px.scatter_3d(iris, x="petal_length", y="petal_width", z="sepal_length", size="sepal_width", 
              color="species", color_discrete_map = {"Joly": "blue", "Bergeron": "violet", "Coderre":"pink"})