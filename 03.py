def grades(notas):

    aluno_notas = {}
    i = 1

    for nota in notas:

        aluno = str(i)

        aluno_notas[aluno] = nota

        i += 1

    for aluno,nota in aluno_notas.items(): 

        if nota == max(aluno_notas.values()): 

            return 'Aluno: {}, Nota: {}'. format(aluno, nota)

on = True
while on:

    nota1 = float(input('Digite a nota do aluno 1: '))
    nota2 = float(input('Digite a nota do aluno 2: '))
    nota3 = float(input('Digite a nota do aluno 3: '))
    nota4 = float(input('Digite a nota do aluno 4: '))
    nota5 = float(input('Digite a nota do aluno 5: '))

    notas = [nota1, nota2, nota3, nota4, nota5]

    on = False

print(grades(notas))


