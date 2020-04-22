prompt = "\n Назовите число и я верну его квадрат"
prompt += "\n Введите 0, чтобы закончить программу"
message = ""
while message != "0":
    message= input(prompt)
    print(int(message) ** 2)
