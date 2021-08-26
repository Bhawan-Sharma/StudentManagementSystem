import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(11,4))
    plt.suptitle('Student marks chart')
    plt.subplot(131)
    plt.bar(x, y,color="blue")
    plt.xlabel('Name')
    plt.ylabel('Marks')
    plt.xticks(rotation=45)
    plt.subplot(132)
    plt.scatter(z, y)
    plt.xlabel('Rollno')
    plt.ylabel('Marks')
    plt.xticks(rotation=45)
    plt.subplot(133)
    plt.plot(x, y)
    plt.xlabel('Name')
    plt.ylabel('Marks')
    plt.xticks(rotation=45)
    plt.tight_layout()
    graph = get_graph()
    return graph
