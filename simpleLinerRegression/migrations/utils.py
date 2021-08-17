import base64
from io import BytesIO
import matplotlib.pyplot as plt

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format = 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,pred_y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title('salary vs Experence')
    plt.scatter(x,y,color = 'red')
    plt.plot(x,pred_y,color = 'blue')
    plt.xlabel('years of exp')
    plt.ylabel('salary')
    plt.tight_layout()
    graph = get_graph()
    return graph