import matplotlib.pyplot as plt

#def rand_list(x1, x2, y_min, y_max)
#    x = list

def prova_plot():
    x1 = range(5)
    y1 = [5, 8.5, 8, None, 9]
    x2 = (2, 3, 4)
    y2 = [10, 10, 11]

    fig, ax = plt.subplots()
    ax.scatter(x1, y1)
    ax.plot(x2, y2, color = "#822433", linewidth=2, linestyle = "dashed")
#    plt.savefig("./prova_plot.pdf")
    plt.show()
    
if __name__ == "__main__":
    prova_plot()