def OrdenamientoBurbuja(nums):
    cambio = True #para entrar en bucle
    while cambio:
        cambio = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]: #intercambio de datos
                nums[i],nums[i + 1] = nums[i + 1],nums[i] # se cambia a true porque se hizo el cambio
                cambio = True
listaNumeros = [9,8,3,6,2,1,7,5] #lista a ordenar
OrdenamientoBurbuja(listaNumeros)
print("Ordenamiento Version de Burbuja los numeros son:" )
print(listaNumeros)