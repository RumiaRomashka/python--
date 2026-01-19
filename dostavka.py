# Создать калькуятор стоимости доставки и заказа
# условия
# - бесплатная доставка от сумммы 10 000 руб.
# - скидка новому клиенту 5% от заказа
# - промо скидка 10% по промокоду MYPROMO от заказа
# - доставка в зону А - 399 руб., В - 599 руб., С - 899 руб.,самовывоз - 0
# - срочная доставка + 450 руб.
# - сервисный сбор 2% от суммы заказа


def read_float(promt: str) -> float:
    input_str = read_str(promt).replace(",", ".")
    value = float(input_str)
    if value <= 0:
        raise ValueError("Значение должно быть > 0")
    return value


def read_str(promt: str) -> str:
    return input(promt).strip()


def read_yes_no(promt: str) -> bool:
    return read_str(promt).lower() == "y"


NEW_CUSTOMER_DISCONT = 0.05
PROMOCODE = "MYPROMO"
PROMOCODE_DISCONT = 0.1
SERVICE = 0.02
SROCHNOST_COST = 450
DELIVERY_FREE = 10000


def calc_product_cost(base: float, is_new_customer: bool, promocode: str) -> float:
    final_price = base
    discont = 0
    if is_new_customer:
        discont += NEW_CUSTOMER_DISCONT
    if promocode == PROMOCODE:
        discont += PROMOCODE_DISCONT
    final_price = final_price * (1 - discont)
    return final_price * (1 + SERVICE)


def calc_delivery_cost(price: float, delivery_zone: str, srochnost: bool) -> float:
    delivery_cost: float = 0
    if srochnost:
        delivery_cost += SROCHNOST_COST
    if price >= DELIVERY_FREE:
        return delivery_cost
    match delivery_zone.upper():
        case "A":
            delivery_cost += 399
        case "B":
            delivery_cost += 599
        case "C":
            delivery_cost += 899
        case "pickup":
            delivery_cost += 0
        case _:
            raise ValueError("Введено неверное значение зоны доставки")
    return delivery_cost


def main():
    price = read_float("Введите итогую стоимость (Например, 50.5 руб.) ")
    is_new_customer = read_yes_no("Вы новый клиент ( y/n): ")
    promocode = read_str("Введите промокод")
    delivery_zone = read_str("В какую зону доставить: A , B , C , pickup ")
    srochnost = read_yes_no("Нужна ли срочная доставка ( y/n): ")
    price = calc_product_cost(price, is_new_customer, promocode)
    delivery_cost = calc_delivery_cost(price, delivery_zone, srochnost)
    print(price)
    print(delivery_cost)


main()
