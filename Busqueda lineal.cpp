// Función que busca dentro del arreglo
int buscarElemento(int arreglo[], int longitudDeArreglo, int busqueda) {
  for (int i = 0; i < longitudDeArreglo; i++) {
    int elementoActual = arreglo[i];
    if (elementoActual == busqueda) return i;
  }
  // Final del ciclo, no encontramos nada así que regresamos
  // -1
  return -1;
}

int main() {
 int indice = -1;
 
  // Veamos otro ejemplo con números
  // y la función

  int numeros[] = {
      1, 2, 5, 50, 11, 50, 20,
  };
  int longitud = sizeof(numeros) / sizeof(numeros[0]), numeroBuscado = 20;

  int indiceDeNumeroBuscado = buscarElemento(numeros, longitud, numeroBuscado);
  if (indiceDeNumeroBuscado == -1) {
    std::cout << "No encontrado\n";
  } else {
    std::cout << "Encontrado en el indice " << indiceDeNumeroBuscado << std::endl;
  }
}

