def main():
    price = {'Banana': 10, 'Apples': 8, 'Bread': 7, 'Cheese': 20, 'Juice': 15}
    shopping_cart = {'Banana': 2, 'Bread': 3, 'Cheese': 1, 'wine': 2}

    total = 0
    for item in shopping_cart:
        try:
            total += price.get(item) * shopping_cart.get(item)

        except Exception as e:
            print("{} does not in the price list".format(item))

    print(total)

if __name__ == "__main__":
    main()
