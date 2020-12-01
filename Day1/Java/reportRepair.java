package Dia1;

import java.io.*;
import java.util.*;

/**
 * Write a description of class reportRepair here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class reportRepair
{
    public static void main(String [] args) {
        File archivo = null;
        FileReader fr = null;
        BufferedReader br = null;
        ArrayList<Integer> datos = new ArrayList<Integer>();

        try {
            archivo = new File("/Users/Jordiros27/Desktop/AdventOfCode2020/Day1/Java/datos.txt");
            fr = new FileReader(archivo);
            br = new BufferedReader(fr);

            //Lectura del fichero
            String linea;
            while((linea = br.readLine()) != null) {
                int añadir = Integer.parseInt(linea);
                datos.add(añadir);
            }

            //Tratado de datos 1
            for(int i = 0; i < datos.size(); i++) {
                for (int j = i; j < datos.size(); j++) {
                    if (datos.get(i) + datos.get(j) == 2020) {
                        System.out.println(datos.get(i) * datos.get(j));
                    }
                    
                    
                }
            }

            //Tratado de datos 2
            for(int i = 0; i < datos.size(); i++) {
                for (int j = i; j < datos.size(); j++) {
                    for(int k = j; k < datos.size(); k++) {
                        if (datos.get(i) + datos.get(j) + datos.get(k) == 2020) {
                            System.out.println(datos.get(i) * datos.get(j) * datos.get(k));
                        }
                    }
                    
                }
            }
        } catch (Exception e) {
            System.out.println(e);
        }
        
    }
}
