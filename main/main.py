import pandas as pd

def main():
    df = pd.read_excel(r'C:\Users\Harry\PycharmProjects\sciElements\resource\listElements.xlsx')
    print(df.head())
    print('Lade von Excel')

    elementsList = list() #einfache Liste für die Elemente

    #Speichert jede Zeile in die elementsList
    for index, value in df.iterrows():
        elementsList.append(value['Elements'])

    #Gibt alle Elemente in der Liste aus(Brauchst du dann nicht)
    for element in elementsList:
        print(element)

main()