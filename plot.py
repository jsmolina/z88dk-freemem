import matplotlib.pyplot as plt

TOTAL_MEM = 65535
GAME_MAP_PATH = './game.map'


if __name__ == "__main__":

    labels = 'Free', 'Code'

    params = {}
    with open(GAME_MAP_PATH, 'r') as f:
        for line in f:
            line_start = line.split(';')[0]
            key, value = line_start.split('=')
            k = key.strip()
            v = value.strip()
            params[k] = v
            val = int(v.replace('$', ''), 16)
            params[k] = val

    code_size = params['__code_compiler_size']
    remaining = TOTAL_MEM - code_size
    sizes = [remaining, code_size]

    # explode es para mostrar el 'queso' separado
    explode = (0.1, 0.0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()

