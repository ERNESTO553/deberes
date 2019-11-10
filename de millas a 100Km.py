# ERNESTO RODRIGUEZ#

# PASO 1  DEFINIMOS LAS FUNCIONES PARA TRANSFORMAR DE Km/lt a M/gl
def mpgtoL100km(litros):
# PASO 2 DESGLOSAR LAS ECUACIONES OBTENIDAS Y AÑADIRLAS A UNA VARIABLE RESPECTIVAMENTE
    a=100/1.60934
    b=litros/3.785411784
    c=a/b
# PASO 3 DEVOLVEMOS EL RESULTADO DE LA ECUACION A LA FUNCION
    return c
# PASO 4 REALIZAMOS NUEVAMENTE LOS ANTERIORES PASOS PARA ENCONTRAR LAS ECUACIONES
def L100tompg(millas):
    d=millas*1.609334
    e=1*3.78541178
    f=e/(d/100)
    return f
# PASO 5 ASIGNAMOS LOS VALORES QUE SERAN REEMPLAZADOS A LAS FUNCIONES 
print(mpgtoL100km(3.9))
print(mpgtoL100km(7.5))
print(mpgtoL100km(10.))
print(L100tompg(60.3))
print(L100tompg(31.4))
print(L100tompg(23.5))