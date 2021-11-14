
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.FileWriter;
import java.io.*;
import java.lang.Process;
public class abs_rm {
    
    public static void main(String[] args){
    String command = "/ade_autofs/ud222_db/GITOOLS_MAIN_LINUX.X64.rdd/LATEST/gitools/bin/absfarmctl backport-analysis  --cand "+ "30953224";
    // try{
    //     Object o = executeShellCMDS(command,env);
    //     return o;
    // }
    // catch(Exception e){
    //     e.printStackTrace();
    //     return "*************Code is failed***********";
    // }
    

    String output="";
    try{
    String backportsList = "30953224";
    System.out.println("****** " + backportsList);
    Process p = Runtime.getRuntime().exec("python abs.py "+backportsList);
    BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
    System.out.println("start******rchamant");
    // System.out.println(in.readLine());
    System.out.println(" end******rchamant");
   
    StringBuilder output_p = new StringBuilder();
    String line;
    while (( line = in.readLine()) != null) {
        output += line;
    }
    File file = new File("");
String currentPath = file.getAbsolutePath();
System.out.println("Current path is:: " + currentPath);
    // output = output_p;
    System.out.println(output);
    System.out.println(" end******rchamant");
  
    p.destroy();
}
      catch(Exception e){
        e.printStackTrace();
        System.out.println( "*************Code is failed***********");
    }
}
}
