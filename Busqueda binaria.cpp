#include <iostream>
int main(){
    int lista[]={1,2,3,4,5},valor,con,inf,sup,mitad,tam;
    bool encontrado=false;
    tam=sizeof(lista)/sizeof(*lista);
    regresa:
    con=0;
    inf=0;
    sup=tam;
    std::cout<<"Ingresa un valor de la siguiente lista: ";
    for (int i = 0; i < tam; i++)
    {
        std::cout<<lista[i]<<" ";
    }
    std::cout<<"\nIngresa el valor:";
    std::cin>>valor;
    while ( (inf<=sup) && con<tam )
    {
        mitad=(inf+sup)/2;
        if(lista[mitad]==valor){
            encontrado=true;
            break;
        }
        if(lista[mitad]>valor){
            sup=mitad;
            mitad=(inf+sup)/2;
        }
        if(lista[mitad]<valor){
            inf=mitad;
            mitad=(inf+sup)/2;
        }
        con++;
    }
    if( encontrado==false ){
       std::cout<<"No se encuentra el valor";
       
    }
    if(encontrado==true){
        std::cout<<"El valor fue encontrado en la posicion: "<<mitad<<"";
    }
   return 0;
}
