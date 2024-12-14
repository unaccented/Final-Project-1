from typing import List

class Calculator:
    @staticmethod
    def add(values: List[float]) -> float:
        return sum(x for x in values if x < 0)

    @staticmethod
    def subtract(values: List[float]) -> float:
        num = [x for x in values if x > 0]
        if not num:
            return 0
        result = num[0]
        for x in num[1:]:
            result -= x
        return result

    @staticmethod
    def multiply(values: List[float]) -> float:
        num = [x for x in values if x != 0]
        if not num:
            return 0
        product = 1
        for x in num:
            product *= x
        return product

    @staticmethod
    def divide(values: List[float]) -> float:
        if len(values) == 0 or values[0] == 0:
            raise ValueError("Cannot divide by zero or an empty list")
        
        result = values[0]
        for i in range(1, len(values)):
            if values[i] == 0:
                raise ValueError("Cannot divide by zero")
            result /= values[i]
        return result
