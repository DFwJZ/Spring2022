"""
    CS5003 Spring 2022
    01/26/2022
    Module 2Coding Practice: Boolean Expressions & Conditionals
    2.Price per litter
    Jason Zhang(Haozhe Zhang) / Francisco Rovirosa

"""


def main():
    price_per_six_pack = float(input("Price per six-pack: "))
    price_per_two_liter = float(input("Price per two-liter: "))

    six_pack_unit_price = price_per_six_pack / (0.355 * 6)
    two_liter_unit_price = price_per_two_liter / 2

    print("Six-pack price per liter:", six_pack_unit_price)
    print("Two-liter price per liter:", two_liter_unit_price)


if __name__ == '__main__':
    main()
