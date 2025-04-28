"""
Codigo sucio, utilitario, tan solo el que lo escribio lo entiende.
No es necesariamente malo, ni un representativo de habilidad, pero
si es una proyeccion de malos habitos y un miembro de equipo que
no necesariamente trabaja en equipo.
"""


def check(items, val):
    """Checks if order needs expediting."""
    f = False
    for i in items:
        if i["type"] == "A" or val > 1000:
            f = True
            break
    return f


"""
    Entonces que procede? Refactorizar, esto no es factible todo el tiempo
    pero si uno tiene la oportunidad es bastante amigable al momento
    de delegar tareas. Esto generalmente agiliza el proceso de 
    desarrollo a largo plazo.
"""


EXPEDITED_ITEM_TYPE = "A"
EXPEDITE_THRESHOLD_VALUE = 1000


def should_expedite_order(order_items, order_total_value):
    """
    Determines if an order requires expedited shipping based
    on it's items and value.

    Args:
        order_items (list): A list of dictionaries where each dictionary represents
        an item and has atleast a type key.

        order_total_value (float/int): Represents the total value of the item.

    Returns:
        bool: True if the order should be expedited
    """
    needs_expediting = False
    for item in order_items:
        if (
            item["type"] == EXPEDITED_ITEM_TYPE
            or order_total_value > EXPEDITE_THRESHOLD_VALUE
        ):
            needs_expediting = True
            break
    return needs_expediting


if __name__ == "__main__":
    order1_items = [{"id": 1, "type": "B"}, {"id": 2, "type": "C"}]
    order1_value = 500
    order2_items = [{"id": 3, "type": "B"}, {"id": 4, "type": "A"}]
    order2_value = 200
    order3_items = [{"id": 5, "type": "C"}]
    order3_value = 1500
    print(
        f"Order 1 Expedite: {should_expedite_order(order1_items, order1_value)}"
    )  # Expected: False
    print(
        f"Order 2 Expedite: {should_expedite_order(order2_items, order2_value)}"
    )  # Expected: True
    print(
        f"Order 3 Expedite: {should_expedite_order(order3_items, order3_value)}"
    )  # Expected: True
