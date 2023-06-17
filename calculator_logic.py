class CalculatorLogic:
    @staticmethod
    def evaluate_expression(expression):
        try:
            print(expression)
            return eval(expression)
        except Exception as e:
            print(e)
            return None
