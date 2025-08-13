import math
import numpy as np
import matplotlib.pyplot as plt
print("TI-84 Emulator!")
print("Supports +, -, *, /, ^, sin(), cos(), tan(), asin(), acos(),")
print("atan(), log(), sqrt(), log()/ln() pi/e and abs value")
print("Switch between degree/radian mode with: 'mode deg' or 'mode rad'")
print("Input 'graph: (function)' to graph. Input 'exit' to quit.")

Ans = 0
angle_mode = "rad"

while True:
    expr = input(">>> ").strip()
    if expr.lower() == "exit":
        break

    # Change from radins to degrees
    if expr.lower().startswith("mode"):
        if "deg" in expr.lower():
            angle_mode = "deg"
            print("Now in degree mode")
        elif "rad" in expr.lower():
            angle_mode = "rad"
            print("Now in radian mode")
        else:
            print("ERROR")
        continue

    # Graphing functions
    if expr.lower().startswith("graph:"):
        x = np.linspace(-10, 10, 1000)
        funcs = expr[6:].split(',')
        try:
            plt.figure()
            for f in funcs:
                f = f.strip().replace('^', '**')

                env = {
                    "x": x,
                    "sin": np.sin,
                    "cos": np.cos,
                    "tan": np.tan,
                    "asin": np.arcsin,
                    "acos": np.arccos,
                    "atan": np.arctan,
                    "log": np.log10,
                    "ln": np.log,
                    "sqrt": np.sqrt,
                    "abs": np.abs,
                    "pi": math.pi,
                    "e": math.e
                }

                y = eval(f, env)


                if angle_mode == "deg":
                    y = np.degrees(y)

                plt.plot(x, y, label=f)
            plt.legend()
            plt.grid(True)
            plt.ylim(-10, 10)
            plt.show()
        except:
            print("Something went wrong with the graph")
        continue

    # Replace power symbol/Ans variable
    expr = expr.replace('^', '**')
    expr = expr.replace('Ans', str(Ans))

    try:
        # Trig if in degrees
        if angle_mode == "deg":
            expr = expr.replace("sin(", "math.sin(math.radians(")
            expr = expr.replace("cos(", "math.cos(math.radians(")
            expr = expr.replace("tan(", "math.tan(math.radians(")
            expr = expr.replace("asin(", "math.degrees(math.asin(")
            expr = expr.replace("acos(", "math.degrees(math.acos(")
            expr = expr.replace("atan(", "math.degrees(math.atan(")
        else:
            expr = expr.replace("sin(", "math.sin(")
            expr = expr.replace("cos(", "math.cos(")
            expr = expr.replace("tan(", "math.tan(")
            expr = expr.replace("asin(", "math.asin(")
            expr = expr.replace("acos(", "math.acos(")
            expr = expr.replace("atan(", "math.atan(")

        # Evaluate the expression
        result = eval(expr, {
    "math": math,
    "fact": math.factorial,
    "abs": abs,
    "log": math.log10,
    "ln": math.log,
    "sqrt": math.sqrt,
    "pi": math.pi,
    "e": math.e
})

        Ans = result
        print("=", result)

    except:
        print("ERROR!")

