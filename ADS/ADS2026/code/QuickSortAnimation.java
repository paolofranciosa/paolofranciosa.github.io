/*
Ordina un'array con l'algoritmo quick sort

L'algoritmo e' descritto nel testo di Cormen, Leiserson, Rivest,
Introduzione agli algoritmi
Jackson Libri
Volume 1, Capitolo 8 (fino a 8.3 compreso) pagg.145-153
*/		


import javax.swing.JOptionPane;

public class QuickSortAnimation
{
	public static int partiziona(int[] v, int from, int to)
	{
		int separatore=v[from];
		int i=from+1;
		int j=to;
		while(i<j)
		{
			while(i<j && v[i]<=separatore)
				i++;
// ora i indica un valore maggiore di separatore
// oppure e' maggiore di j
			while(i<j && v[j]>=separatore)
				j--;
// ora j indica un valore minore di separatore
// oppure e' minore o uguale a i
			if(i<j)
			{
				int app=v[i];
				v[i]=v[j];
				v[j]=app;
			}
		}
		if(v[i]>separatore)
		{
			i--;
		}
// posiziona correttamente il separatore
		int app=v[i];
		v[i]=v[from];
		v[from]=app;
		return i;
	}


	public static void quick(int[] v, int from, int to)
// ordina l'intervallo da from a to, estremi inclusi
	{
		if(from>=to)
			return;
		else
		{
			int separazione=partiziona(v, from, to);
			printArraySeparato(v, from, separazione, to);
			JOptionPane.showMessageDialog(null, "partition terminated on interval "+from+"-"+to+"\npivot "+v[separazione]+" in position "+separazione);
			quick(v, from, separazione-1);
			quick(v, separazione+1, to);
		}
	}
	
	
	public static void quickSort(int[] v)
	{
		quick(v, 0, v.length-1);
	}
		
	
	public static int[] leggiArrayInt()
	{
		int[] a=new int[20];
		for(int i=0; i<a.length; i++)
			a[i] = (int)(Math.random()*100);
// evitiamo la lettura per testare piu' agevolmente il codice

//		int n=Integer.parseInt(JOptionPane.showInputDialog("Dimensione dell'array?"));
//		int[] a = new int[n];
//		for(int i=0; i<a.length; i++)
//			a[i]=Integer.parseInt(JOptionPane.showInputDialog("digita elemento ["+i+"]"));

		return a;
	}

	public static void printArray(int[] v, int from, int to)
	{
		for(int i=0; i<4*from; i++)
			System.out.print(" ");

		for(int i=from; i<=to; i++)
			System.out.printf("%4d", v[i]);
		System.out.println();
	}


	public static void printArraySeparato(int[] v, int from, int sep, int to)
	{
		for(int i=0; i<=4*sep; i++)
			System.out.print(" ");
		System.out.printf("*%2d*\n", v[sep]);
		
		for(int i=0; i<4*from; i++)
			System.out.print(" ");		
		for(int i=from; i<=sep-1; i++)
			System.out.printf("%4d", v[i]);
		System.out.print("    ");
		for(int i=sep+1; i<=to; i++)
			System.out.printf("%4d", v[i]);
		System.out.println();
	}


	public static void main(String[] x)
	{
		int[] vettore;
		vettore=leggiArrayInt();
		System.out.println("before sorting");
		printArray(vettore, 0, vettore.length-1);
		
		quickSort(vettore);
		
		System.out.println("after sorting");
		printArray(vettore, 0, vettore.length-1);

		System.exit(0);
	}
}
