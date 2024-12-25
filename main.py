# Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
# Напишите асинхронную функцию start_strongman(name, power), где name - имя силача, power - его подъёмная мощность. Реализуйте следующую логику в функции:
# В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
# После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>' с задержкой обратно пропорциональной его силе power. Для каждого участника количество шаров одинаковое - 5.
# В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'
# Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman. Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
# После поставьте каждую задачу в ожидание (await).
# Запустите асинхронную функцию start_tournament методом run.
import asyncio
import random


async def start_strongman(name: str, power: float) -> None:

    print(f"Силач {name} начал соревнования.")

    for i in range(1, 6):  # 5 шаров
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна силе
        print(f"Силач {name} поднял {i}-й шар.")

    print(f"Силач {name} закончил соревнования.")


async def start_tournament() -> None:
    # Создание задач для участников
    tasks = [
        start_strongman("Александр", random.randint(1, 10)),
        start_strongman("Владимир", random.randint(1, 10)),
        start_strongman("Николай", random.randint(1, 10))
    ]
    await asyncio.gather(*tasks)  # Ожидание завершения всех задач
    # await start_strongman("Александр", random.randint(1, 10))
    # await start_strongman("Владимир", random.randint(1, 10))
    # await start_strongman("Николай", random.randint(1, 10))

if __name__ == "__main__":

    asyncio.run(start_tournament())

