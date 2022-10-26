/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.metododeseleccion;

/**
 *
 * @author Usuario
 */
public class MetodoDeSeleccion {

    public static int[] seleccion(int[] tabla) {
     int menor;
     int aux;
        for (int i=0; i<tabla.length-1; i++) {
        menor = tabla[i];
        for (int j=i+1; j<=tabla.length-1; j++) {
            if (tabla[j] < menor) {
                  aux = tabla[j];
                  tabla[j] = menor;
                  menor = aux;
    }
}
        tabla[i] = menor;
    }
        return tabla;
}

    public static void main(String[] args) {
        int[] tabla = {5,78,2,3,1,25,7,1,90,8,1,45};
        int[] nuevaTabla = seleccion(tabla);
            for (int i=0; nuevaTabla.length>=i; i++) {
                System.out.println(nuevaTabla[i]);
        }
    }
}