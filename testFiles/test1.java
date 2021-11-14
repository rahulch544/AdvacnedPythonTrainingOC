import java.io.*;
 
class test1{
public static void main(String a[]){
try{
 
String prg = "import sys\nprint (int(sys.argv[1])+int(sys.argv[2]))\n";
BufferedWriter out = new BufferedWriter(new FileWriter("test1.py"));
out.write(prg);
out.close();
int number1 = 10;
int number2 = 32;
Process p = Runtime.getRuntime().exec("python test1.py "+number1+" "+number2);
System.out.println("getting  error1");
BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
System.out.println("getting  error2");

int output = Integer.parseInt(in.readLine());
System.out.println("value is : "+output);

}catch(Exception e){
    System.out.println("getting  error3");
}
}
}