import java.util.Scanner;

abstract class Figure{

	int d1;
	int d2;

	Figure(int a, int b){
		d1=a;
		d2=b;
	}

	abstract void area();


}

class Rectangle extends Figure{
	Rectangle(int l, int b){
		super(l,b);
	}	
	void area(){
		System.out.println("Area = "+(d1*d2));
	}
}

class Triangle extends Figure{
	Triangle(int h, int b){
		super(h,b);
	}	
	void area(){
		System.out.println("Area = "+(0.5*d1*d2));
	}
}

class Sqaure extends Figure{
	Sqaure(int a){
		super(a,a);
	}	
	void area(){
		System.out.println("Area = "+(d2*d1));
	}
}

class FigureDemo{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);


		Figure obj;

		System.out.println("Enter Length and breadth of rectangle");
		int len = sc.nextInt();
		int bre = sc.nextInt();
		obj = new Rectangle(len,bre);
		obj.area();
		

		System.out.println("Enter Height and base");
		int h = sc.nextInt();
		int base = sc.nextInt();
		obj = new Triangle(h,base);
		obj.area();


		System.out.println("Enter side of square");
		int side = sc.nextInt();
		obj = new Sqaure(side);
		obj.area();



	}
}