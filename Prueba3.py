def f(x):
    return x**2 + 5*x + 6

def df(x):
    return 2*x + 5

def gradient_descent(learning_rate, epochs, x_init):
    x = x_init
    epochs = int(epochs)
    for _ in range(epochs):
        grad = df(x)
        x = x - learning_rate * grad
    y = f(x)
    return x, y

learning_rate, epochs, x_init = map(float, input().split())

x_final, y_final = gradient_descent(learning_rate, epochs, x_init)

print(f"{x_final:.6f}".rstrip('0').rstrip('.0'), f"{y_final:.6f}".rstrip('0').rstrip('.'))