"""Script de la Parte 3: Refactorización PEP 8."""

def calculate_promedio(numbers: list[float]) -> float:
    """Calcula el promedio de una lista de números."""
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

if __name__ == "__main__":
    print(calculate_promedio([10, 20, 30]))