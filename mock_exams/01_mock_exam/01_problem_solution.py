from collections import deque


def filter_valid_orders(data):
    return [order for order in data if 0 < order <= 10]


def process_data(orders, workers):
    total_pizzas = 0
    while orders:
        if not workers:
            break

        if orders[0] <= workers[-1]:
            total_pizzas += orders[0]
            orders.popleft()
            workers.pop()
        else:
            total_pizzas += workers[-1]
            orders[0] -= workers.pop()
    return total_pizzas, orders, workers


def print_result(data):
    total_pizzas = data[0]
    orders = data[1]
    workers = data[2]
    if not valid_orders:
        print("All orders are successfully completed!")
        print(f"Total pizzas made: {total_pizzas}")
        print(f"Employees: {', '.join([str(i) for i in workers])}")
    elif not employees:
        print("Not all orders are completed.")
        print(f"Orders left: {', '.join([str(i) for i in orders])}")


pizza_orders = list(map(int, input().split(", ")))
employees = list(map(int, input().split(", ")))
valid_orders = deque(filter_valid_orders(pizza_orders))
result = process_data(valid_orders, employees)
print_result(result)
