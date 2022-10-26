class Main { 
    
    public static int linearSearch(int arr[], int elementToSearch) {

    for (int index = 0; index < arr.length; index++) {
        if (arr[index] == elementToSearch)
            return index;
    }
    return -1;
}
    
     public static void main (String args []) { 
        int arr[] = {1, 2, 8, 10, 24, 7, 90, 55, 69, 100}; 
        int elementToSearch = 3; int salida = linearSearch (arr, elementToSearch); 
        if (salida == -1)
        System.out.println ("El número que está buscando no está presente en la matriz");
        else 
        System.out.println ("El número " + elementToSearch + " está presente en la matriz en la posición " + salida); 
        
    } 
}


 // Mostrar arreglo.
 for (int i = 0; i < numeros.length ; i++)
     System.out.println ( "numero["+i+"]: "+  numeros[i]);

 int resultado = BusquedaAlgoritmo.buscar(numeros, 65);

 if (resultado != -1) {
     System.out.println ( "Encontrado en posición: "+  resultado);
 } else {
     System.out.println ( "El dato no se encuentra en el arreglo, o el arreglo no estÃ¡ ordenado."  );
 }
 
    }
}

