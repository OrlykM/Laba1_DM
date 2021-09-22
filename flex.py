from itertools import product  # функція для генерування значень 0 і 1
from prettytable import PrettyTable  # клас для красивого виводу значень таблиці істинності
Values = [{"X": []}, {"Y": []}, {"Z": []}]
AnitValues = [{"notX":[]}, {"notY": []}, {"notZ":[]}]
Results = []
InputValues = []
Results2 = []
s = 0
def generateData(diapazon:int):
    return list(product([0, 1], repeat=diapazon))
def show_table_difficalt_statement():
   t = PrettyTable()
   print("""
        Додаток 2 частина 1
        
        1 - notX~notY'\n
        2 - Y~Z\n
        3 - Z~X\n
        4 - XorZ\n
        5 - (Y~Z)->(Z~X)\n
        6 - ((Y~Z)->(Z~X)) -> (XorZ)\n
        7 - (notX~notY) -> ((Y~Z)->(Z~X)) -> (XorZ)\n
   """)
   t.add_column("X",Values[0].get("X"))
   t.add_column("Y", Values[1].get("Y"))
   t.add_column("Z", Values[2].get("Z"))
   t.add_column("notX", AnitValues[0].get("notX"))
   t.add_column("notY", AnitValues[1].get("notY"))
   t.add_column("notZ", AnitValues[2].get("notZ"))
   for x in range(len(Results)):t.add_column(f"{x+1}", Results[x])
   print(str(t))
def show_table_simple_statement(name_of_operation):
    t = PrettyTable()
    for x in range(len(Results2)): t.add_column(f"P{x}", InputValues[x].get(f"P{x}"))
    for x in range(len(Results2)): t.add_column(f"{name_of_operation}", Results2[x])
    print(str(t))
def eqvivalention(list1, list2):
    OutputArray = []
    if len(list1) == len(list2):
        for x in range(len(list1)):
            if list1[x] == list2[x]:
                OutputArray.append(1)
            else:
                OutputArray.append(0)
    return OutputArray
def implication(list1, list2):
    OutPutArray = []
    if len(list1) == len(list2):
        for x in range(len(list1)):
            if list1[x] == 0 and list2 == 1:
                OutPutArray.append(1)
            elif list1[x] == list2[x]:
                OutPutArray.append(1)
            else:
                OutPutArray.append(0)
    return OutPutArray
def dezunction(list1, list2):
    OutPutArray = []
    if len(list1) == len(list2):
        for x in range(len(list1)):
            if list1[x] == 1 or list2[x] == 1 or list1[x] == list2[x] == 1:
                OutPutArray.append(1)
            else:
                OutPutArray.append(0)
    return OutPutArray
def konunction(list1, list2):
    OutPutArray = []
    if len(list1) == len(list2):
        for x in range(len(list1)):
            if list1[x] == list2[x] == 1:
                OutPutArray.append(1)
            else:
                OutPutArray.append(0)
    return OutPutArray
def modul2(list1, list2):
    OutPutArray = []
    if len(list1) == len(list2):
        for x in range(len(list1)):
            if list1[x] == list2[x]:
                OutPutArray.append(0)
            else:
                OutPutArray.append(1)
    return OutPutArray
if __name__ == '__main__':
    # Додаток 2 частина 1
    All_Data_Values = generateData(3)
    for x in All_Data_Values:
        if x[0] == 0:
            Values[0].get("X").append(x[0])
            AnitValues[0].get("notX").append(1)
        else:
            Values[0].get("X").append(x[0])
            AnitValues[0].get("notX").append(0)

        if x[1] == 0:
            Values[1].get("Y").append(x[1])
            AnitValues[1].get("notY").append(1)
        else:
            Values[1].get("Y").append(x[1])
            AnitValues[1].get("notY").append(0)

        if x[2] == 0:
            Values[2].get("Z").append(x[2])
            AnitValues[2].get("notZ").append(1)
        else:
            Values[2].get("Z").append(x[2])
            AnitValues[2].get("notZ").append(0)
    Results.append(eqvivalention(AnitValues[0].get("notX"), AnitValues[1].get("notY")))
    Results.append(eqvivalention(Values[1].get("Y"), Values[2].get("Z")))
    Results.append(eqvivalention(Values[2].get("Z"), Values[0].get("X")))
    Results.append(dezunction(Values[0].get("X"), Values[2].get("Z")))
    Results.append(implication(Results[1],Results[2]))
    Results.append(implication(Results[4],Results[3]))
    Results.append(implication(Results[0], Results[5]))
    show_table_difficalt_statement()
    print("Додаток 2 частина 2")
    # Додаток 2 частина 2
    CountOfValues = int(input("Уведіть кількість простих висловлювань:>>> "))
    Operation = int(input("Уведіть номер операції між простими висловлюваннями\n "
                          "(1-імплікація, 2-диз'юнкція, 3-кон'юнкція\n"
                          "4-виключна диз'юнкція 5-еквівалентність\n"
                          ":>>> "))
    if CountOfValues.__sizeof__() > 0 and Operation.__sizeof__() > 0 and Operation > 0 and Operation < 6:
        CountValuesData = generateData(CountOfValues)
        for i in range(CountOfValues):
            InputValues.append({f"P{i}":[]})
        while s < len(InputValues):
            for j in CountValuesData:
                InputValues[s].get(f"P{s}").append(j[s])
            s += 1
        k = 0
        if Operation == 1:
            while k < len(InputValues):
                if k == len(InputValues) - 1 and len(InputValues) > 1:
                    Results2.append(implication(InputValues[0].get(f"P{0}"), InputValues[k].get(f"P{k}")))
                    show_table_simple_statement("implication")
                elif k == 1 and len(InputValues) == 1:
                    print("Замала кількість простих висловлювань")
                else:
                    Results2.append(implication(InputValues[k].get(f"P{k}"), InputValues[k+1].get(f"P{k+1}")))
                k += 1
        elif Operation == 2:
            while k < len(InputValues):
                if k == len(InputValues) - 1 and len(InputValues) > 1:
                    Results2.append(dezunction(InputValues[0].get(f"P{0}"), InputValues[k].get(f"P{k}")))
                elif k == len(InputValues) and len(InputValues) == 1:
                    print("Замала кількість простих висловлювань")
                else:
                    Results2.append(dezunction(InputValues[k].get(f"P{k}"), InputValues[k + 1].get(f"P{k + 1}")))
                k += 1
            show_table_simple_statement("dezunction")
        elif Operation == 3:
            while k < len(InputValues):
                if k == len(InputValues) - 1 and len(InputValues) > 1:
                    Results2.append(konunction(InputValues[0].get(f"P{0}"), InputValues[k].get(f"P{k}")))
                elif k == len(InputValues) and len(InputValues) == 1:
                    print("Замала кількість простих висловлювань")
                else:
                    Results2.append(konunction(InputValues[k].get(f"P{k}"), InputValues[k + 1].get(f"P{k + 1}")))
                k += 1
            show_table_simple_statement("konnunction")
        elif Operation == 4:
            while k < len(InputValues):
                if k == len(InputValues) - 1 and len(InputValues) > 1:
                    Results2.append(modul2(InputValues[0].get(f"P{0}"), InputValues[k].get(f"P{k}")))
                elif k == len(InputValues) and len(InputValues) == 1:
                    print("Замала кількість простих висловлювань")
                else:
                    Results2.append(modul2(InputValues[k].get(f"P{k}"), InputValues[k + 1].get(f"P{k + 1}")))
                k += 1
            show_table_simple_statement("modul 2")
        elif Operation == 5:
            while k < len(InputValues):
                if k == len(InputValues) - 1 and len(InputValues) > 1:
                    Results2.append(eqvivalention(InputValues[0].get(f"P{0}"), InputValues[k].get(f"P{k}")))
                elif k == len(InputValues) and len(InputValues) == 1:
                    print("Замала кількість простих висловлювань")
                else:
                    Results2.append(eqvivalention(InputValues[k].get(f"P{k}"), InputValues[k + 1].get(f"P{k + 1}")))
                k += 1
            show_table_simple_statement("eqvivalention")
    else:
        print("Задані вами параметри неправильні, будь ласка спробуйде щераз")