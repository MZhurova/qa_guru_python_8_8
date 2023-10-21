"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(999)
        assert product.quantity == 1

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add(self, cart, product):
        cart.add_product(product, 1)

        assert cart.products[product] == 1

        cart.add_product(product, 6)

        assert cart.products[product] == 7

    def test_delete(self, cart, product):
        cart.add_product(product, 7)
        cart.remove_product(product, 3)

        assert cart.products[product] == 4

        cart.remove_product(product, 4)

        assert product not in cart.products

    def test_clear(self, cart, product):
        cart.add_product(product, 7)
        cart.clear()

        assert product not in cart.products

    def test_buy(self, cart, product):
        cart.add_product(product, 77)
        cart.buy() == 90

        assert product not in cart.products
        assert product.quantity == 923

    def test_buy_more(self, cart, product):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()
