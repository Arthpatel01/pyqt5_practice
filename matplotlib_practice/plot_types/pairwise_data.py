import matplotlib.pyplot as plt
import numpy as np


def plot_tutorial():
    plt.style.use("_mpl-gallery")

    x = np.linspace(0, 10, 100)
    y = 4 + 2 * np.sin(2 * x)

    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    plt.show()


def scatter_plot_tutorial():
    # plt.style.use("_mpl-gallery")

    np.random.seed(3)
    x = 4 + np.random.normal(0, 2, 24)
    y = 4 + np.random.normal(0, 2, len(x))

    size = np.random.uniform(15, 80, len(x))
    colors = np.random.uniform(15, 80, len(x))

    print("X:", x)
    print("Y:", y)
    print("Size:", size)
    print("Color:", colors)

    fig, ax = plt.subplots()

    ax.scatter(x, y, s=size, c=colors, vmin=0, vmax=100)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()


def multi_lines_tutorial():
    # Provided data
    data = [
        [83.0, 234.289, 235.6, 159.0, 107.608, 1947, 60.323],
        [88.5, 259.426, 232.5, 145.6, 108.632, 1948, 61.122],
        [88.2, 258.054, 368.2, 161.6, 109.773, 1949, 60.171],
        [89.5, 284.599, 335.1, 165.0, 110.929, 1950, 61.187],
        [96.2, 328.975, 209.9, 309.9, 112.075, 1951, 63.221],
        [98.1, 346.999, 193.2, 359.4, 113.27, 1952, 63.639],
        [99.0, 365.385, 187.0, 354.7, 115.094, 1953, 64.989],
        [100.0, 363.112, 357.8, 335.0, 116.219, 1954, 63.761],
        [101.2, 397.469, 290.4, 304.8, 117.388, 1955, 66.019],
        [104.6, 419.18, 282.2, 285.7, 118.734, 1956, 67.857],
        [108.4, 442.769, 293.6, 279.8, 120.445, 1957, 68.169],
        [110.8, 444.546, 468.1, 263.7, 121.95, 1958, 66.513],
        [112.6, 482.704, 381.3, 255.2, 123.366, 1959, 68.655],
        [114.2, 502.601, 393.1, 251.4, 125.368, 1960, 69.564],
        [115.7, 518.173, 480.6, 257.2, 127.852, 1961, 69.331],
        [116.9, 554.894, 400.7, 282.7, 130.081, 1962, 70.551]
    ]

    transposed_data = list(map(list, zip(*data)))

    # Extracting data for plotting
    years = transposed_data[-1]
    sensor_data = transposed_data[:-1]

    # Plotting each sensor's data
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, sensor_values in enumerate(sensor_data):
        ax.plot(years, sensor_values, label=f"Sensor {i + 1}")

    # Adding labels and legend
    ax.set_xlabel('Year')
    ax.set_ylabel('Sensor Values')
    ax.set_title('Sensor Data Over Time')
    ax.legend()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    # plot_tutorial()
    # scatter_plot_tutorial()
    multi_lines_tutorial()
