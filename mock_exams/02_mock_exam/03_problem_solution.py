def stock_availability(list_of_boxes, command, *args):
    args = [str(i) for i in args]
    if command == "delivery":
        list_of_boxes.extend(args)
    elif command == "sell":
        if args:
            if args[0].isdigit():
                for i in range(int(args[0])):
                    list_of_boxes.pop(0)
            else:
                for item in args:
                    while item in list_of_boxes:
                        list_of_boxes.remove(item)
        else:
            list_of_boxes.pop(0)
    return list_of_boxes


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
