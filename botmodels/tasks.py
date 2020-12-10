


@app.task
def hello_world():
    sleep(60)  # поставим тут задержку в 10 сек для демонстрации ассинхрности
    print('Hello World')
