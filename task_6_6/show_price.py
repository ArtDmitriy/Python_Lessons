PRICE_FILE = "./bakery.csv"

def my_gen(start=-1, end=-1):

    with open(PRICE_FILE, "r", encoding="utf-8") as price_list:
        if start > 0:
            for _ in range(start - 1):
                price_list.readline()

        if end > 0:
            for _ in range(abs(end-start)):
                yield price_list.readline().replace("\n", "")

        for line in price_list:
            yield line.replace("\n", "")

if __name__ == "__main__":
    pass
