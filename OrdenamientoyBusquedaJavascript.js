//Burbuja
Array.prototype.ordenarDatosBurbuja = function() {
    let ordenado = false;

    while(!ordenado) {
        ordenado = true;

        for (let i = 0; i < this.length - 1; i++) {
            if (this[i] > this[i + 1]) {
                let temporal = this[i + 1];
                this[i + 1] = this[i];
                this[i] = temporal;

                ordenado = false;
            }
        }
    }

    return this;
}

let numeros = [7, 2, 5, 13, 11, 29, 23];
console.log(numeros);

console.log();

let numerosOrdenados = numeros.ordenarDatosBurbuja();

console.log(numerosOrdenados); 

//Quicksort
function quickSort(array) {

  if (array.length < 1) {
    return [];
  }

  var left = [];
  var right = [];
  var pivot = array[0];

  for (var i = 1; i < array.length; i++) {
    if (array[i] < pivot) {
      left.push(array[i]);
    }
    else {
      right.push(array[i]);
    }
  }

  return [].concat(quickSort(left), pivot, quickSort(right));
}

console.log(quickSort([4, 9, 2, 1, 6, 3, 8]));

//Seleccion
function insertionSort(datos) {
    for (let i = 1; i < datos.length; i++) {
        let j = i - 1;
        let auxiliar = datos[i];

        while (j >= 0 && datos[j] > auxiliar) {
            datos[j + 1] = datos[j];
            --j;
        }

        datos[j + 1] = auxiliar;
    }

    return datos;
}

let primos = [13, 2, 19, 5, 3, 7, 11, 23];
console.log(primos);

console.log();

let resultado = insertionSort(primos);
console.log(resultado);

//Busqueda binaria
function busquedaBinaria(datos, valor) {
    let izquierda = 0;
    let derecha = datos.length - 1;

    while (izquierda <= derecha) {
        let mitad = Math.floor((izquierda + derecha) / 2);
        let dato = datos[mitad];

        if (dato == valor) {
            return mitad;
        } else if (valor > dato) {
            izquierda = mitad + 1;
        } else {
            derecha = mitad - 1;
        }
    }

    return -1;
}

let primos = [2, 3, 5, 7, 11, 13, 17, 19];
let numero = 19;
console.log("número:" +numero);
console.log(primos);
console.log("posición:" +busquedaBinaria(primos, numero));

//Busqueda lineal
function busquedaLinear(arr, val) {
  for(let i = 0 ; i < arr.length ; i++){
      if(arr[i] === val) {
          return i;
      }
  }
  return -1;
}


