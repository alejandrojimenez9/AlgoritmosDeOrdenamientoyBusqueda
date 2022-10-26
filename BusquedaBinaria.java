class BusquedaAlgoritmo {
    public static int buscar( int [] arreglo, int dato) {
 int inicio = 0;
 int fin = arreglo.length - 1;
 int pos;
 while (inicio <= fin) {
     pos = (inicio+fin) / 2;
     if ( arreglo[pos] == dato )
       return pos;
     else if ( arreglo[pos] < dato ) {
  inicio = pos+1;
     } else {
  fin = pos-1;
     }
 }
 return -1;
    }
}
public class BusquedaBinaria {
    public static void  main (String args[]) {
 // Llenar arreglo
 int [] numeros = new int [35];
 for (int i = 0; i < numeros.length ; i++)
     numeros [i] = i*i; 
      

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

