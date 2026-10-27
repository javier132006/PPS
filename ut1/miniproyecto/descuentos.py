"""PPS UT1 · Mini-proyecto para la práctica de pruebas y cobertura (PPS-E2).

INCIDENCIA #17 (reportada por soporte): un cliente aplicó un cupón del 150 %
y la tienda le devolvió un precio NEGATIVO (le "regalamos" dinero).
Tu trabajo: escribir primero el TEST DE REGRESIÓN que reproduce el fallo,
verlo en rojo, corregir el código y verlo en verde.
"""
import math

def aplicar_descuento(precio: float, pct: float) -> float:

    if not (math.isfinite(precio) and math.isfinite(pct)):
        raise ValueError("valor no finito")

    if precio < 0:
        raise ValueError("precio negativo")
    if not 0 <= pct <= 100:
        raise ValueError("porcentaje fuera de rango")
    return round(precio * (1 - pct / 100), 2)


def es_precio_valido(precio: float) -> bool:
    return precio >= 0
