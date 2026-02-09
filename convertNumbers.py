"""
Module for converting decimal numbers to binary and hexadecimal.
This script reads from a file and outputs results to console and a file.
"""
# pylint: disable=invalid-name
import sys
import time
def to_binary(n):
    """Convierte un número entero a binario usando el algoritmo de división."""
    if n == 0:
        return "0"
    binary = ""
    is_negative = n < 0
    n = abs(int(n))
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return "-" + binary if is_negative else binary

def to_hexadecimal(n):
    """Convierte un número entero a hexadecimal manualmente."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    is_negative = n < 0
    n = abs(int(n))
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n = n // 16
    return "-" + hexadecimal if is_negative else hexadecimal

def main():
    """Main function to handle file input and conversion."""
    start_time = time.time()
    # Validación de argumentos de línea de comandos
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        return

    filename = sys.argv[1]
    results_list = []

    # Manejo de archivos y datos inválidos
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                item = line.strip()
                if not item:
                    continue
                try:
                    num = int(float(item))  # Convertimos a entero para bases
                    binary = to_binary(num)
                    hexa = to_hexadecimal(num)
                    results_list.append((item, binary, hexa))
                except ValueError:
                    # Muestra el error y continúa la ejecución
                    print(f"Error: Datos inválidos detectados: '{item}'")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
        return

    # Formateo de resultados y tiempo
    elapsed_time = time.time() - start_time
    header = f"{'ITEM':<10} {'BINARIO':<20} {'HEXADECIMAL':<15}"
    separator = "-" * 50
    output = []
    output.append(f"Resultados de: {filename}")
    output.append(header)
    output.append(separator)
    for item, b, h in results_list:
        output.append(f"{item:<10} {b:<20} {h:<15}")
    output.append(separator)
    output.append(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")
    # Imprimir en pantalla y guardar en archivo
    final_text = "\n".join(output)
    print(final_text)

    with open("ConvertionResults.txt", "a", encoding='utf-8') as out_file:
        out_file.write(final_text + "\n\n")

if __name__ == "__main__":
    main()
    